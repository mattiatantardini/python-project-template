import streamlit as st

from __version__ import __version__
from settings.constants import SITE_NAME


FOOTER_VERSION_HTML = """
            <style>
            footer:after{
                content:' -- %s Version %s';
                position:relative
            }
            </style>
        """


def footer_include_version():
    st.markdown(FOOTER_VERSION_HTML % (SITE_NAME, __version__), unsafe_allow_html=True)
    return
