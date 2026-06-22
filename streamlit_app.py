import streamlit as st
import os

st.set_page_config(
    page_title="单词大爆炸 Word Blast",
    page_icon="💥",
    layout="centered"
)

html_path = os.path.join(os.path.dirname(__file__), "word_blast.html")
with open(html_path, "r", encoding="utf-8") as f:
    game_html = f.read()

st.components.v1.html(game_html, height=680, scrolling=False)
