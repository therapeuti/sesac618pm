from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

from langchain_chroma import Chroma

import os

load_dotenv()


PERSIST_DIR = './chroma_db'

def create_vector_db():
    documents = TextLoader('./nvme.txt', encoding='utf-8').load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)  # 1000/200, 2000/500
    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    store = Chroma.from_documents(texts, embeddings, collection_name='nvme', persist_directory=PERSIST_DIR)
    return store

def load_vector_db():
    embeddings = OpenAIEmbeddings()
    store = Chroma(collection_name='nvme', embedding_function=embeddings, persist_directory=PERSIST_DIR)
    return store


if os.path.exists(PERSIST_DIR):
    print('db 로딩 중')
    store = load_vector_db
else:
    print('db 생성 중')
    store = create_vector_db()
print('db 준비됨')

llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.2) # RAG모델에서는 온도를 낮추는게 일반적
retriever = store.as_retriever(search_kwars={'k':5}) # 유사도 기준 상위 3개 문서를 고르시오.
template = '''
다음 내용을 바탕으로 질문에 답변해주세요. 해당 문서에 내용이 없을 경우, 모른다고 답변하고, 출처는 없음으로 표시하세요.
{context}
질문 : {question}

답변을 작성하고, 마지막에 참고한 문서의 "출처 : [파일명:청크번호]" 형식으로 참고한 문서 정보를 모두 명시해주세요.
예시) 출처: nvme.txt: 1, ssd.txt:3
출처 내에 답변이 없을 경우 출처에 '없음'이라고 명시해주세요.
'''

prompt = ChatPromptTemplate.from_template(template)

chain = {'context': retriever, 'question': RunnablePassthrough()} | prompt | llm | StrOutputParser()



response = chain.invoke('NVME와 SATA의 차이점을 100글자로 요약해주세요')
print(f'A : {response}')



