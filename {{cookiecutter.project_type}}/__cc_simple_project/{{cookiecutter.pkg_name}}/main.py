import logging

from common.utils import configure_logging


if __name__ == "__main__":
    configure_logging()

    logging.info("Welcome to {{cookiecutter.directory_name}} project!")
