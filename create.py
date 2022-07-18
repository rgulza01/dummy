import email
from application import db
from application.models import *

db.drop_all()
db.create_all()

# user1 =User(name = "Bismillah", email = "bismillah@live.it")
# user2 =User(name = "Bambi", email = "bambi@outlook.com")
# user3 =User(name = "Shakalaka", email = "shakalaka@gmail.com")
# db.session.add_all([user1, user2, user3])

# ----------I can't do one to many with the backref like I am used to anymore--------
                                                                                                            #backref=
# post2=Post(title="An utterly vegan post", content="Vegan stories and more", author="budi", slug="budi post", user=?)
# db.session.add(post2)
# db.session.commit()


