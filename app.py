import streamlit as st
import pandas as pd
import joblib

# Modelni yuklash
model_path = "purchase_amount_predictor.pkl"
model = joblib.load(model_path)

# Sarlavha
st.title("Xaridorlar Xarid Miqdorini Bashorat Qilish Ilovasi")

# Foydalanuvchidan kirish ma'lumotlarini olish
st.sidebar.header("Ma'lumotlarni kiriting:")

age_group = st.sidebar.selectbox("Yosh guruhi:", ['18-24', '25-34', '35-44', '45-54', '55+'])
category = st.sidebar.selectbox("Kategoriya:", ['Electronics', 'Fashion', 'Home & Kitchen', 'Sports', 'Books', 'Beauty'])
region = st.sidebar.selectbox("Hudud:", ['North', 'South', 'East', 'West'])
purchase_method = st.sidebar.selectbox("Xarid qilish usuli:", ['Online', 'In-store'])
day_of_purchase = st.sidebar.slider("Xarid qilingan kun:", 1, 31, 15)

# Foydalanuvchi kiritgan ma'lumotlardan DataFrame yaratish
input_data = pd.DataFrame({
    'AgeGroup': [age_group],
    'Category': [category],
    'Region': [region],
    'PurchaseMethod': [purchase_method],
    'DayOfPurchase': [day_of_purchase]
})

# Bashorat qilish tugmasi
if st.sidebar.button("Bashorat qilish"):
    # Modeldan foydalangan holda bashorat qilish
    prediction = model.predict(input_data)
    st.success(f"Bashorat qilingan xarid miqdori: ${prediction[0]:.2f}")
else:
    st.info("Ma'lumotlarni kiriting va 'Bashorat qilish' tugmasini bosing.")

# Eslatma
st.write("---")
st.write("Ushbu dastur xaridorlarning xarid miqdorini bashorat qilish uchun Random Forest Regression modelidan foydalanadi.")
