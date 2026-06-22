import streamlit as st
import os

st.set_page_config(
    page_title="瑞士阿尔卑斯 · 风景列车",
    page_icon="🚂",
    layout="centered"
)

html_path = os.path.join(os.path.dirname(__file__), "train_journey.html")
with open(html_path, "r", encoding="utf-8") as f:
    game_html = f.read()

st.components.v1.html(game_html, height=630, scrolling=False)
