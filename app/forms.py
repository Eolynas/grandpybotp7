from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ChoseProjectForm(FlaskForm):
    name_project = StringField('name_project', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class QuestionToTheBot(FlaskForm):
    message = StringField('message', validators=[DataRequired()])
    submit = SubmitField('Envoyer')
