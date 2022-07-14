import email
from application import db
from application.models import *

#db.drop_all()
db.create_all()

user1 =User(name = "Bismillah", email = "bismillah@live.it")
user2 =User(name = "Bambi", email = "bambi@outlook.com")
user3 =User(name = "Shakalaka", email = "shakalaka@gmail.com")

db.session.add_all([user1, user2, user3])
db.session.commit()

#-----------------------------------------queries-----------------------------------------

