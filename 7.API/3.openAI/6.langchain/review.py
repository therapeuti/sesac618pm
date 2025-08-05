import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI # chat 모델 (QA모델)
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()



from langchain.schema import HumanMessage, SystemMessage, AIMessage

llm2 = ChatOpenAI(model='gpt-4o')
prompt = [
    SystemMessage(content='당신은 chat gpt 전문가입니다. chat gpt 사용에 관련한 사용자의 질문에 상세하고 자세하게 답변해주세요.'),
    HumanMessage(content='chat gpt api를 이용하여 서비스를 만드려고 하는데, chat gpt 모델들에 관해서 비교 설명해주고, api를 호출해서 사용할 때 각 모델의 이름을 어떻게 입력해야하는지 알려주세요.'),
]
result3 = llm2.invoke(prompt)
print(result3.content)


# (base) C:\Users\temnt\0.SESAC\sesac618pm_clean\7.API\3.openAI\6.langchain>python review.py
# ChatGPT API를 이용하여 서비스를 개발할 때, OpenAI의 모델들에 대한 이해가 중요합니다. ChatGPT는 여러 가지 모델 변형을 제공하며, 각 모델은 크기와 성능면에서  다릅니다. 여기서는 주로 사용되는 모델들에 대해 비교 설명하고, API 호출 시 사용할 모델 이름을 안내해드리겠습니다.

# ### 모델 비교

# 1. **GPT-3**:
#    - **Variations**: `ada`, `babbage`, `curie`, `davinci`
#    - **특징**:
#      - `ada`: 가장 빠르고 저렴하며, 간단한 작업에 적합합니다.
#      - `babbage`: 텍스트 분류와 같은 간단한 작업에 적절합니다.
#      - `curie`: 좀 더 복잡한 자연어 처리 작업에 유용합니다.
#      - `davinci`: 가장 강력하며, 창의적인 작업과 복잡한 질의응답 등에 적합합니다.

# 2. **GPT-3.5**:
#    - **Variations**: `gpt-3.5-turbo`
#    - **특징**:
#      - 강화된 성능을 제공하며, 특히 대화형 애플리케이션에 유리합니다. 성능과 비용 효율 사이의 균형을 잘 맞춥니다.

# 3. **GPT-4**:
#    - **Variations**: `gpt-4`, `gpt-4-turbo`
#    - **특징**:
#      - 기존의 GPT-3 모델들보다 더 진보된 성능을 자랑합니다. 복잡한 문제 해결과 고급 응용 분야에 적합합니다.
#      - `gpt-4-turbo`: 이는 `gpt-4`에 비해서 비용 효율적이며, 대부분의 경우에 비슷한 성능을 제공합니다.

# ### API 호출 시 모델 이름 입력

# 각 모델에 따라 API 호출 시 사용해야 할 모델 이름을 아래에 정리합니다.

# - **GPT-3**:
#   - `'text-ada-001'`
#   - `'text-babbage-001'`
#   - `'text-curie-001'`
#   - `'text-davinci-003'`

# - **GPT-3.5**:
#   - `'gpt-3.5-turbo'`

# - **GPT-4**:
#   - `'gpt-4'`
#   - `'gpt-4-turbo'`

# ### API 호출 예시

# ```python
# import openai

# openai.api_key = 'your-api-key'

# response = openai.Completion.create(
#     model="gpt-3.5-turbo",
#     prompt="ChatGPT API를 이용하여 어떻게 애플리케이션을 만들 수 있나요?",
#     max_tokens=150
# )

# print(response.choices[0].text.strip())
# ```

# 위 예시에서는 `gpt-3.5-turbo` 모델을 사용하여 ChatGPT API를 호출하였습니다. 사용 목적에 따라 적절한 모델을 선택해야 하며, 각 모델 이름은 OpenAI에서 공식적으로 제공하는 문서를 참고하시기 바랍니다. 이러한 모델들은 사용 패턴과 성능, 그리고 비용 효율성 측면에서 다르므로, 귀하의 서비스 요구사항에 맞는 올바른 모델을 선택하는 것이 중요합니다.
