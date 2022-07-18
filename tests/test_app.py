from flask_testing import TestCase
from flask import url_for
import app
from application import *
from application.models import *


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite3',
        SECRET_KEY='TEST_SECRET_KEY',
        DEBUG=True,
        WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
        # Create table schema
        db.create_all()
        # Create test objects
        test_user = User(name = "Test User", email = "testuser@live.it")
        test_post = Post(title="A testy vegan post", content="Testy stories and more", author="Test User", slug="test post", user=test_user)
        # save sample data to database
        db.session.add_all([test_user, test_post])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
#-----------------------------------------------------Testing models-----------------------------------------------------
    def test_User_model(self):
        db.create_all()
        user1 = User(name = "Bismillah", email = "bismillah@live.it")
        assert user1.email == "bismillah@live.it"
        assert f"{user1.__repr__()}" == 'User: Bismillah, bismillah@live.it'   
        assert self.assertEqual(User.query.count(), 2)

# ----------------------------------------------questions--------------------------------------------

    #do I have to have my GET and POST separate if they are checking the same asserIn?
    def test_UserForm_GET(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200) # 200 default
        self.assertIn(b'Welcome to our Gluten Free Flask website!', response.data) 

    def test_UserForm_POST(self):
        response = self.client.post(
            url_for('register'),
            #what is the connection between my user1 (Bismillah) for response from the website? Asking because we added this line together
            data = dict(name_box="Bismillah", email_box="bismillah@live.it"),
            follow_redirects=True   
        )
        # trying to assert that the website's title is present in the HTTP response's data but what is the use of data and dict?
        self.assertIn(b'Welcome to our Gluten Free Flask website!', response.data)  
# ---------------------------------------------------------------------------------------------------

    def test_UserFormUpdate_GET(self):
        response = self.client.get(url_for('update'))
        self.assertEqual(response.status_code, 200) # 200 default
        #asserting that the website's title is present in the HTTP response's data
        self.assertIn(b'Updating User', response.data) 

    def test_UserForm_POST(self):
        response = self.client.post(
            url_for('update'),
            data = dict(name_box="Bismillah", email_box="bismillah@live.it"),
            follow_redirects=True   
        )
        # asserts that the website's title is present in the HTTP response's data
        self.assertIn(b'Welcome to our Gluten Free Flask website!', response.data) 