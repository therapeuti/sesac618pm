from app import app
from models import db, User

app = app()

with app.app_context(): # 위 flask 앱이 초기화 되면
    db.drop_all()
    db.create_all()

    db.session.add(User(name="Alice", age=30))
    db.session.add(User(name="Bob", age=35))
    db.session.add(User(name="Charlie", age=40))
    db.session.commit

    for u in User.query.all():
        print(u.id, u.name, u.age)