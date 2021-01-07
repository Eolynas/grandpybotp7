# from app_flask.hello import app as flask_app
from app import app as flask_app


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

    def test_post_form_index(self):
        """
        simulate post form
        :return:
        """
        data_form = 'Chatbot'
        c = self.client.post('/', data={'name_project': data_form})
        # print(c.data)
        assert c.status_code == 200
        assert data_form in str(c.data)

    def test_post_chatbot(self):
        """

        :return:
        """
        data_form = "Bonjour, connnait tu l'adresse d'Openclassrooms"
        c = self.client.post('/chatbot', data={'message': data_form})
        # print(c.data)
        assert c.status_code == 200
        # print(data_form)
        print(data_form in str(c.data))
        # assert data_form in str(c.data)







