import openai
from dotenv import load_dotenv
import os
load_dotenv()

openai_api_key = os.getenv('OPEN_API_KEY')
openai.api_key = openai_api_key

# openai.ChatCompletion으로 시작하는 것은 구버전 api. 더이상 사용안 됨.
# response = openai.ChatCompletion.create(
#     model='gpt-3.5-turbo',
#     messages= [
#         {'role': 'user',
#          }
#     ]
# )

client = openai.OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages = [
        {'role':'user', 'content': 'api 처음 사용할 때 주는 무료 크레딧 있는지 확인하는 방법 간단하게 알려줘'}
    ]
)

print(response.choices[0].message.content)