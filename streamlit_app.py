import streamlit as st
import os

st.set_page_config(
    page_title="小鼠去旅行 - 风景跑酷",
    page_icon="🐭",
    layout="centered"
)

# 读取游戏 HTML
html_path = os.path.join(os.path.dirname(__file__), "parkour_game.html")
with open(html_path, "r", encoding="utf-8") as f:
    game_html = f.read()

# 嵌入游戏
st.components.v1.html(game_html, height=550, scrolling=False)
