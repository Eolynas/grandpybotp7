import requests
import app.config.config as config


class ApiGoogle:
    """
    # TODO
    """

    def __init__(self):
        pass

    def get_address(self, addresse: str) -> dict:
        """
        # TOTO A FAIRE
        :param addresse:
        :return:
        """
        key_api = config.config['API']['key_api_google']

        get_api = requests.get(url=f"https://maps.googleapis.com/maps/api/geocode/json?address={addresse}&key={key_api}")
        print(get_api)

        return get_api.json()


