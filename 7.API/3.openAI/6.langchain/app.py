import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

llm = OpenAI()

print(llm)

prompt = '오늘 점심에 먹을 메뉴는'

result = llm.invoke(prompt)
print(result)