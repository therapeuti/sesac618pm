from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from vectorstore import get_store
import json
import yaml

PROMPT_JSON_FILE = 'prompts.json'
PROMPT_YAML_FILE = 'prompts.yaml'


llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.2)

def answer_question(question):
    embeddings=OpenAIEmbeddings()
    # store = Chroma(collection_name=COLLECTION_NAME, embedding_function=embeddings, persist_directory=VECTOR_DB)
    store = get_store()

    retriever = store.as_retriever(search_kwargs={'k':5}) # retriever 객체

    # print('추출된 문서 내용이 아니라 객체', retriever)
    # 검색된 문서 내용
    docs = retriever.invoke(question)
    print('검색된 문서 내용 : ', docs)
    for i, doc in enumerate(docs, 1):
        print(f'문서번호<{i}> \n  {doc}')
    
    context = '\n\n'.join([doc.page_content for doc in docs])



    # llm에 질문

    # 체인 호출, 질문
    #

    response = chain.invoke({'question':question, 'content':context})
    print('Q', question)
    print('A', response)
    return response



def _load_prompts_from_json(filepath): # 내부에서만 쓰는 로컬함수...
    with open(filepath, 'r', encoding='utf-8') as f:
        # data = json.load(f)

    # result = {}
    # for name, p in data.items():
    #     template = p['template']
    #     result[name] = ChatPromptTemplate.from_template(template)
    # return result

        data = yaml.safe_load(f) # yaml 문법에 escaping 문자열로 나쁜 짓 못하게
    return {
        name: ChatPromptTemplate.from_template(p['template'])
        for name, p in data.items()
    }

def initialize_llm():
    global prompt, llm, chain

    # prompt = _load_prompts_from_json(PROMPT_JSON_FILE)['default_prompt']
    prompt = _load_prompts_from_json(PROMPT_YAML_FILE)['default_prompt']
    print('프롬프트 로딩 : ', prompt)

    chain = prompt | chain | StrOutputParser()