import requests
import app.config.config as config
from random import *


class Wiki:
    """
    return the info on the address from the wiki API
    """

    def __init__(self):
        self.url_api = 'http://fr.wikipedia.org/w/api.php'
        self.response_for_api = config.dict_response_grandpy

    def get_wiki_address(self, name) -> str:
        """
        # TODO A FAIRE
        :param name:
        :return:
        """
        parameters = {
            "action": "query",
            "list": "search",
            "srsearch": name,
            "format": "json",
        }
        try:
            get_api = requests.get(self.url_api, params=parameters).json()
            page_id = get_api['query']['search'][0]['pageid']
            parameters_by_id = {
                "format": "json",
                "action": "query",
                "prop": "extracts",
                "exintro": 1,
                "explaintext": 1,
                "exsentences": 2,
                "pageids": page_id
            }
            get_api_by_id = requests.get(self.url_api, params=parameters_by_id).json()['query']['pages'][str(page_id)][
                'extract']
            return get_api_by_id
        except requests.exceptions.ConnectionError as e:
            print("Probleme de connexion à l'API WIKI")
            print(e)
            choise_response_connection_error = choice(self.response_for_api['api_wiki']['connection_error'])

            return choise_response_connection_error
        except IndexError as e:
            print("Aucune information dans l'API WIKI")
            print(e)
            bad_response = choice(self.response_for_api['api_wiki']['bad_response'])

            return bad_response





if __name__ == "__main__":
    a = Wiki().get_wiki_address("sdqsdqsdqsdqsdqsdqsdq")
    print(a)
    print("-----")
    b = Wiki().get_wiki_address("Le Mans")
    print(b)
    print("-----")
    c = Wiki().get_wiki_address("Paris")
    print(c)
    print("-----")
