# from app_flask.hello import app as flask_app
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

    def test_get_api_google(self):
        """
        # TODO A FAIRE
        :return:
        """
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

        get_api_address = self.mock_api_google(question_parsed_1)
        print(get_api_address)
        assert get_api_address == example_true_reponse_api

        get_api_address_2 = self.mock_api_google(question_parsed_2)
        print(get_api_address_2)
        assert get_api_address_2 == example_false_reponse_api

        get_api_address_3 = self.mock_api_google(question_parsed_3)
        print(get_api_address_2)
        assert get_api_address_2 == example_false_reponse_api

    # def test_get_api_wiki(self):
    #     """
    #     # TODO A FAIRE
    #     :return:
    #     """
    #
    #     example_get = {
    #         "batchcomplete": "",
    #         "continue": {
    #             "sroffset": 10,
    #             "continue": "-||"
    #         },
    #         "query": {
    #             "searchinfo": {
    #                 "totalhits": 41
    #             },
    #             "search": [
    #                 {
    #                     "ns": 0,
    #                     "title": "OpenClassrooms",
    #                     "pageid": 4338589,
    #                     "size": 30753,
    #                     "wordcount": 3137,
    #                     "snippet": "chez <span class=\"searchmatch\">OpenClassrooms</span> », <span class=\"searchmatch\">OpenClassrooms</span> : le blog,\u200e 17 avril 2018 (lire en ligne, consulté le 11 juillet 2018) « <span class=\"searchmatch\">OpenClassrooms</span> », sur <span class=\"searchmatch\">openclassrooms</span>.com",
    #                     "timestamp": "2020-12-30T04:35:53Z"
    #                 }
    #             ]
    #         }
    #     }
    #     example_get_no_found = {
    #         "batchcomplete": "",
    #         "query": {
    #             "searchinfo": {
    #                 "totalhits": 0
    #             },
    #             "search": []
    #         }
    #     }
    #
    #     init_wiki = wiki.Wiki()
    #     get_test = init_wiki.get_wiki_address("Openclassrooms")
    #     assert get_test == example_get
    #
    #     get_test_no_found = init_wiki.get_wiki_address("sqdqsdqsdqsdq")
    #     assert get_test_no_found == example_get_no_found
