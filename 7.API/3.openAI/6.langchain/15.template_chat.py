from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate # 이전까지 배운 것
from langchain_core.prompts import ChatPromptTemplate # 지금부터 할 거
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

#1. 프롬프트 템플릿
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content='You ar a naming consultant for new companies'),
    HumanMessage(content='What is a good name for a {company} that makes {product}')
])

# 현업에서 많이 쓰는 축약형
# prompt_short =  ChatPromptTemplate.from_messages([
#     ('system', 'You are a naming consultant for new companies'),
#     ('human', 'What is a good name for a {company} that makes {product}?')
# ])

#2. 모델 생성
llm = ChatOpenAI(model='gpt-3.5-turbo') # chat 모델 중에 하나를 고를 것

#3. 파서 생성
parser = StrOutputParser()

#4. 입력값 정의 하고 invoke로 호출 3줄로 해도 됨.
# messages = ''
# response = llm.invoke(message)
# output = parser.invoke(response)

chain = prompt | llm | parser |RunnableLambda(lambda x: {'response': x})

inputs = {'company': 'high-tech startup', 'product':'electrical automobile'}
result = chain.invoke(inputs)

print('최종결과: ', result)