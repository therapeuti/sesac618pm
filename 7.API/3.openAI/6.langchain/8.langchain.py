import os
from dotenv import load_dotenv
from langchain_openai import OpenAI # completion 모델
from langchain_openai import ChatOpenAI # chat 모델 (QA모델)

load_dotenv()


print('---------- 1 ------------')
llm = OpenAI(max_tokens=1000)
print(llm)
prompt = '인공지능이란'
result = llm.invoke(prompt)
print(result)


print('---------- 2 ------------')
llm2 = ChatOpenAI(model='gpt-3.5-turbo')
prompt = '인공지능이란'
result2 = llm2.invoke(prompt)
print(result2.content)


print('---------- 3 ------------')
from langchain.schema import HumanMessage, SystemMessage

llm2 = ChatOpenAI(model='gpt-3.5-turbo')
prompt = [
    SystemMessage(content='당신은 인공지능 분야의 전문가입니다.'),
    HumanMessage(content='인공지능이란')
]
result3 = llm2.invoke(prompt)
print(result3.content)


print('---------- 3 ------------')
from langchain.schema import HumanMessage, SystemMessage, AIMessage

llm2 = ChatOpenAI(model='gpt-3.5-turbo')
prompt = [
    SystemMessage(content='당신은 요리 레시피 연구가입니다.'),
    HumanMessage(content='디저트 케이크를 맛있게 만들려면'),
    AIMessage(content='신선한 재료를 사용하고, 정확한 계량과 온도조절로 부드럽고 촉촉한 식감을 살리는 것이 비결입니다.'),
    HumanMessage(content='디저트 케이크를 맛있게 만들려면')
]
result3 = llm2.invoke(prompt)
print(result3.content)
