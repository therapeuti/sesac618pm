from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda


load_dotenv()

template = '다음 문장을 한글로 번역하시오. \n{article}'
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template('당신은 번역 전문가입니다.'),
    HumanMessagePromptTemplate.from_template(template)
])

prompt =

# 모델 정의
llm = ChatOpenAI(temperature=0.5)

# 체인 생성
chain = prompt | llm | RunnableLambda(lambda x:{'translated': x.content.strip()})


# 4. 입력 및 호출
input_text = {
    # 'recipient':'마케팅팀', 'topic':'신제품 출시를 위한 전략'
    'recipient':'인사팀', 'topic':'버그를 많이 만든 개발자 해고'
    }

response = chain.invoke(input_text)
print(response)