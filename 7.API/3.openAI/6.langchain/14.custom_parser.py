from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda #내가 원하는 한 줄짜리 함수 실행하게 만듦
from langchain_openai import OpenAI
from dotenv import load_env
load_env()

# 1. 프롬프트 생성

template = 'You are a naming consultant. Suggest 5 creative company name for a {company} that makes {product}'
prompt = PromptTemplate(
    input_variables=['product'],
    template=template
)

# 2. 모델 생성
llm = OpenAI()

def my_function(output):
    print('raw출력값은')
    print(output)
    cleaned_output = output.strip().replace('"', '').strip() # 다양한 공백 제거
    return {'final_response': cleaned_output}


# 4. 체인 만들기 prompt -> llm -> ouput parser(내가 정의할 lambda)
# 이 예시에서 정의한 lambda는 {'response': result} 형태로 담기 위한 커스텀 함수.
# chain = prompt | llm | RunnableLambda(lambda x: {"response": x.strip()})
chain = prompt | llm | RunnableLambda(my_function)

# 5. 결과 도출 (위의 생성기들을 연결한 체인을 실행함.)
inputs = {'company': 'high-tech startup', 'product':'mobile games'}

result = chain.invoke(inputs)

print(f'최종결과: \n{result}')

