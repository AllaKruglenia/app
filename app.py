
#####
import sklearn

# from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

import streamlit as st
import pickle
import numpy as np
import pandas as pd
import pickle
import streamlit as st

import base64
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgFzljZpFVn-h0RJLKnldE0KBP1F-lB_VV-w&usqp=CAU")
        background-size: 50%; 
        background-size: 3.2em;
        background-size: 12px;
        background-size: auto;
    }
   .sidebar.sidebar-content {
        background: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_TwY4kqrJ5o1Je28Ro4ZOayfq9S_OaZFW5g&usqp=CAU")
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# import base64

# @st.cache(allow_output_mutation=True)
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('background2.jpg')



def load_model():
    with open("model.pickle", "rb") as file:
        model = pickle.load(file)
    return model
    from load_model import load_model

    model = load_model()



def user_input_features():
    Age = st.slider('Возраст', 18, 92, 31)
    Balance = st.slider('Баланс', 0.00, 12544.90, 2000.00)
    NumOfProducts = st.slider('Количество продуктов оформленных в банке', 1, 4, 2)
    EstimatedSalary = st.slider('Размер зароботной платы', 0.00, 4444.28, 1500.00)
    CreditScore = st.slider('Кредитный рейтинг', 350, 850, 400)
    data = {'Возраст': Age,
            'Баланс': Balance,
            'Количество продуктов оформленных в банке': NumOfProducts,
            'Размер зароботной платы': EstimatedSalary,
            'Кредитный рейтинг': CreditScore,}
    features = pd.DataFrame(data, index=[0])
    return features
input = user_input_features()


if st.button("Предсказать отток клиентов"):
    if input_data:
        prediction = pred(model, input)
        st.write(prediction)
        
st.sidebar.title('ИТ-АКАДЕМИЯ ПРИОРБАНК')
st.sidebar.title('Проект "Отток клиентов"')

st.sidebar.markdown('Курс Diving into Darkness of Data Science.')
st.sidebar.markdown('Подготовила проект Кругленя А.М.')      


