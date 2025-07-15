from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db') # 상대경로 정의. 기본 디렉토리는 instance라는 폴더를 만들어서 사용
# engine = create_engine('sqlite:////tmp/example.db') # 절대경로 정의 /tmp/example.db
# engine = create_engine('sqlite:///./example.db') # 절대경로 정의. 현재 디렉토리 ./ 내에 example.db

# 베이스 클래스를 마늗ㄹ어서 객체랑 DB랑 연결
Base = declarative_base()

class User(Base):
    __tablename__ = 'users' # 옵셔널. DB 테이블명을 내가 지정해 줄 수 있음. 지정하지 않으면 클래스명이 소문자로 테이블명이 됨
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# DB에게 테이블 생성하라고 시킴
Base.metadata.create_all(engine)

# 세션을 통해서 실제 DB와 CRUD를 시킴
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='Alice', age=30)
session.add(new_user)
session.commit()

# SELECT * FROM users;
users = session.query(User).all()
# print(users)
for user in users:
    print(user.id, user.name, user.age)