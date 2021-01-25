import requests


class Wiki:
    """
    return the info on the address from the wiki API
    """

    def __init__(self):
        # TODO: A REVOIR
        self.key_api = ''
        self.url_api = 'http://fr.wikipedia.org/w/api.php'

    def get_wiki_address(self, name):
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
        print(get_api.json())

        return get_api.json()['query']['search']


if __name__ == "__main__":
    Wiki().get_wiki_address("openclassrooms")
