""" this module takes care of the flask forms """
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class QuestionToTheBot(FlaskForm):
    """
    form for get user's question
    """

    message = StringField("message", validators=[DataRequired()])
    submit = SubmitField("Envoyer")
