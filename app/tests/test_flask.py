# from app_flask.hello import app as flask_app
from app import app as flask_app
from app import forms
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
    def test_post_chatbot(self):
        """
        # TODO A FAIRE
        :return:
        """
        data_form = "Bonjour, connnait tu l'adresse d'Openclassrooms"
        c = self.client.post('/message', data={'message': data_form})
        response = self.client.post(
            '/message',
            data={'message': data_form},
            # content_type='application/json',
        )
        # print(c.data)
        assert c.status_code == 200
        assert response.status_code == 200
        # print(response.get_data())
        data = json.loads(response.get_data(as_text=True))
        # assert data['user'] == 'Eddy'
        print(data['data'][0]['message'])
        assert data_form in data['data'][0]['message']
        # {'data': [
        #     {'date': 'Sun, 10 Jan 2021 09:47:02 GMT', 'message': "Bonjour, connnait tu l'adresse d'Openclassrooms",
        #      'user': 'Eddy'},
        #     {'date': 'Sun, 10 Jan 2021 09:47:02 GMT', 'message': "Bonjour, connnait tu l'adresse d'Openclassrooms",
        #      'user': 'GrandPyBOT'}]}

        # assert data['message'] == data_form

        # data = json.loads(response.get_data(as_text=True))
        # assert data['message'] == data_form
        # assert b'<strong>HTML</strong> allowed here' in c.data
        # print(data_form)
        # print(data_form in str(c.data))
        # assert data_form in str(c.data)








