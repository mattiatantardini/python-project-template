import logging

import streamlit as st
from tantaroba.log import configure_logging


if __name__ == "__main__":
    configure_logging()

    logging.info("Welcome to {{cookiecutter.directory_name}} app!")
    st.title("Your first app!")
    st.ballons()
