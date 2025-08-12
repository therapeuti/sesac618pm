from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.vectorstores.utils import filter_complex_metadata

import os

load_dotenv()

pdf_filename = "./DATA/Python_시큐어코딩_가이드(2023년_개정본).pdf"
PERSIST_DIR = './chroma_db'
COLLECTION_NAME = 'secure_coding_python'

def create_db():
    loader = PyPDFLoader(pdf_filename)
    pages = loader.load()
    # print(pages)
    # print(f'총 페이지수 : {len(pages)}')
    # print(f' 100 페이지 내용 : \n{pages[100].page_content}')
    # print(f' 100 페이지 메타데이터 : \n{pages[100].metadata}')

    pages = filter_complex_metadata(pages) # 메타데이터 먼저 필터링.....
    # 페이지별 메타데이터 추가 (딕셔너리 형태로)
    for i, page in enumerate(pages):
        page.metadata.update({
            'page': i+1, 
            'source': 'Python 시큐어코딩 가이드 2023년 개정본'
        })
    
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator="\n\n", # 문서 분할 기준
        chunk_size=2000, #최대 2000토큰
        chunk_overlap=500 # 중복 500토큰 포함
    )

    texts = text_splitter.split_documents(pages)
    # print(texts[10])

    embeddings = OpenAIEmbeddings()

    store = Chroma.from_documents(texts, embeddings, collection_name='secure_coding_python', persist_directory=PERSIST_DIR)
    return store



# store = create_db()

def load_db():
    embeddings = OpenAIEmbeddings()
    store = Chroma(collection_name='secure_coding_python', embedding_function=embeddings, persist_directory=PERSIST_DIR)
    return store

def check_collection_exists(persist_dir, collection_name):
    embeddings = OpenAIEmbeddings()
    store = Chroma(collection_name=collection_name, embedding_function=embeddings, persist_directory=persist_dir)

    results = store.get(limit=1)
    print(f'결과의 길이: {len(results)}')
    return bool(results['ids'])


    if check_collection_exists(PERSIST_DIR, COLLECTION_NAME):
        print('DB 로딩 중')
        store = load_db()
    else:
        print('db 생성 중')
        store = create_db()
    print('db 준비완료')




llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.2)
template = '''
주어진 문서 내용을 바탕으로 질문에 답변해주세요.
문서내용 : {content}
질문: {question}
답변할 때 반드시 출처도 명시해주세요.
예: (출처: 페이지 15, Python 시큐어코딩 가이드)
'''

prompt = ChatPromptTemplate.from_template(template)

retriever = store.as_retriever(search_kwargs={'k':5})

chain = ({'content':retriever, 'question':RunnablePassthrough()}) | prompt | llm | StrOutputParser()

question = '시큐어코딩의 주요 기법들에 대해서 리스트 형태로 요약해서 설명해줘'

response = chain.invoke(question) # question이 RunnablePassthrough를 통해 'question'에 들어감.
print('Q : ', question)
print('A : ', response)

# db가 있으면 안 만들고, 없으면 만들기
# 답변 시 출처, 페이지 함께 출력