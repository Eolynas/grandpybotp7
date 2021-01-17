import os
import configparser

cnx_db = False
config = configparser.ConfigParser()


try:

    config.read("app/config/config.ini")
    print("____________________________________")
    print("LOAD FILE CONFIGURATION")
    print("____________________________________")

except:
    print("Erreur pendant la lecture du fichier config")


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

