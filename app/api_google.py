import requests
import app.config.config as config
from datetime import datetime
from random import *


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

        try:
            get_api = requests.get(url=f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={self.key_api}&components=country:FR")
            response = get_api.json()

            dict_get_api = {}
            date_now = datetime.now()
            date_now = date_now.strftime("%d/%m/%Y %H:%M")
            response_for_api = config.dict_response_grandpy
            if response["status"] == "ZERO_RESULTS":
                choise_response = choice(response_for_api['api_google']['bad_response'])
                message_no_found = f"{choise_response} {address}"
                dict_message = {'data': message_no_found, 'date': date_now}
                dict_get_api['message'] = dict_message
                dict_get_api['status'] = False

                return dict_get_api

            else:
                choise_response = choice(response_for_api['api_google']['good_response'])
                try:
                    message_return = f" {choise_response} {address}: {response['results'][0]['formatted_address']}"
                    dict_message = {'data': message_return, 'date': date_now}
                    dict_get_api['message'] = dict_message
                    dict_get_api['status'] = True
                    dict_get_api['address'] = response["results"][0]["formatted_address"]
                    dict_get_api['location'] = response["results"][0]["geometry"]["location"]
                    return dict_get_api
                except KeyError:
                    print("je n'ai pas toutes les infos")
                    dict_get_api['status'] = False
                    return dict_get_api
        except:
            print("ERREUR APPEL API")
            # TODO GESITON CODE 200


