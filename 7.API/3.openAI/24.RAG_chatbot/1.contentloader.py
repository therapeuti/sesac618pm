from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

load_dotenv()

# 1. 문서 로딩

import os
print(os.path.exists("./nvme.txt"))  # True가 나와야 함
print(os.getcwd())  # 현재 작업 디렉토리 확인


loader = TextLoader('./nvme.txt', encoding='utf-8')
documents = loader.load()

# 2. 문서를 청쿠(chunk) 단위로 자르기
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)  # 1000/200, 2000/500
texts = text_splitter.split_documents(documents)

print(texts)

# 3. 임베딩 하기
embeddings = OpenAIEmbeddings()
store = Chroma.from_documents(texts, embeddings, collection_name='nvme')
print(store)


# 4. 실제로 질문할 준비
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.2) # RAG모델에서는 온도를 낮추는게 일반적

retriever = store.as_retriever()

template = '''
다음 내용을 바탕으로 질문에 답변해주세요.
{context}
질문 : {question}
'''

prompt = ChatPromptTemplate.from_template(template)

# 5. 체인 구성 : 사용자 질문은 question에 담아서 넘어감.
# context는 retiriever로부터 추출해서 context에 채워줄 예정
# 프롬프트 -> LLM -> 응답
chain = {'context': retriever, 'question': RunnablePassthrough()} | prompt | llm

question = 'NVME와 SATA의 차이점을 100글자로 요약해주세요.'
response = chain.invoke(question)

print(response.content)

# 6. 확인작업
context_docs = retriever.invoke(question)
print('-------------------검색된 문서 내용은?---------------')
for i, doc in enumerate(context_docs, start=1):
    print(f'[=={i}==] {doc.page_content}')