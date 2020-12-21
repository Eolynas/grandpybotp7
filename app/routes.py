from app import app, forms
from flask import render_template, redirect, url_for, flash, request


@app.route('/')
@app.route('/index')
def index():
    """
    Load home page
    :return:
    """
    title = 'GrandPy'
    # form = forms.ChoseProjectForm()
    # name_project = form.data['name_project']
    # if form.validate_on_submit():
    #     print(name_project)
    #     if len(name_project) > 0:
    #         return redirect(url_for('chatbot'), code=307)
    #         # return 'Submit Form'
    return render_template('index.html')


@app.route('/chatbot')
def chatbot():
    name_project = 'GrandPy ChatBot'
    return render_template('chatbot.html', name_project=name_project)

