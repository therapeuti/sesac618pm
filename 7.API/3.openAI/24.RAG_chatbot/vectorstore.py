from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.vectorstores.utils import filter_complex_metadata
import os
from chatbot import answer_question


VECTOR_DB = './chroma_db'
COLLECTION_NAME = 'my_collection' # 일단 콜렉션 이름 다 통일...?
store = None
# _store = None 다른데서 함부로 가져가서 변경해서 사용하지 못 하게 언더바사용
load_dotenv()

def get_store():
    return store

def initialize_vector_db():
    global store
    # 디렉토리 생성
    if not os.path.exists(VECTOR_DB):
        os.makedirs(VECTOR_DB, exist_ok=True)
    # 이전 db가 있으면 로딩
    store = Chroma(collection_name=COLLECTION_NAME, embedding_function=OpenAIEmbeddings(), persist_directory=VECTOR_DB)
    return True    


def create_vector_db(file_path):
    global store
    # 벡터db 생성
    print(file_path)
    # 1. 파일 가져온다
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    print('업로드된 문서 내용: ', pages)

    for doc in pages:
        doc.metadata['source'] = os.path.basename(file_path)


    # 2. 문서 분할
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator="\n\n",
        chunk_size=100,
        chunk_overlap=20
    )
    texts = text_splitter.split_documents(pages)

    # 3. 임베딩
    embeddings = OpenAIEmbeddings()
    
    if store:
        store.add_documents(texts)
        print('벡터DB에 업로드 문서 내용 추가')
    else:
        store = Chroma.from_documents(texts, embeddings, collection_name=COLLECTION_NAME, persist_directory=VECTOR_DB)
        print('벡터 DB 생성')

    return store





def delete_file_from_vsstore(filename):
    # NoSQL 기반의 DB에서 자료 삭제하는것과 동일함 (예, mongodb)

    store._collection.delete(where={'source': filename})

    
    # 백터DB가 persist 옵션이 켜져 있으면? 저장..
    if hasattr(store, "persist"):
        store.persist()