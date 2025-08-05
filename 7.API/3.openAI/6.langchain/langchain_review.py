# 요약, 번역, 메일 chat 모델로 구현
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# 프롬프트
template = '다음 내용을 요약해줘.{summary}'
prompt = PromptTemplate(input_variables=['summary'], template=template)
# 모델
llm = ChatOpenAI()
print(llm)
chain = prompt | llm

input_text = {'summary':'''
- [ ]  사용자 정보에 따라 프롬프트 변경되는 부분에 랭체인 프롬프트 템플릿 적용하기
- [ ]  멘토 이상형 분석 프롬프트 설계
- [x]  클로드 코드로 데이터 및 db 생성 가능한지 테스트 해보기
- [ ]  하이퍼 파라미터 조정. 문제 정확성과 일관성 높이기 위함. temperature 낮추기.
- [ ]  알고리즘 매칭에 사용된 데이터는 걍 내가 알아서 다 만든다.. 치고… 이왕 만든거 db에 넣어두는게 좋을 것 같은데..  이 경우, csv나 sqlite로 넘겨주면 알아서 mysql로 넣을 수 잇음?

회의 때 할 얘기
1. 오늘까지 한 작업 내용 공유
    1. llm 각 웹사이트에서 테스트 한 결과 chat gpt api 사용아 가장 나은 것 같아서 그걸로 결정했고, 선불 결제로 결제한 만큼한 api 사용할 수 있어서 일단 오늘 10달러 결제했음.
    2. 주말에 할루시네이션 줄이기 위한 rag 시스템 구축 가능여부도 알아봤는데, 가능은 한데 굳이 할 필요는 없을 것 같음. chat gpt 좋은 모델 쓰고, 웹 검색 가능한 모델을 쓰는 방식도 사용할 수 있고, 프롬프트를 구체적으로 입력하면 할루시네이션 줄일 수 있어서 그 방향으로 진행.
    3. flask 서버 구축해서 각 엔드포인트 설계.
    4. chat gpt api 불러서 응답 받아서 전달하는 로직 대부분 설계 해놨는데, 프롬프트가 사용자 정보에 따라 조금씩 바뀔 예정이라 그 부분 간편하게 진행하기 위해 랭체인 도입하는 방식으로 수정 들어갈 예정.
    5. 각각의 경우에 프롬프트 어떻게 들어갈건지 구상해놨고, 하이퍼파라미터랑 프롬프트 조금씩 바꿔가면서 chat gpt api로 테스트하면서 확정.
    6. 여기까지 7일까지 진행. 
    7. 그리고 오늘 더미 데이터 생성 테스트 했는데, 클로드 코드가 sqlite db까지 잘 만들어주는 것 확인했고, 클로드 코드로 좀 더 많은 데이터 생성해서 매칭 알고리즘 만드는데 사용할 것.
    8. 알고리즘 만들고, 해당 알고리즘 돌리는 엔드포인트 설계하는 부분은 빠르면 토요일 늦으면 일요일까지 완성할 예정.
    9. 알고리즘 계산 시.. db에 직접 접속? 아니면 자바 서버 통해서?
    10. CORS 설정 필요 자바는 8080, 프론트는 3000
    11. 알고리즘 계산 돌리는 게, 누군가가 레벨테스트 하고, 이상형 답변 입력했을 때 매칭하러 가기가 뜨기 때문에 그 때에도 계산 돌린 후에 매칭 결과 출력되는 방식으로 진행되어야 함.
    

1. chat gpt 사용하는 부분
    1. 멘티, 멘토의 레벨테스트 문제 요청
    2. 멘티, 멘토의 레벨테스트 결과 분석 요청
    3. 멘티, 멘토의 이상형 답변에 대한 키워드 도출 요청

1. 멘티, 멘토 알고리즘 설계
2. 멘티, 멘토 정보 토대로 설계된 알고리즘 돌려서 db에 저장하는 엔드포인트 및 로직
    1. 내가 직접 db에서 정보 가져와? 아님 또 자바 서버에 요청을 해?


멘토링 질문:
- chat gpt api 사용시 어떤 모델을 사용하는게 할루시네이션을 줄이고 정확한 문제를 잘 생성해줄 수 있을지.
- 웹 검색 등 tool 사용하는 모델들… 어떻게 사용해야하는지…
- 프롬프트 어떻게 작성하는게 좋을지
- 백엔드 설계.
- 지금 프론트-자바-파이썬  형태
- 나중에 매칭기능도 파이썬에서 담당을 하게 되는데, 매칭 기능시 DB에서 정보를 가져와서 매칭 알고리즘을 돌려야하는데, 이때도 자바를 통해서 db 정보를 가져오는게 나을지, 아니면 직접 DB에서 정보 가져오도록 설계하는게 나을지…
- CORS 설정 필요?


단원별.. 점수화… 각 단원을.. 7차원 벡터로….유사도 찾기…
의미 유사도….
한국어.. BM42 llm 기반..  스플레이드 모델.. SPLADE
https://github.com/qdrant/fastembed
bm25????
bm42 → 같은 단어에 대해서 같은 숫자로 표현…. 그거 워드임베딩이니까…. 그 숫자들을 키워드로 취급해서 벡터로 사용.
openai 임베딩 모델로 사용자 답변 넣어서…. 벡터들 가지고 numpy나 faiss 사용하거나 해서 코사인 유사ㅣ도 계산….
형태소분석기 사용방식…. 고려….
키워드 뽑아달라고….키워드 가지고 임베딩해서 유사도 계산..
시스템화…. → 엘라스틱 서치……'''}


response = chain.invoke(input_text)
print(response)


# content='- 랭체인 프롬프트 템플릿을 사용자 정보에 따라 변경할 예정\n- 클로드 코드로 데이터 및 DB 생성이 가능한지 테스트를 진행함\n- 멘토 이상형 분석 프롬프 트 설계와 하이퍼파라미터 조정 계획을 하였음\n- 알고리즘 매칭 데이터를 만들기 위해 클로드 코드로 더미 데이터를 생성하고, 이에 대한 매칭 알고리즘 설계를 할 예정\n- 멘티와 멘토 정보를 토대로 설계된 알고리즘을 돌려서 DB에 저장하는 엔드포인트 및 로직에 대한 논의와 CORS 설정에 대한 검토가 필요함.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 233, 'prompt_tokens': 1800, 'total_tokens': 2033, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-C1DDSfbYGndyW7kVcjrdFhedHZVXQ', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='run--007cdd28-e7ac-498a-b202-692b1c06b979-0' usage_metadata={'input_tokens': 1800, 'output_tokens': 233, 'total_tokens': 2033, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}