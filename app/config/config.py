import os
import json
from pathlib import Path

dict_response_grandpy = []


try:
    json_response_file_path = config_file_path = Path(os.path.dirname(os.path.abspath(__file__))).absolute().parent / 'static/response.json'
    with open(json_response_file_path) as json_file:
        data = json.load(json_file)
        dict_response_grandpy = data

except:
    print("Erreur pendant la lecture du fichier config")


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

