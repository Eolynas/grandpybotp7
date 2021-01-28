# from app_flask.hello import app as flask_app
from unittest.mock import patch

from app import app as flask_app
from app import parser, api_google, wiki


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
        # TODO A FAIRE
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
        # assert parse_message == "openclassrooms"

        parse_message = parse_question.parser(messages_empty)
        # assert parse_message == []

        parse_message = parse_question.parser(messages_number)
        # assert parse_message == []
        #
        # parse_message = parser.parser(messages_speciaux[0])
        # assert parse_message == ["eddy"]
        # #
        # parse_message = parser.parser(messages_speciaux[1])
        # assert parse_message == ["bonjour"]

    def mock_api_google(self, search: str) -> dict:
        txt_input = "openclassrooms"
        request_no_found = {
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

        if search.lower() == txt_input.lower():
            return request_found
        elif search == "":
            return request_no_found
        else:
            return request_no_found

    @patch('api_google.ApiGoogle.get_address.requests.get')
    def test_get_api_google(self, mock_get):
        """
        # TODO A FAIRE
        :return:
        """
        request_no_found = {
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
        example_true_reponse_api = {
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
        example_false_reponse_api = {
            "results": [],
            "status": "ZERO_RESULTS"
        }


        question_parsed_1 = "Openclassrooms"
        question_parsed_2 = "sqsdqqdqsdqsdq"
        question_parsed_3 = ""

        mock_get.return_value.json.return_value = request_found

        init_apigoole = api_google.ApiGoogle()
        get_api_address = init_apigoole.get_address(question_parsed_1)
        print(get_api_address)
        assert get_api_address == example_true_reponse_api

        # get_api_address_2 = self.mock_api_google(question_parsed_2)
        # print(get_api_address_2)
        # assert get_api_address_2 == example_false_reponse_api
        #
        # get_api_address_3 = self.mock_api_google(question_parsed_3)
        # print(get_api_address_2)
        # assert get_api_address_2 == example_false_reponse_api

    # def mock_api_wiki(self, search: str) -> dict:
    #     """
    #
    #     :param search:
    #     :return:
    #     """
    #     request_found = {
    #         "ns": 0,
    #         "title": "Paris",
    #         "pageid": 681159,
    #         "size": 411931,
    #         "wordcount": 45357,
    #         "snippet": "significations, voir <span class=\"searchmatch\">Paris</span> (homonymie). « Ville Lumière » redirige ici. Ne pas confondre avec Ville de lumière ni la villa Lumière. <span class=\"searchmatch\">Paris</span> ([pa.ʁi]Écouter)",
    #         "timestamp": "2021-01-23T17:55:20Z"
    #     }
    #     request_no_found = {
    #         "batchcomplete": "",
    #         "query": {
    #             "searchinfo": {
    #                 "totalhits": 0
    #             },
    #             "search": []
    #         }
    #     }
    #     txt_input = "Paris"
    #
    #     if search.lower() == txt_input.lower():
    #         return request_found
    #     elif search == "":
    #         return request_no_found
    #     else:
    #         return request_no_found
    #
    # def test_get_api_wiki(self):
    #     """
    #     # TODO A FAIRE
    #     :return:
    #     """
    #
    #     example_get = {
    #             "ns": 0,
    #             "title": "Paris",
    #             "pageid": 681159,
    #             "size": 411931,
    #             "wordcount": 45357,
    #             "snippet": "significations, voir <span class=\"searchmatch\">Paris</span> (homonymie). « Ville Lumière » redirige ici. Ne pas confondre avec Ville de lumière ni la villa Lumière. <span class=\"searchmatch\">Paris</span> ([pa.ʁi]Écouter)",
    #             "timestamp": "2021-01-23T17:55:20Z"
    #         }
    #     example_get_no_found = {
    #         "batchcomplete": "",
    #         "query": {
    #             "searchinfo": {
    #                 "totalhits": 0
    #             },
    #             "search": []
    #         }
    #     }
    #     question_parsed_1 = "Paris"
    #     question_parsed_2 = "sqsdqqdqsdqsdq"
    #     question_parsed_3 = ""
    #
    #     get_test = self.mock_api_wiki(question_parsed_1)
    #     assert get_test == example_get
    #
    #     get_test_no_found = self.mock_api_wiki(question_parsed_2)
    #     assert get_test_no_found == example_get_no_found
    #
    #     get_test_no_found = self.mock_api_wiki(question_parsed_3)
    #     assert get_test_no_found == example_get_no_found
