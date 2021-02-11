import logging
import os

from flask import Flask

from app.config.logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
from app import routes
