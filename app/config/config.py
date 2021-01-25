import os
import configparser
import json

cnx_db = False
config = configparser.ConfigParser()
dict_response_grandpy = []


try:

    print("____________________________________")
    print("LOAD FILE CONFIGURATION")
    print("____________________________________")
    config.read("app/config/config.ini")
    file_json_response_grandpy = 'app/response.json'
    with open(file_json_response_grandpy) as json_file:
        data = json.load(json_file)
        dict_response_grandpy = data

except:
    print("Erreur pendant la lecture du fichier config")


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

