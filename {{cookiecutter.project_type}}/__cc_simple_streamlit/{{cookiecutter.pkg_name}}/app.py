import logging

from tantaroba.log import configure_logging


if __name__ == "__main__":
    configure_logging()

    logging.info("Welcome to {{cookiecutter.directory_name}} app!")
