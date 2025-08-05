from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import CommaSeparatedListOutputParser
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

# 3. 출력 파서 생성
parser = StrOutputParser()
parser_csv = CommaSeparatedListOutputParser()

# 4. 결과 도출
inputs = {'company': 'high-tech startup', 'product':'mobile games'}

filled_prompt = prompt.format(**inputs)
llm_output = llm.invoke(filled_prompt)
result_str = parser.invoke(llm_output)
result_csv = parser_csv.invoke(llm_output)

print('일반 문자열')
print(result_str)
print('csv 리스트')
print(result_csv)

