# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:04:46 2020
Script with defined app, including styling.
@author: Ifeanyi Nneji
"""

from PIL import Image

import streamlit as st

from functions.functions import *

# app design
app_meta('🖼️')
#set_bg_hack('./images/background.jpg')

# hide warning for st.pyplot() deprecation
st.set_option('deprecation.showPyplotGlobalUse', False)

# Main panel setup
display_app_header(main_txt='WordsAI',
                       sub_txt='A collection of Natural Language Processing apps')


st.markdown("""
    # Welcome to WordsAI
    A collection of Natural Language Processing apps

    """, unsafe_allow_html=True)

st.markdown("""
    ### About
    This app is a collection of Natural Language Processing apps that uses the WordsAI API to perform Natural Language Processing tasks.
    Features:
    - Text Summarizer
    - Webpage Summarizer
    - Sentiment Analyzer
    - Autocorrect
    - Resume Parser
    - Wordcloud
    - Translate
    - Optical Character Recognition
    - Speech to Text

    You can also check out the [Github repo](https://github.com/Nneji123/WordsAI) for more information.

    """, unsafe_allow_html=True)

st.markdown("""
    ### How to use
    1. Select a category from the sidebar.
    2. Select a app from the sidebar.
    3. Input text or URL.
    4. Click the button.
    """, unsafe_allow_html=True)

st.markdown("""
    ### Credits
    This app is created by Ifeanyi Nneji.
    """, unsafe_allow_html=True)

st.markdown("""
    ### Contact
    [Ifeanyi Nneji](https://www.github.com/Nneji123/)


    """)

   