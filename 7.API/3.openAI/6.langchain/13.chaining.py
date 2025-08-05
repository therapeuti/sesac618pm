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

# 4. 체인 만들기 LCEL (LangCHain Expression Language)
chain = prompt | llm | parser

# 5. 결과 도출 (위의 생성기들을 연결한 체인을 실행함.)
inputs = {'company': 'high-tech startup', 'product':'mobile games'}

result = chain.invoke(inputs)

print('최종결과: ', result)

