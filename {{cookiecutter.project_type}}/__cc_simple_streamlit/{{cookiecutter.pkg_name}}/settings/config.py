"""
Define here all constants that actually are programs parameters.

Define them as environmental variables, so that one can easily configure the program to
run in an IDE and, above all, make the program portable (for instance with docker)
"""

import os

VERBOSITY = os.getenv("VERBOSITY", "info")
