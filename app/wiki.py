import requests
import app.config.config as config
from random import choice
from app import logger



class Wiki:
    """
    return the info on the address from the wiki API
    """

    def __init__(self):
        self.url_api = 'http://fr.wikipedia.org/w/api.php'
        self.response_for_api = config.dict_response_grandpy

    def _get_wiki_id_page(self, name) -> int:
        """
        return the id_page wiki page for search name
        :param name: search name in api wiki
        :return: name id_page
        """
        parameters = {
            "action": "query",
            "list": "search",
            "srsearch": name,
            "format": "json",
        }
        get_api = requests.get(self.url_api, params=parameters).json()
        page_id = get_api['query']['search'][0]['pageid']

        return page_id

    def get_wiki_address(self, name) -> str:
        """
        return the id_page wiki page for search name
        :param name: search name in api wiki
        :return: research history (name)
        """
        try:
            page_id = self._get_wiki_id_page(name=name)
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

            test_coherence = 0
            for word in name.split(" "):
                 if word.lower() in get_api_by_id.lower():
                     test_coherence += 1

            if ((test_coherence*100) / len(name.split(" "))) >= 60:
                return get_api_by_id
            else:
                bad_response = choice(self.response_for_api['api_wiki']['bad_response'])
                return bad_response

        except requests.exceptions.ConnectionError as e:
            logger.info("Probleme de connexion à l'API WIKI")
            logger.info(e)
            choise_response_connection_error = choice(self.response_for_api['api_wiki']['connection_error'])

            return choise_response_connection_error
        except IndexError as e:
            logger.error("Aucune information dans l'API WIKI")
            logger.error(e)
            bad_response = choice(self.response_for_api['api_wiki']['bad_response'])

            return bad_response
