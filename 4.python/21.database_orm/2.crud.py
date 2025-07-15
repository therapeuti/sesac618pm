from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///users.db')

Base = declarative_base()

# 테이블 설계 - 객체 설계
# 사용자 모델을 정의
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)



# -------- CRUD 함수 만들기 ------------------------------------------------
# 좀 더 모던한 파이써닉한 형태의 함수로 짜려면
def create_user(session, name: str, age: int) -> User:
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
    return new_user


def get_users(session) -> list[User]:
    # 아무 인자도 안 받고, 사용자 리스트 리턴하기
    users = session.query(User).all()
    return users

def get_user_by_id(session, user_id: int) -> User | None:
    # 사용자 id 받아서 사용자 반환하기
    # user = session.query(User).where(User.id == user_id).first()
    # user = session.query(User).filter(User.id == user_id).first()
    # user = session.query(User).filter_by(User.id == user_id).first()
    user = session.get(User, user_id)
    return user

def update_user_age(session ,user_id: int, new_age: int) -> bool:
     # 사용자 아이디, 나이 받아서 나이 업데이트 하기
     # 객체에 값만 설정하면 자동으로 쓰임. 물론 커밋해야함.
    # user = session.query(User).where(User.id == user_id).first()
    user = session.get(User, user_id)
    if not user:
        return False
    user.age = new_age
    session.commit()
    return True

def delete_user_id(session, user_id: int) -> bool:
     # 사용자 삭제하고 성공시 True 반환
    user = session.get(User, user_id)
    if not user:
        return False
    session.delete(user)
    session.commit()
    return True

def delete_user_name(session, user_name: str) -> int:
     # 사용자 삭제하고 성공시 삭제한 사용자 수를 반환
    users = session.query(User).filter_by(name=user_name).all()
    if not users:
        return 0
    for u in users:
        session.delete(u)
    session.commit()
    return len(users)



if __name__=='__main__':
     Session = sessionmaker(bind=engine, expire_on_commit=False)
     with Session() as session:
        alice = create_user(session, 'Alice', 30)
        bob = create_user(session, 'Bob', 34)
        print(f'추가된 사용자 ID: {alice.id}, {bob.id}')
        
          # 사용자 조회
        user1 = get_user_by_id(session, alice.id)
        print(user1)
        print(f'조회한 사용자 정보: {user1.name}, {user1.age}')
          
        user2 = get_user_by_id(session, bob.id)
        print(user2)
        print(f'조회한 사용자 정보: {user2.name}, {user2.age}')

        # 정보 수정
        update_alice = update_user_age(session, alice.id, 29) 
        print(f'업데이트 성공 여부: {update_alice}')

        # 사용자 모두 조회
        users = get_users(session)
        for u in users:
            print(f'아이디: {u.id}, 이름: {u.name}, 나이: {u.age}')

        # 사용자 삭제
        delete_alice = delete_user_id(session, alice.id)
        print(f'사용자 삭제 확인: {delete_alice}')


        print(f'삭제된 사용자 수: {delete_user_name(session, 'Bob')}')

        # 최종 사용자 목록
        users = get_users(session)
        for u in users:
            print(f'아이디: {u.id}, 이름: {u.name}, 나이: {u.age}')