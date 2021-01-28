import requests


class Wiki:
    """
    return the info on the address from the wiki API
    """

    def __init__(self):
        # TODO: A REVOIR
        self.key_api = ''
        self.url_api = 'http://fr.wikipedia.org/w/api.php'

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
        get_api = requests.get(self.url_api, params=parameters)
        # print(get_api.json())
        page_id = get_api.json()['query']['search'][0]['pagseid']
        parameters_by_id = {
            "format": "json",
            "action": "query",
            "prop": "extracts",
            "exintro" : 1,
            "explaintext" : 1,
            "exsentences" : 2,
            "pageids" : page_id
        }

        get_api_by_id = requests.get(self.url_api, params=parameters_by_id).json()['query']['pages'][str(page_id)]['extract']

        return get_api_by_id


        # return get_api.json()['query']['search']


if __name__ == "__main__":
    Wiki().get_wiki_address("openclassrooms")
    Wiki().get_wiki_address("Le Mans")
    Wiki().get_wiki_address("Paris")
