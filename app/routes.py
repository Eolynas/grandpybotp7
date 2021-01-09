from datetime import datetime

from app import app, forms
from flask import render_template, redirect, url_for, flash, request, jsonify


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    Load home page
    :return:
    """
    title = 'GrandPy'
    form = forms.ChoseProjectForm()
    name_project = form.data['name_project']
    if form.validate_on_submit():
        print(name_project)
        if str(name_project) == "chatbot":
            return redirect(url_for('chatbot'), code=307)
            # return 'Submit Form'
    return render_template('index.html', form=form)


@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    name_project = 'GrandPy ChatBot'
    # form = forms.ChoseProjectForm()
    question = forms.QuestionToTheBot()
    # message_question = question.data['message']
    posts = [
        {
            'user': 'GrandPy',
            'message': 'Bonjour est bienvenue sur mon chatbot',
            'date': '22/12/2020 17:13'
        },
        {
            'user': 'Eddy',
            'message': 'Bonjour vous allez bien',
            'date': '22/12/2020 17:14'
        }

    ]
    # if question.validate_on_submit():
    #     print(message_question)
    #     new_post = {
    #         'user': 'Eddy',
    #         'message': message_question,
    #         'date': datetime.now()
    #     }
    #     # posts.append(new_post)
    #     # return render_template('chatbot.html', name_project=name_project, posts=posts, form=question)
    #     return redirect(url_for('message'), code=307)

    return render_template('chatbot.html', name_project=name_project, posts=posts, form=question)
    # return render_template('chattest.html', name_project=form.data['name_project'])


@app.route('/message', methods=['POST'])
def message():
    """

    :return:
    """
    question = forms.QuestionToTheBot()
    message_question = question.data['message']
    # TRAITEMENT DU FORM
    # print(message_question)

    # RECUPERATION DE LA REPONSE VIA L'API GOOGLE

    new_post = [{
        'user': 'Eddy',
        'message': message_question,
        'date': datetime.now()
        },
        {
        'user': 'GrandPyBOT',
        'message': message_question,
        'date': datetime.now()
        }
    ]

    # REDIRECTION VERS CHATBOT
    return jsonify(data=new_post)

