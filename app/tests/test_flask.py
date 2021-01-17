# from app_flask.hello import app as flask_app
from app import app as flask_app
from app import parser, api_google


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

    # def test_post_form_index(self):
    #     """
    #     simulate post form
    #     :return:
    #     """
    #     data_form = 'Chatbot'
    #     c = self.client.post('/', data={'name_project': data_form})
    #     # print(c.data)
    #     assert c.status_code == 200
    #     assert data_form in str(c.data)

    # CREER LE MESSAGE ET L'ENVOIE EN POST SUR LA ROUTE 'chatbot'
    # def test_post_chatbot(self):
    #     """
    #     # TODO A FAIRE
    #     :return:
    #     """
    #     data_form = "Bonjour, connnait tu l'adresse d'Openclassrooms"
    #     c = self.client.post('/message', data={'message': data_form})
    #     response = self.client.post(
    #         '/message',
    #         data={'message': data_form},
    #         # content_type='application/json',
    #     )
    #     # print(c.data)
    #     assert c.status_code == 200
    #     assert response.status_code == 200
    #     # print(response.get_data())
    #     data = json.loads(response.get_data(as_text=True))
    #     # assert data['user'] == 'Eddy'
    #     print(data['data'][0]['message'])
    #     assert data_form in data['data'][0]['message']

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

        parse_message = parse_question.parser(messages[0])
        assert parse_message == ["openclassrooms"]

        parse_message = parse_question.parser(messages[1])
        assert parse_message == ["openclassrooms"]

        parse_message = parse_question.parser(messages_empty)
        assert parse_message == []

        parse_message = parse_question.parser(messages_number)
        assert parse_message == []
        #
        # parse_message = parse_question.parser(messages_speciaux[0])
        # assert parse_message == ["eddy"]
        # #
        # parse_message = parse_question.parser(messages_speciaux[1])
        # assert parse_message == ["bonjour"]

    def test_get_api(self):
        """
        # TODO A FAIRE
        :return:
        """
        example_true_reponse_api = {
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

        example_false_reponse_api = {
            "results": [],
            "status": "ZERO_RESULTS"
        }

        question_parsed_1 = "openclassrooms"
        question_parsed_2 = "sqsdqqdqsdqsdq"
        init_api = api_google.ApiGoogle()

        get_api_address = init_api.get_address(question_parsed_1)
        print(get_api_address)
        assert get_api_address == example_true_reponse_api

        get_api_address_2 = init_api.get_address(question_parsed_2)
        print(get_api_address_2)
        assert get_api_address_2 == example_false_reponse_api




