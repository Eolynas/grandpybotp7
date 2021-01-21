import requests
import app.config.config as config
from app import function


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
        # get_api = get_api.json()
        #
        # dict_get_api = {}
        # date_now = function.get_date_now()
        # if get_api["status"] == "ZERO_RESULTS":
        #     message_no_found = f"Désolé mon petit, je ne trouve pas l'adresse de {parse_question}"
        #     dict_message = {'data': message_no_found, 'date': date_now}
        #     dict_get_api['message'] = dict_message
        #     dict_get_api['status'] = False
        #
        #     return jsonify(data=dict_get_api)
        #
        # else:
        #     print(cnx_api)
        #     message_return = f" Voici l'adresse de {parse_question}: {get_api['results'][0]['formatted_address']}"
        #     dict_message = {'data': message_return, 'date': date_now}
        #     dict_get_api['message'] = dict_message
        #     dict_get_api['status'] = True
        #     dict_get_api['address'] = get_api["results"][0]["formatted_address"]
        #     dict_get_api['location'] = get_api["results"][0]["geometry"]["location"]

        return get_api.json()


