# 요약, 번역, 메일 chat 모델로 구현
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# 프롬프트
template = '당신은 풀스택 개발자이자, 자바, 파이썬 등 여러 프로그래밍 언어를 사용할 줄 아는 개발자이면서 풀스택 개발 교육을 하고 있는 교육강사입니다. 교육생의 질문에 대해서 자세하게 답변해주는 이메일을 작성하세요. 학생의 질문내용: {question}'
prompt = PromptTemplate(input_variables=['question'], template=template)
# 모델
llm = ChatOpenAI(model='gpt-4o')
print(llm)
chain = prompt | llm

input_text = {'question':'''현재 llm을 이용한 서비스를 만드는 프로젝트를 진행 중입니다. 기술스택은 프론트:리액트, 백엔드:자바 spring, AI백엔드: 파이썬 flask입니다. 현재 독립적으로 각각 개발을 하고 있으며 github organization을 통해 각각의 레포지토리로 소스코드 관리를 하고 있습니다. 여러가지 궁금증이 있는데, 아래 질문사항에 답변해주세요. 
1. 자바 백엔드는 spring을 사용하고 있어서 db로 mysql을 사용하는게 편하다고 하는데, 그게 무슨의미인지 알려주세요.
2. 자바 스프링 백엔드의 db로 mysql을 사용하는데, 굳이 파이썬 서버를 위한 db를 따로 만들 이유가 있을지, 아니면 같이 my sql을 사용하면 되는지, 그렇다면 my sql을 사용하기 위해서 파이썬 서버에서 설정해야하는 것들이 무엇이 있는지, 자바 개발자에게 어떤 것들을 알려달라고 해야하는지 알려주세요.
3. 사용자가 서술형으로 답변한 텍스트를 가지고 유사도 계산을 통해 유사도 점수가 높은 사람끼리 매칭해주기 위한 과정을 단계별로 상세힐 알려주세요.
              '''}

response = chain.invoke(input_text)
print(response)
print(response.content)


# content="안녕하세요,\n\n프로젝트 진행에 있어 여러 가지 궁금증이 있으신 것 같아 기쁜 마음으로 답변드리겠습니다. 질문 사항에 대해 하나씩 차근차근 설명 드리겠 습니다.\n\n1. **자바 백엔드에서 Spring을 사용하는 경우 MySQL 사용의 의미**:\n   - **Spring과 MySQL의 친화성**: Spring 프레임워크는 다양한 데이터베이스와의  연동을 쉽게 할 수 있도록 지원하지만, MySQL은 특히 널리 사용되고 있기 때문에 수많은 지원 자료와 커뮤니티, 플러그인이 존재합니다. Spring Data JPA 같은 라이브 러리를 통해 MySQL과의 매핑이 용이하고, 데이터베이스 접근 코드의 양을 줄여 생산성을 높일 수 있습니다.\n\n2. **Python 서버와 Java 서버간의 DB 통합 여부**:\n   - **단일 DB 사용**: 두 백엔드 서비스가 동일한 데이터베이스를 이용할 필요가 있는 공통의 데이터를 다루고 있다면, 한 개의 MySQL 데이터베이스를 공유하는 것이  좋습니다. 이렇게 하면 데이터 일관성을 유지하고, 데이터 중복을 피할 수 있습니다. Python 서버에서도 MySQL을 접근할 수 있도록 드라이버 설치가 필요합니다.\n     - **설치 및 설정**:\n       1. `mysql-connector-python` 또는 `PyMySQL` 등의 라이브러리를 설치합니다. (예: `pip install mysql-connector-python`)\n       2. SQLAlchemy 같은 ORM을 사용하여 데이터베이스 조작을 좀 더 쉽게 할 수 있습니다.\n       3. 데이터베이스 연결 정보를 Flask 설정에 추가합니다.\n         ```python\n         app.config['MYSQL_DATABASE_USER'] = 'your_user'\n         app.config['MYSQL_DATABASE_PASSWORD'] = 'your_password'\n         app.config['MYSQL_DATABASE_DB'] = 'your_db'\n         app.config['MYSQL_DATABASE_HOST'] = 'your_host'\n         ```\n   - **Java 개발자와의 협업**:\n     - 데이터베이스 연결  정보와 스키마에 대한 공유가 중요합니다. 데이터 모형에 변화가 있을 때 서로 조율할 수 있도록 테이블 스키마에 대한 문서를 유지하는 것이 좋습니다.\n     - 데이 터베이스 접근에 필요한 계정 정보와 권한 설정 방법에 대해 공유가 필요합니다.\n\n3. **유사도 계산을 통한 사용자 매칭 과정**:\n   - **단계 1: 데이터 전처리**\n     - 사용자의 서술형 데이터를 수집하고, 필요한 전처리를 수행합니다. 여기에는 텍스트 클리닝, 불용어 제거, 표제어 추출 등이 포함됩니다.\n   - **단계 2: 텍스트 임베딩**\n     - 자연어 처리(NLP) 모델을 사용하여 텍스트 데이터를 벡터로 변환합니다. BERT, GPT, Sentence-BERT와 같은 다양한 임베딩 기법을 사용할 수 있습 니다. 이 단계에서는 각 사용자 응답을 고정된 차원의 벡터로 변환하게 됩니다.\n   - **단계 3: 유사도 계산**\n     - 코사인 유사도 또는 유클리디안 거리 등의 방 법을 활용하여 임베딩된 벡터 간의 유사도를 계산합니다. 두 벡터 간의 코사인 유사도가 높을수록 두 사용자의 응답이 유사하다고 말할 수 있습니다.\n   - **단계 4: 매칭 알고리즘 구현**\n     - 유사도 점수를 기반으로 사용자를 매칭합니다. 특정 임계값을 넘어가는 유사도 점수를 가진 사용자들끼리 쌍을 이루거나, 상위 N명의 유사한 사용자 그룹을 형성하는 방법으로 구현할 수 있습니다.\n   - **단계 5: 결과 피드백 및 반복**\n     - 매칭 결과를 평가하고, 필요하면 알고리즘을 조정하거나 데이터 전처리 방법을 개선하여 반복 학습을 통해 성능을 향상시킵니다.\n\n이외에도 추가적인 질문이 있으시면 언제든지 연락주시기 바랍니다. 프로젝트가 성공적으로 진행되기를 기원하며, 도움될만한 자료나 조언이 필요하면 편하게 문의하세요.\n\n감사합니다." additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 900, 'prompt_tokens': 343, 'total_tokens': 1243, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_07871e2ad8', 'id': 'chatcmpl-C1DcgliCm0sSvWRkIormpElDMTxif', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='run--cf1d7e31-bcf7-4653-95a8-f04eb6aad91f-0' usage_metadata={'input_tokens': 343, 'output_tokens': 900, 'total_tokens': 1243, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}

# 안녕하세요,

# 프로젝트 진행에 있어 여러 가지 궁금증이 있으신 것 같아 기쁜 마음으로 답변드리겠습니다. 질문 사항에 대해 하나씩 차근차근 설명 드리겠습니다.

# 1. **자바 백엔드에서 Spring을 사용하는 경우 MySQL 사용의 의미**:
#    - **Spring과 MySQL의 친화성**: Spring 프레임워크는 다양한 데이터베이스와의 연동을 쉽게 할 수 있도록 지원하지만, MySQL은 특히 널리 사용되고 있기 때문에 수많은 지원 자료와 커뮤니티, 플러그인이 존재합니다. Spring Data JPA 같은 라이브러리를 통해 MySQL과의 매핑이 용이하고, 데이터베이스 접근 코드의 양을 줄여 생산 성을 높일 수 있습니다.

# 2. **Python 서버와 Java 서버간의 DB 통합 여부**:
#    - **단일 DB 사용**: 두 백엔드 서비스가 동일한 데이터베이스를 이용할 필요가 있는 공통의 데이터를 다루고 있다면, 한 개의 MySQL 데이터베이스를 공유하는 것이 좋습니다. 이렇게 하면 데이터 일관성을 유지하고, 데이터 중복을 피할 수 있습니다. Python 서버에서도 MySQL을 접근할 수 있도록 드라이버 설치가 필요합니다.     
#      - **설치 및 설정**:
#        1. `mysql-connector-python` 또는 `PyMySQL` 등의 라이브러리를 설치합니다. (예: `pip install mysql-connector-python`)
#        2. SQLAlchemy 같은 ORM을 사용하여 데이터베이스 조작을 좀 더 쉽게 할 수 있습니다.
#        3. 데이터베이스 연결 정보를 Flask 설정에 추가합니다.
#          ```python
#          app.config['MYSQL_DATABASE_USER'] = 'your_user'
#          app.config['MYSQL_DATABASE_PASSWORD'] = 'your_password'
#          app.config['MYSQL_DATABASE_DB'] = 'your_db'
#          app.config['MYSQL_DATABASE_HOST'] = 'your_host'
#          ```
#    - **Java 개발자와의 협업**:
#      - 데이터베이스 연결 정보와 스키마에 대한 공유가 중요합니다. 데이터 모형에 변화가 있을 때 서로 조율할 수 있도록 테이블 스키마에 대한 문서를 유지하는 것 이 좋습니다.
#      - 데이터베이스 접근에 필요한 계정 정보와 권한 설정 방법에 대해 공유가 필요합니다.

# 3. **유사도 계산을 통한 사용자 매칭 과정**:
#    - **단계 1: 데이터 전처리**
#      - 사용자의 서술형 데이터를 수집하고, 필요한 전처리를 수행합니다. 여기에는 텍스트 클리닝, 불용어 제거, 표제어 추출 등이 포함됩니다.
#    - **단계 2: 텍스트 임베딩**
#      - 자연어 처리(NLP) 모델을 사용하여 텍스트 데이터를 벡터로 변환합니다. BERT, GPT, Sentence-BERT와 같은 다양한 임베딩 기법을 사용할 수 있습니다. 이 단계 에서는 각 사용자 응답을 고정된 차원의 벡터로 변환하게 됩니다.
#    - **단계 3: 유사도 계산**
#      - 코사인 유사도 또는 유클리디안 거리 등의 방법을 활용하여 임베딩된 벡터 간의 유사도를 계산합니다. 두 벡터 간의 코사인 유사도가 높을수록 두 사용자의 응 답이 유사하다고 말할 수 있습니다.
#    - **단계 4: 매칭 알고리즘 구현**
#      - 유사도 점수를 기반으로 사용자를 매칭합니다. 특정 임계값을 넘어가는 유사도 점수를 가진 사용자들끼리 쌍을 이루거나, 상위 N명의 유사한 사용자 그룹을 형 성하는 방법으로 구현할 수 있습니다.
#    - **단계 5: 결과 피드백 및 반복**
#      - 매칭 결과를 평가하고, 필요하면 알고리즘을 조정하거나 데이터 전처리 방법을 개선하여 반복 학습을 통해 성능을 향상시킵니다.

# 이외에도 추가적인 질문이 있으시면 언제든지 연락주시기 바랍니다. 프로젝트가 성공적으로 진행되기를 기원하며, 도움될만한 자료나 조언이 필요하면 편하게 문의하세요.

# 감사합니다.