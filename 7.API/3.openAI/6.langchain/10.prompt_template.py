from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_env
load_env()

template = 'You are a naming consultant. Suggest a name for a company that makes {product}'

prompt = PromptTemplate(
    input_variables=['product'],
    template=template
)

filled_prompt = prompt.format(product='icecream')
print(filled_prompt)

filled_prompt = prompt.format(product='cookie')
print(filled_prompt)

filled_prompt = prompt.format(product='smartphone')
print(filled_prompt)

test_products = ['mobile games', 'robot toys', 'electrical goods', 'programming language education']

llm = ChatOpenAI()
for product in test_products:
    result = prompt.format(product=product)
    print(f'[{product}] : {result}')

    # 이렇게 만들어진 프롬프트를 다시 llm.invoke로 호출
    response = llm.invoke(result).content.strip()
    print(response)
