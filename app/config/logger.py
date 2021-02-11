""" this module takes care of the logger in project """
import os
import yaml
import logging.config
import logging
import coloredlogs


def setup_logging(default_path='app/config/logger.yaml', default_level=logging.INFO):
    """
    run logger
    """
    path = default_path
    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
                coloredlogs.install()
            except Exception as e:
                print(e)
                print('Error in Logging Configuration. Using default configs')
                logging.basicConfig(level=default_level)
                coloredlogs.install(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        print('Failed to load configuration file. Using default configs')
