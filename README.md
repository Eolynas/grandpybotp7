# GrandPy Bot (Chatbot)

[![Generic badge](https://img.shields.io/badge/GrandPyBot-0.9-<>.svg)]()
[![made-with-python](https://img.shields.io/badge/Made%20with-Python_Flask-1f425f.svg)]()
[![version-python](https://img.shields.io/static/v1?label=Python&message=3.7&color=065535)]()


--------------
# Détail du projet

Ah, les grands-pères... Je ne sais pas vous, mais le mien connaissait quantité d'histoires. Il me suffisait de lui dire un mot pour le voir parti pendant des heures. "Tu veux l'adresse de la poste ? Ah oui, c'est bien. Mais je t'ai déjà raconté que j'ai aidé à la construire ? C'était en 1974 et..." 😴

Pourtant, j'adore ses récits ! J'ai beaucoup appris et rêvé d'autres contrées en l'écoutant. Voici donc le projet que je vous propose : créer un robot qui vous répondrait comme votre grand-père ! Si vous lui demandez l'adresse d'un lieu, il vous la donnera, certes, mais agrémentée d'un long récit très intéressant. Vous êtes prêt·e ?

--------------
# Fonctionnalités

- Interactions en AJAX : l'utilisateur envoie sa question en appuyant sur entrée et la réponse s'affiche directement dans l'écran, sans recharger la page.
- Utilisation de l'API de Google Maps pour récuperer l'adresse et l'affichage de la mini-map
- Utilisation de l'API de Media WIKI pour la recherche d'une histoire sur le lieux
- Rien n'est sauvegardé. Si l'utilisateur charge de nouveau la page, tout l'historique est perdu.
- Mise en ligne par Heroku

--------------
# Installation

Installation des dépendances

```
pip install -r requirements.txt
```

Création des variables d'environnment:
```
DEBUG_FLASK= True for true, vide si false
SECRET_KEY= YOUR SECRET KEY
key_api_google= YOUR API KEY GOOEL
```

--------------
# Author

Développeur: Eddy Hubert

Contact: contact@eddy-hubert.fr
