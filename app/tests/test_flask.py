# from app_flask.hello import app as flask_app
from app import app as flask_app
from app import forms, parser
from flask import json


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









        # TEST SUR UNE CHAINE SI JE RECUPERER LES BONS MOTS

        #









