import logging

import pytest


@pytest.mark.functions
def test_function():
    logging.debug("Testing function with message")
    message = "Ciao Intellera!"
    assert message == "CIAO INTELLERA!"
