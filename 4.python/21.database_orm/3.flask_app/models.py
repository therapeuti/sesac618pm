from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy 초기화
db = SQLAlchemy()

# 사용자 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

    # 디버깅용...
    def __repr__(self):
        return f'출력 : <User {self.id}: {self.name}, {self.age}>'
    
    # 문자열로 출력...
    def __str__(self):
        return f'문자열 변환 : <User {self.id}: {self.name}, {self.age}>'
        

