from application import db, app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField 
from wtforms.validators import DataRequired, Length, Email 

class UserForm(FlaskForm):
    name_box = StringField("Enter your full name: ", validators=[DataRequired(), Length(min=3, max=80)])
    email_box= StringField("Email address here: ", validators=[DataRequired(), Email()])
    submit_button = SubmitField("Submit")

class UserFormUpdate(FlaskForm):
    name_box = StringField("Enter the new name: ", validators=[DataRequired(), Length(min=3, max=80)])
    email_box= StringField("Enter the new email address: ", validators=[DataRequired(), Email()])
    submit_button = SubmitField("Submit")

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(95), nullable=False)
    email = db.Column(db.String(180), unique=True , nullable=False)

    def __repr__(self):
        return f"User: {self.name}, {self.email}"

