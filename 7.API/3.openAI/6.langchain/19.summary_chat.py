from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda


load_dotenv()

template = ''
prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(template)
])

prompt =



