import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from pathlib import Path
import base64
import matplotlib.pyplot as plt
from PIL import Image
import random

st.markdown("""
<h2 style="color:white; text-align:center;">
💗 Проценты 💗
</h2>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
x = col1.slider('Выбери насколько % ты меня любишь', 0, 100)
st.error(f'Насколько я люблю тебя {x + 1} % 💗')


st.set_page_config(
    page_title="💗 Love",
    page_icon="💗",
    layout="centered"
)


# =========================
# ЗАГРУЗКА ФОНА
# =========================

image_path = "hearts-design.jpg"

with open(image_path, "rb") as file:
    image = base64.b64encode(file.read()).decode()



# -------------------------
# ФОН
# -------------------------

from pathlib import Path
import base64

image_path = Path(__file__).parent / "hearts-design.jpg"

with open(image_path, "rb") as file:
    image = base64.b64encode(file.read()).decode("utf-8")

st.markdown(f"""
<style>

.stApp {{
    background-image: url("data:image/jpeg;base64,{image}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Кнопка */

.stButton > button {{
    background: linear-gradient(135deg, #ff69b4, #ff1493);
    color: white;
    border: none;
    border-radius: 20px;

    padding: 15px 35px;

    font-size: 20px;
    font-weight: bold;

    box-shadow: 0 5px 20px rgba(255, 20, 147, 0.4);

    transition: 0.3s;
}}

.stButton > button:hover {{
    transform: scale(1.08);
    box-shadow: 0 8px 30px rgba(255, 20, 147, 0.7);
}}

.stButton > button:active {{
    transform: scale(0.95);
}}

</style>
""", unsafe_allow_html=True)



# -------------------------
# КНОПКА
# -------------------------
st.markdown("""
<h2 style="color:white; text-align:center;">
💗 График 💗
</h2>
""", unsafe_allow_html=True)


st.markdown(
    r"""
    <div style="
        text-align: center;
        font-size: 24px;
        color: #ff1493;
        font-weight: bold;
        margin: 30px 0 20px 0;
    ">
        Сегодня я решала задачу
        <br><br>
        <span style="font-size: 26px;">
            x² + (y − ∛(x²))² = 1
        </span>
        <br><br>
        Хочешь посмотреть ответ?
    </div>
    """,
    unsafe_allow_html=True
)

if st.button("💗 Да, посмотреть 💗"):
    st.session_state.show_graph = True

# Запоминаем, нажата ли кнопка
if "show_graph" not in st.session_state:
    st.session_state.show_graph = False


# Создаём маленький график
fig, ax = plt.subplots(figsize=(4, 3))

# Оси
ax.axhline(0, linewidth=1)
ax.axvline(0, linewidth=1)

# Сетка
ax.grid(True, alpha=0.3)

# Границы графика
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 2.2)

ax.set_aspect("equal")

ax.set_xlabel("")
ax.set_ylabel("")
ax.set_title("")


# Если кнопку нажали — рисуем функцию
if st.session_state.show_graph:

    x = np.linspace(-1, 1, 500)

    cube_root = np.cbrt(x ** 2)
    sqrt_part = np.sqrt(1 - x ** 2)

    y1 = cube_root + sqrt_part
    y2 = cube_root - sqrt_part

    ax.plot(x, y1, linewidth=2)
    ax.plot(x, y2, linewidth=2)


# -------------------------
# Картинка с котиками
# -------------------------
# График всегда находится на странице
st.pyplot(fig, width="stretch")
# Загружаем картинку
image_path = Path(__file__).parent / "Cats.jpg"

with open(image_path, "rb") as file:
    image = base64.b64encode(file.read()).decode("utf-8")


st.markdown("""
<h2 style="color:white; text-align:center;">
💗 Открой картинку 💗
</h2>
""", unsafe_allow_html=True)

image = Image.open("Cats.jpg")


# Фиксированный размер картинки на экране
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = int(image.height * DISPLAY_WIDTH / image.width)

# Слайдер
value = st.slider(
    "Проведи ползунок →",
    min_value=0,
    max_value=100,
    value=0
)

# Масштабируем ОДИН раз до нужного статичного размера
image = image.resize((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# Сколько картинки показать
visible_width = int(DISPLAY_WIDTH * value / 100)

# Создаём изображение такого же размера,
# но сначала полностью прозрачное
result = Image.new("RGBA", (DISPLAY_WIDTH, DISPLAY_HEIGHT), (0, 0, 0, 0))

# Обрезанная часть вставляется слева
if visible_width > 0:
    cropped = image.crop(
        (0, 0, visible_width, DISPLAY_HEIGHT)
    )

    result.paste(cropped, (0, 0))

st.image(result, width=DISPLAY_WIDTH)

st.markdown("""
<h2 style="color:white; text-align:center;">
💗 Кнопочки 💗
</h2>
""", unsafe_allow_html=True)


# Варианты сердечек
heart_variants = [
    "💗 ",
    "💕 ",
    "💖 ",
    "❤️ ",
    "💞 ",
    "💗 "
]


# Запоминаем текущие сердечки
if "hearts" not in st.session_state:
    st.session_state.hearts = ""


# Кнопка
if st.button("💗 Нажми меня 💗"):

    new_hearts = random.choice(heart_variants)

    # Не повторяем предыдущий вариант
    while new_hearts == st.session_state.hearts:
        new_hearts = random.choice(heart_variants)

    st.session_state.hearts = new_hearts


# Показываем сердечки
if st.session_state.hearts:
    st.markdown(
        "<div style='text-align:center; "
        "font-size:32px; "
        "margin-top:15px;'>"
        + st.session_state.hearts
        + "</div>",
        unsafe_allow_html=True
    )


hearts = st.button("💗 Сердечки")


sun = st.button("И сюда тыкни")


# ---------------------------
# СЕРДЕЧКИ
# ---------------------------

if hearts:

    hearts_html = ""

    for i in range(25):

        left = random.randint(5, 95)
        size = random.randint(20, 45)
        delay = random.uniform(0, 1.5)
        duration = random.uniform(2, 4)

        hearts_html += f"""
        <div class="heart"
             style="
                left: {left}%;
                font-size: {size}px;
                animation-delay: {delay}s;
                animation-duration: {duration}s;
             ">
            {random.choice(["💗", "💖", "💕", "💞", "❤️"])}
        </div>
        """

    st.markdown(
        f"""
        <style>

        .heart {{
            position: fixed;
            bottom: 20px;
            z-index: 999999;
            pointer-events: none;

            animation-name: heart-fly;
            animation-timing-function: ease-out;
            animation-fill-mode: forwards;
        }}

        @keyframes heart-fly {{

            0% {{
                transform: translateY(0) scale(0.3) rotate(0deg);
                opacity: 0;
            }}

            15% {{
                opacity: 1;
            }}

            100% {{
                transform: translateY(-90vh) scale(1.3) rotate(360deg);
                opacity: 0;
            }}

        }}

        </style>

        {hearts_html}
        """,
        unsafe_allow_html=True
    )


# ---------------------------
# СООБЩЕНИЕ
# ---------------------------

if sun:

    st.markdown(
        """
        <div style="
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            font-size: 30px;
            font-weight: bold;
            color: #ff1493;
        ">
            ☀️ Ты солнце) ☀️
        </div>
        """,
        unsafe_allow_html=True
    )