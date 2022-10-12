import logging

from settings.config import VERBOSITY


def configure_logging(verbosity: str=VERBOSITY):
    """
    Configures the logging format for the whole program.

    Args:
        verbosity (str, optional): log verbosity. By default it is taken equal to 
        the value of the corresponding environmental variable. Defaults to VERBOSITY.

    Raises:
        NotImplementedError: error whether the provided verbosity does not exists.
    """
    log_level = logging.getLevelName(verbosity.upper())
    if isinstance(log_level, int):
        logging.basicConfig(
            level=log_level,
            format="[%(levelname)s] %(asctime)s | %(message)s | in function: %(funcName)s",
            force=True, # see https://stackoverflow.com/questions/73882299/python-logging-messages-not-showing-up-due-to-imports/73882890#73882890
        )
    else:
        raise NotImplementedError(f"Logging level {verbosity} does not exist!")
