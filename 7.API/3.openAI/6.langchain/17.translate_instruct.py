from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_core.runnables import RunnableLambda

load_dotenv()

# 1. 템플릿 정의
template = '다음 문장을 영어로 번역하시오. \n\n{article}'
prompt = PromptTemplate(input_variables=['article'], template=template)

# 2. 모델 정의
llm = OpenAI(temperature=0.5)

# 3. 체인 생성
chain = prompt | llm | RunnableLambda(lambda x: {'translated': x.strip()})

# 4. 입력 및 호출
input_text = {'article':'''


'''}

result = chain.invoke(input_text)
print('최종결과 : ', result)
