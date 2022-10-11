import logging

# Define the logs and set verbosity
def configure_logging(verbosity="INFO"):
    log_level = logging.getLevelName(verbosity)
    if isinstance(log_level, int):
        logging.basicConfig(
            level=log_level,
            format="[%(levelname)s] %(asctime)s | %(message)s | in function: %(funcName)s",
            force=True, # see https://stackoverflow.com/questions/73882299/python-logging-messages-not-showing-up-due-to-imports/73882890#73882890
        )
    else:
        raise NotImplementedError(f"Logging level {verbosity} does not exist!")
