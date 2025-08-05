from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_core.runnables import RunnableLambda

load_dotenv()

# 1. 템플릿 정의
template = '다음 문장을 3줄로 요약하시오.'
prompt = PromptTemplate(input_variables=['article'], template=template)

# 2. 모델 정의
llm = OpenAI()

# 3. 체인 생성
print_line_by_lie = RunnableLambda(
    lambda x: {
        "summary": [line.strip() for line in x.split('\n')]
    }
)


# chain = prompt | llm | RunnableLambda(lambda x: {'summary': x.strip()})
chain = prompt | llm | print_line_by_lie

# 4. 입력 및 호출
input_text = {'article':'''


'''}

result = chain.invoke(input_text)
print('최종결과 : ', result)

# lines = result['summary'].split('\n')
# for line in lines:
#     print(line)