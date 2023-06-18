import sklearn

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

import streamlit as st
import pickle
import numpy as np

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
    .stApp {
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
# model=pickle.load(open("model.pkl","rb"))
model = pickle.load(open("final_model.pkl","rb"))
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

    Age = st.slider("Возраст", 18, 95)
    Tenure = st.selectbox("Срок обслуживания", ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','10', '11', '12', '13', '14', '15'])
    CreditScore = st.slider('Скоринговый балл', 300, 900)
    Geography = st.selectbox('Страна', ['France', 'Germany', 'Spain'])
    Geo = int(le1_pik.transform([Geography]))
    Gender = st.selectbox('Пол', ['Male', 'Female'])
    Gen = int(le_pik.transform([Gender]))
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
    if int(Age)-int(Tenure)<18: 
        st.error('Внимание проверьте данные возраст и срок обслуживания')
 
    
    if st.button('Сделать прогноз'):
        output = predict_churn(CreditScore, Geo, Gen, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary)
        st.success('Вероятность оттока составляет {}'.format(output))


        # if output >= 0.5:
        #     st.markdown(churn_html, unsafe_allow_html= True)

        # else:
        #     st.markdown(no_churn_html, unsafe_allow_html= True)
       
        # if Balance<200 and EstimatedSalary<100 and IsActiveMember==0 and Age<22 and Tenure==0:
        #     st.success('Вероятность оттока составляет более 70%.')
        #     st.markdown(churn_html, unsafe_allow_html= True)

        # if CreditScore < 200 and Balance < 10000 and EstimatedSalary < 10000 and IsActiveMember == 0 and Age > 70 and Tenure == 1:
        #     st.success('Вероятность оттока составляет более 60%.')
        #     st.markdown(churn_html, unsafe_allow_html= True)

        # if CreditScore < 300 and Balance < 15000 and EstimatedSalary < 15000 and IsActiveMember == 0 and Age > 60 and Tenure == 2:
        #     st.success('Вероятность оттока составляет более 50%.')
        #     st.markdown(churn_html, unsafe_allow_html= True)

        # if CreditScore > 100 and EstimatedSalary > 5000 and IsActiveMember == 1 and NumOfProducts > 1 and Age < 60 and Tenure > 3 and Balance > 5000:
        #     st.success('Вероятность оттока составляет менее 30%.')
        #     st.markdown(churn_html, unsafe_allow_html= True)
  
        # if CreditScore > 200 and EstimatedSalary > 10000 and IsActiveMember == 1 and NumOfProducts > 2 and Age < 50 and Tenure > 4 and Balance > 10000:
        #     st.success('Вероятность оттока составляет менее 20%.')
        #     st.markdown(churn_html, unsafe_allow_html= True)

        # if CreditScore > 300 and EstimatedSalary > 15000 and IsActiveMember == 1 and NumOfProducts > 3 and Age < 40 and Tenure > 5 and Balance > 20000:
        #     st.success('Вероятность оттока составляет менее 10%.')
        #     st.markdown(churn_html, unsafe_allow_html= True)
        
        if int(Age)-int(Tenure)<18: 
            st.error('Внимание проверьте данные возраст и срок обслуживания')
            
        
        elif Balance < 1000 and EstimatedSalary < 500 and IsActiveMember == 0 and NumOfProducts == 1:
            st.success('Вероятность оттока составляет более 90%.')
            st.markdown(churn_html, unsafe_allow_html= True)

        elif Balance > 2000 and EstimatedSalary > 2000 and CreditScore > 250:
            # and predict_churn(CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary)  > 40:
            st.success('Вероятность оттока составляет менее 40 %.')
            st.markdown(no_churn_html, unsafe_allow_html= True)
                
        else:
            output = predict_churn(CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary)
            st.success('Вероятность оттока составляет {0:.2f}'.format(output))
            if output >= 85:
                st.markdown(churn_html, unsafe_allow_html= True)
            elif output >= 40:
                st.markdown(mb_churn_html, unsafe_allow_html= True)
            else:
                st.markdown(no_churn_html, unsafe_allow_html= True)

        

if __name__=='__main__':
    main()

st.sidebar.title('ИТ-АКАДЕМИЯ ПРИОРБАНК')
st.sidebar.title('Проект "Отток клиентов"')


st.sidebar.markdown('Курс Diving into Darkness of Data Science.')
st.sidebar.markdown('Подготовила проект Кругленя А.М.')
