""" this module takes care of the flask routes """
from datetime import datetime
import os

from flask import render_template, jsonify

from app import app, forms, parser, api_google, wiki


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    """
    Load home page
    """
    return render_template(
        "index.html", key_api_google=os.environ.get("key_api_google")
    )


@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():
    """
    route for chatbot
    """
    name_project = "GrandPy ChatBot"
    question = forms.QuestionToTheBot()
    date_now = datetime.now()
    date_now = date_now.strftime("%d/%m/%Y %H:%M")
    posts = [
        {
            "user": "GrandPy",
            "message": "Bonjour est bienvenue sur mon chatbot",
            "date": date_now,
        }
    ]

    return render_template(
        "chatbot.html",
        name_project=name_project,
        posts=posts,
        form=question,
        key_api_google=os.environ.get("key_api_google"),
    )


@app.route("/message", methods=["POST"])
def message():
    """
    route to process messages
    """
    question = forms.QuestionToTheBot()
    message_question = question.data["message"]
    parse = parser.Parser()
    parse_question = parse.parser(string=message_question)

    cnx_api = api_google.ApiGoogle()

    get_api = cnx_api.get_address(parse_question)

    # WIKI API
    if not get_api["status"]:
        return jsonify(data=get_api)

    get_api_wiki = wiki.Wiki().get_wiki_address(parse_question)
    get_api["WIKI"] = get_api_wiki

    return jsonify(data=get_api)
