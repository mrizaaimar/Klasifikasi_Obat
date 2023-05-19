import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('obat.sav', 'rb'))

st.title('Prediksi Obat')
Age = st.number_input('Umur Pasien')
Sex = st.number_input('Jenis Kelamin (0 = Perempuan; 1 = Laki-laki)')
BP = st.number_input('Tekanan Darah (0 = HIGH; 1 = LOW; 2 = NORMAL)')
Cholesterol = st.number_input('Kolesterol (0 = HIGH; 1 = NORMAL)')
Na_to_K = st.number_input('Kandungan Sodium')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[Age, Sex, BP, Cholesterol, Na_to_K]])

    if (prediksi [0] == 0):
        prediksi = 'Obat yang disarankan adalah obat A'
    elif(prediksi == 1):
        prediksi = 'Obat yang disarankan adalah obat B'
    elif(prediksi == 2):
        prediksi = 'Obat yang disarankan adalah obat C'
    elif(prediksi == 3):
        prediksi = 'Obat yang disarankan adalah obat X'
    else:
        prediksi = 'Obat yang disarankan adalah obat Y'
st.success(prediksi)