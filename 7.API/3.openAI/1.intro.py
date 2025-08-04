from dotenv import load_dotenv
import os
import requests
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

response = requests.post('https://api.openai.com/v1/chat/completions',
              json={
                  'model':'gpt-4o',
                #   'input':'잠자리에 들기 전 양 한 마리, 별빛 아래 풀밭에서 조용히 잠드는 내용의 짧은 동화를 작성해줘'
                'messages':[{'role':"user", "content":'잠자리에 들기 전에 양에 대한 스토리를 한 문장으로 말해줘.'}]
              },
              headers={
                  'Content-Type': 'application/json',
                  'Authorization': f'Bearer {OPENAI_API_KEY}'
              })

response_data = response.json()
print(response_data)

# print(response_data['output'][0]['content']['text'])


# 고등학교 1학년 영어 학습 능력을 평가하기 위한 4지선다형 객관식 문항 10개를 만들어줘.
#                         요청 사항:
#                         대상: 고등학교 1학년 학생
#                         과목: 영어
#                         영역: 어휘, 문법, 독해, 듣기(듣기 지문 제시) 영역을 모두 포함하여 출제해줘.
#                         난이도: 중학교 과정에서 고등학교 과정으로 넘어가는 학생들의 수준을 고려하여, 기본적인 어휘 및 문법 개념을 이해하고, 짧고 명확한 지문을 해석하는 능력을 평가하는 데 초점을 맞춰줘.
#                         문제 구성:
#                         문제당 4개의 선택지를 포함해야 하며, 정답은 한 개만 존재해야 합니다.
#                         각 문제에는 **정답 해설(rationale)**과 **힌트(hint)**를 추가해야 합니다.
#                         해설(rationale): 정답인 이유와 오답인 이유를 간결하게 설명해 줘.
#                         힌트(hint): 정답을 직접적으로 암시하지 않으면서 문제 해결에 도움이 되는 방향성을 제시해 줘.
#                         출제 내용:
#                         어휘/문법: 고등학교 필수 어휘, 문장의 5형식, 수의 일치, 시제 등 기초 문법 개념을 묻는 문제.
#                         독해: 일상생활, 교내 활동, 문화 등 친숙한 주제의 짧은 지문을 활용하여, 글의 요지, 목적, 세부 정보 등을 파악하는 문제.
#                         듣기: 고등학교 교과서 수준의 대화나 담화를 기반으로, 화자의 의도나 세부 내용을 파악하는 문제. (듣기 스크립트를 문제와 함께 제시해 줘)
#                         출력 형식: 문제, 선택지, 해설, 힌트를 명확히 구분하여 보기 좋게 작성해줘