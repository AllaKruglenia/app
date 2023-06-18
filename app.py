
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

import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('ottok_klientov.jpg')

classifier_name=['Random Forest']
option = st.sidebar.selectbox('Алгоритм', classifier_name)
st.subheader(option)

#Importing model and label encoders
model=pickle.load(open("model.pkl","rb"))
# model = pickle.load(open("final_xg_model.pkl","rb"))
le_pik=pickle.load(open("label_encoding_for_gender.pkl","rb"))
le1_pik=pickle.load(open("label_encoding_for_geo.pkl","rb"))


def predict_churn(CreditScore, Geo, Gen, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary):
    input = np.array([[Balance, EstimatedSalary]]).astype(np.float64)
    if option == 'Random Forest':
        prediction = model.predict_proba(input)
        pred = '{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)    
    
# else:
        # pred=0.50
        # #st.markdown('Клиент может уйти, рекомендуется провести СРМ компанию')




def main():
    # st.title("Прогноз оттока клиентов")
    html_temp = """
    <div style="background-color:white ;padding:10px">
    <h2 style="color:red;text-align:center;">Прогноз оттока клиентов</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    CreditScore = st.slider('Скоринговый балл', 300, 900)
    Geography = st.selectbox('Страна', ['France', 'Germany', 'Spain'])
    Geo = int(le1_pik.transform([Geography]))
    Gender = st.selectbox('Пол', ['Male', 'Female'])
    Gen = int(le_pik.transform([Gender]))
    Age = st.slider("Возраст", 18, 95)
    Tenure = st.selectbox("Срок обслуживания", ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','10', '11', '12', '13', '14', '15'])
    Balance = st.slider("Баланс", 0.00, 250000.00)
    NumOfProducts = st.selectbox('Количество продуктов', ['1', '2', '3', '4'])
    HasCrCard = st.selectbox("Наличие кредитной БПК", ['0', '1'])
    IsActiveMember = st.selectbox("Является ли активным клиентом?", ['0', '1'])
    EstimatedSalary = st.slider("Зарплата", 0.00, 200000.00)

    churn_html = """  
              <div style="background-color:#f44336;padding:20px >
               <h2 style="color:red;text-align:center;">Увы, клиент уходит.</h2>
               </div>
            """
    no_churn_html = """  
              <div style="background-color:#94be8d;padding:20px >
               <h2 style="color:green ;text-align:center;"> Хорошая новость, клиент остаётся в банке! </h2>
               </div>
            """
    # if int(Age)-int(Tenure)<18: 
    #     st.error('Внимание проверьте данные возраст и срок обслуживания')

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
    if input:
        prediction = pred(model, input)
        st.write(prediction)
        
st.sidebar.title('ИТ-АКАДЕМИЯ ПРИОРБАНК')
st.sidebar.title('Проект "Отток клиентов"')

st.sidebar.markdown('Курс Diving into Darkness of Data Science.')
st.sidebar.markdown('Подготовила проект Кругленя А.М.')      


