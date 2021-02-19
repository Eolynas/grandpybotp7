# from app_flask.hello import app as flask_app
from unittest.mock import patch, MagicMock

from app import app as flask_app
from app import parser, api_google, wiki
import os

flask_app.config['SECRET_KEY'] = "grandpy"


class TestFlaskApp:
    """
    Class for testing Flask
    """
    app = flask_app
    client = app.test_client()

    # Méthode exécutée avant chaque test
    def test_route_index(self):
        """
        test status get for index page
        """
        res = self.client.get('/')
        assert res.status_code == 200

    def test_route_chatbot(self):
        """
        test status get for index page
        """
        res = self.client.get('/chatbot')
        assert res.status_code == 200

    def test_parser(self):
        """
        test parser methode
        :return:
        """
        messages = ["Bonjour, connait tu l'adresse d'OpenClassRooms", 'OpenClassRooms']
        messages_empty = ''
        messages_number = '212484'
        messages_speciaux = ["(--èè_--è:; Eddy", 'BONJOUR é&&']
        parse_question = parser.Parser()
        # print(parse_question)
        parse_message = parse_question.parser("Bonjour, connait tu l'adresse d'OpenClassRooms")
        assert parse_message == "OpenClassRooms"

        parse_message = parse_question.parser(messages[1])
        assert parse_message == "OpenClassRooms"

        parse_message = parse_question.parser(messages_empty)
        assert parse_message == ""

        # parse_message = parse_question.parser(messages_number)
        # assert messages_number == ""

    @patch("app.api_google.requests")
    def test_get_api_google(self, mock_get):
        """
        test request get api google
        :return:
        """
        request_not_found = {
            "results": [],
            "status": "ZERO_RESULTS"
        }
        request_found = {
            "results": [
                {
                    "formatted_address": "10 Quai de la Charente, 75019 Paris, France",
                    "geometry": {
                        "location": {
                            "lat": 48.8975156,
                            "lng": 2.3833993
                        },
                    },
                },
            ],
            "status": "OK"
        }


        question_parsed_1 = "Openclassrooms"
        question_parsed_2 = "sqsdqqdqsdqsdq"
        question_parsed_3 = ""

        # mock_get.return_value.json.return_value = request_found
        mock_get.get = MagicMock()
        mock_get.get.return_value.json.return_value = request_found

        init_apigoole = api_google.ApiGoogle()
        get_api_address = init_apigoole.get_address(question_parsed_1)
        # print(get_api_address)
        assert get_api_address['status'] == True
        assert "Openclassrooms" in get_api_address['message']['data']

        mock_get.get.return_value.json.return_value = request_not_found
        get_api_address_not_found = init_apigoole.get_address(question_parsed_2)
        assert get_api_address_not_found['status'] == False

        get_api_address_empty = init_apigoole.get_address(question_parsed_3)
        assert get_api_address_empty['status'] == False

    @patch("app.wiki")
    def test_get_id_api_wiki(self, mock_get):
        """
        # TODO A FAIRE
        :return:
        """

        example_get = {
                "ns": 0,
                "title": "Paris",
                "pageid": 681159,
                "size": 411931,
                "wordcount": 45357,
                "snippet": "significations, voir <span class=\"searchmatch\">Paris</span> (homonymie). « Ville Lumière » redirige ici. Ne pas confondre avec Ville de lumière ni la villa Lumière. <span class=\"searchmatch\">Paris</span> ([pa.ʁi]Écouter)",
                "timestamp": "2021-01-23T17:55:20Z"
            }
        example_get_no_found = {
            "batchcomplete": "",
            "query": {
                "searchinfo": {
                    "totalhits": 0
                },
                "search": []
            }
        }
        question_parsed_1 = "Paris"
        question_parsed_2 = "sqsdqqdqsdqsdq"
        question_parsed_3 = ""

        mock_get.requests.get = MagicMock()
        mock_get.requests.get.return_value.json.return_value = example_get

        init_apiwiki = wiki.Wiki()
        get_api_address = init_apiwiki._get_wiki_id_page(question_parsed_1)
        # print(get_api_address)
        assert get_api_address == 681159

    @patch("app.wiki")
    def test_get_api_wiki_by_id(self, mock_get):
        """
        # TODO A FAIRE
        :return:
        """

        example_get = {
            "ns": 0,
            "title": "Paris",
            "pageid": 681159,
            "size": 411931,
            "wordcount": 45357,
            "snippet": "significations, voir <span class=\"searchmatch\">Paris</span> (homonymie). « Ville Lumière » redirige ici. Ne pas confondre avec Ville de lumière ni la villa Lumière. <span class=\"searchmatch\">Paris</span> ([pa.ʁi]Écouter)",
            "timestamp": "2021-01-23T17:55:20Z"
        }
        example_get_no_found = {
            "batchcomplete": "",
            "query": {
                "searchinfo": {
                    "totalhits": 0
                },
                "search": []
            }
        }
        question_parsed_1 = "Paris"
        question_parsed_2 = "sqsdqqdqsdqsdq"
        question_parsed_3 = ""

        mock_get.requests.get = MagicMock()
        mock_get.requests.get.return_value.json.return_value = example_get

        with patch.object(wiki.Wiki, '_get_wiki_id_page', return_value=681159) as mock_method:
            init_apiwiki = wiki.Wiki()
            get_api_address = init_apiwiki.get_wiki_address(question_parsed_1)
            # print(get_api_address)
            assert "Paris ([pa.ʁi]) est la commune la plus peuplée et la capitale de la France" in get_api_address
