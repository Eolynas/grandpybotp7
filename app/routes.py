import os
from datetime import datetime

from flask import render_template, redirect, url_for, jsonify, send_from_directory

from app import app, forms, parser, api_google, function, wiki

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
                               'favicon.ico', mimetype='image/png')

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
    return render_template('index.html', form=form)


@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    name_project = 'GrandPy ChatBot'
    question = forms.QuestionToTheBot()
    posts = [
        {
            'user': 'GrandPy',
            'message': 'Bonjour est bienvenue sur mon chatbot',
            'date': '22/12/2020 17:13'
        }

    ]

    return render_template('chatbot.html', name_project=name_project, posts=posts, form=question)


@app.route('/message', methods=['POST'])
def message():
    """

    :return:
    """
    question = forms.QuestionToTheBot()
    message_question = question.data['message']
    # TRAITEMENT DU FORM

    # PARSER
    parse = parser.Parser()
    parse_question = parse.parser(string=message_question)

    cnx_api = api_google.ApiGoogle()

    get_api = cnx_api.get_address(parse_question)

    # WIKI API
    if not get_api["status"]:
        return jsonify(data=get_api)

    get_api_wiki = wiki.Wiki().get_wiki_address(parse_question)
    get_api['WIKI'] = get_api_wiki

    return jsonify(data=get_api)
    # dict_get_api = {}
    # date_now = datetime.now()
    # date_now = date_now.strftime("%d/%m/%Y %H:%M")
    # if get_api["status"] == "ZERO_RESULTS":
    #     message_no_found = f"Désolé mon petit, je ne trouve pas l'adresse de {parse_question}"
    #     dict_message = {'data': message_no_found, 'date': date_now}
    #     dict_get_api['message'] = dict_message
    #     dict_get_api['status'] = False
    #
    #     return jsonify(data=dict_get_api)
    #
    # else:
    #     print(cnx_api)
    #     message_return = f" Voici l'adresse de {parse_question}: {get_api['results'][0]['formatted_address']}"
    #     dict_message = {'data': message_return, 'date': date_now}
    #     dict_get_api['message'] = dict_message
    #     dict_get_api['status'] = True
    #     dict_get_api['address'] = get_api["results"][0]["formatted_address"]
    #     dict_get_api['location'] = get_api["results"][0]["geometry"]["location"]
    #
    #     # REQUEST API MEDIAWIKI
    #     init_wiki = wiki.Wiki()
    #     get_info_wiki = init_wiki.get_wiki_address(parse_question)
    #     dict_get_api['wiki'] = get_info_wiki
    #     dict_get_api['wiki_grandpy'] = f"Voici une petite histoire sur {parse_question}"
    #
    #
    #     # REDIRECTION VERS CHATBOT
    #     return jsonify(data=dict_get_api)

