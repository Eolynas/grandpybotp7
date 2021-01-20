import requests
import app.config.config as config


class ApiGoogle:
    """
    return info from the google api of the address
    """

    def __init__(self):
        # TODO: A REVOIR
        self.key_api = config.config['API']['key_api_google']

    def get_address(self, address: str) -> dict:
        """
        # TOTO A FAIRE
        :param address: string parsed
        :return: dict with info googlemap api
        """

        get_api = requests.get(url=f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={self.key_api}&components=country:FR")
        print(get_api)

        return get_api.json()


