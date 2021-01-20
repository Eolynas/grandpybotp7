from datetime import datetime

from flask import render_template, redirect, url_for, jsonify

from app import app, forms, parser, api_google, function


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
        }

    ]

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

    # PARSER
    # init_parser = parser.Parser
    parse_question = parser.parser(string=message_question)

    cnx_api = api_google.ApiGoogle()
    get_api = cnx_api.get_address(parse_question)
    dict_get_api = {}
    date_now = function.get_date_now()
    if get_api["status"] == "ZERO_RESULTS":
        message_no_found = f"Désolé mon petit, je ne trouve pas cette adresse de {parse_question}"
        dict_message = {'data': message_no_found, 'date': date_now}
        dict_get_api['message'] = dict_message
        dict_get_api['status'] = False

        return jsonify(data=dict_get_api)

    else:
        result_address = get_api["results"][0]["formatted_address"]
        print(cnx_api)
        message_return = f" Voici l'adresse de {parse_question}: {get_api['results'][0]['formatted_address']}"
        dict_message = {'data': message_return, 'date': date_now}
        dict_get_api['message'] = dict_message
        dict_get_api['status'] = True
        dict_get_api['address'] = get_api["results"][0]["formatted_address"]
        dict_get_api['location'] = get_api["results"][0]["geometry"]["location"]


        # REDIRECTION VERS CHATBOT
        return jsonify(data=dict_get_api)
    # return redirect(url_for('chatbot'), code=307)


"""
{
    "results": [
        {
            "address_components": [
                {
                    "long_name": "10",
                    "short_name": "10",
                    "types": [
                        "street_number"
                    ]
                },
                {
                    "long_name": "Quai de la Charente",
                    "short_name": "Quai de la Charente",
                    "types": [
                        "route"
                    ]
                },
                {
                    "long_name": "Paris",
                    "short_name": "Paris",
                    "types": [
                        "locality",
                        "political"
                    ]
                },
                {
                    "long_name": "Département de Paris",
                    "short_name": "Département de Paris",
                    "types": [
                        "administrative_area_level_2",
                        "political"
                    ]
                },
                {
                    "long_name": "Île-de-France",
                    "short_name": "IDF",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                },
                {
                    "long_name": "France",
                    "short_name": "FR",
                    "types": [
                        "country",
                        "political"
                    ]
                },
                {
                    "long_name": "75019",
                    "short_name": "75019",
                    "types": [
                        "postal_code"
                    ]
                }
            ],
            "formatted_address": "10 Quai de la Charente, 75019 Paris, France",
            "geometry": {
                "location": {
                    "lat": 48.8975156,
                    "lng": 2.3833993
                },
                "location_type": "ROOFTOP",
                "viewport": {
                    "northeast": {
                        "lat": 48.8988645802915,
                        "lng": 2.384748280291502
                    },
                    "southwest": {
                        "lat": 48.8961666197085,
                        "lng": 2.382050319708498
                    }
                }
            },
            "place_id": "ChIJIZX8lhRu5kcRGwYk8Ce3Vc8",
            "plus_code": {
                "compound_code": "V9XM+29 Paris, France",
                "global_code": "8FW4V9XM+29"
            },
            "types": [
                "establishment",
                "point_of_interest"
            ]
        }
    ],
    "status": "OK"
}
"""
