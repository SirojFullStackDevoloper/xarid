# # import bcrypt

# # # Foydalanuvchi ma'lumotlarini saqlash uchun oddiy ma'lumotlar bazasi
# # user_database = {}

# # # Parolni xesh qilish funksiyasi
# # def hash_password(password):
# #     # Parolni xavfsiz xesh qilish
# #     salt = bcrypt.gensalt()
# #     hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
# #     return hashed

# # # Foydalanuvchini ro'yxatdan o'tkazish funksiyasi
# # def register_user(username, password):
# #     if username in user_database:
# #         print("Bu foydalanuvchi allaqachon ro'yxatdan o'tgan.")
# #     else:
# #         hashed_password = hash_password(password)
# #         user_database[username] = hashed_password
# #         print(f"{username} muvaffaqiyatli ro'yxatdan o'tkazildi!")

# # # Loginni tekshirish funksiyasi
# # def login_user(username, password):
# #     if username in user_database:
# #         stored_password = user_database[username]
# #         # Kiritilgan parolni tekshirish
# #         if bcrypt.checkpw(password.encode('utf-8'), stored_password):
# #             print("Login muvaffaqiyatli!")
# #         else:
# #             print("Parol noto'g'ri.")
# #     else:
# #         print("Bunday foydalanuvchi mavjud emas.")

# # # Test dasturi
# # if __name__ == "__main__":
# #     print("Ro'yxatdan o'tish:")
# #     register_user("foydalanuvchi1", "maxfiy_parol")
    
# #     print("\nLogin qilish:")
# #     login_user("foydalanuvchi1", "maxfiy_parol")  # To'g'ri parol
# #     login_user("foydalanuvchi1", "noto'g'ri_parol")  # Noto'g'ri parol


# import bcrypt
# import streamlit as st

# # Foydalanuvchi ma'lumotlarini saqlash uchun oddiy ma'lumotlar bazasi
# user_database = {}

# # Parolni xesh qilish funksiyasi
# def hash_password(password):
#     # Parolni xavfsiz xesh qilish
#     salt = bcrypt.gensalt()
#     hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
#     return hashed

# # Foydalanuvchini ro'yxatdan o'tkazish funksiyasi
# def register_user(username, password):
#     if username in user_database:
#         return "Bu foydalanuvchi allaqachon ro'yxatdan o'tgan."
#     else:
#         hashed_password = hash_password(password)
#         user_database[username] = hashed_password
#         return f"{username} muvaffaqiyatli ro'yxatdan o'tkazildi!"

# # Loginni tekshirish funksiyasi
# def login_user(username, password):
#     if username in user_database:
#         stored_password = user_database[username]
#         # Kiritilgan parolni tekshirish
#         if bcrypt.checkpw(password.encode('utf-8'), stored_password):
#             return "Login muvaffaqiyatli!"
#         else:
#             return "Parol noto'g'ri."
#     else:
#         return "Bunday foydalanuvchi mavjud emas."

# # Streamlit interfeysi
# st.title("Foydalanuvchi tizimi: Ro'yxatdan o'tish va Login")

# menu = st.sidebar.selectbox("Menu", ["Ro'yxatdan o'tish", "Login"])

# if menu == "Ro'yxatdan o'tish":
#     st.subheader("Ro'yxatdan o'tish")
#     username = st.text_input("Foydalanuvchi nomi")
#     password = st.text_input("Parol", type="password")
#     if st.button("Ro'yxatdan o'tish"):
#         if username and password:
#             message = register_user(username, password)
#             st.success(message)
#         else:
#             st.error("Iltimos, foydalanuvchi nomi va parolni kiriting.")

# elif menu == "Login":
#     st.subheader("Login qilish")
#     username = st.text_input("Foydalanuvchi nomi")
#     password = st.text_input("Parol", type="password")
#     if st.button("Login"):
#         if username and password:
#             message = login_user(username, password)
#             if "muvaffaqiyatli" in message.lower():
#                 st.success(message)
#             else:
#                 st.error(message)
#         else:
#             st.error("Iltimos, foydalanuvchi nomi va parolni kiriting.")

import bcrypt
import streamlit as st

# Foydalanuvchi ma'lumotlarini saqlash uchun oddiy ma'lumotlar bazasi
user_database = {}

# Parolni xesh qilish funksiyasi
def hash_password(password):
    # Parolni xavfsiz xesh qilish
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

# Foydalanuvchini ro'yxatdan o'tkazish funksiyasi
def register_user(username, password):
    if username in user_database:
        return "Bu foydalanuvchi allaqachon ro'yxatdan o'tgan."
    else:
        hashed_password = hash_password(password)
        user_database[username] = hashed_password
        return f"{username} muvaffaqiyatli ro'yxatdan o'tkazildi!"

# Loginni tekshirish funksiyasi
def login_user(username, password):
    if username in user_database:
        stored_password = user_database[username]
        # Kiritilgan parolni tekshirish
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            return "Login muvaffaqiyatli!"
        else:
            return "Parol noto'g'ri."
    else:
        return "Bunday foydalanuvchi mavjud emas."

# Ilk foydalanuvchini ma'lumotlar bazasiga qo'shish
user_database["muxtor"] = hash_password("1234")

# Streamlit interfeysi
st.title("Foydalanuvchi tizimi: Ro'yxatdan o'tish va Login")

menu = st.sidebar.selectbox("Menu", ["Ro'yxatdan o'tish", "Login"])

if menu == "Ro'yxatdan o'tish":
    st.subheader("Ro'yxatdan o'tish")
    username = st.text_input("Foydalanuvchi nomi")
    password = st.text_input("Parol", type="password")
    if st.button("Ro'yxatdan o'tish"):
        if username and password:
            message = register_user(username, password)
            st.success(message)
        else:
            st.error("Iltimos, foydalanuvchi nomi va parolni kiriting.")

elif menu == "Login":
    st.subheader("Login qilish")
    username = st.text_input("Foydalanuvchi nomi")
    password = st.text_input("Parol", type="password")
    if st.button("Login"):
        if username and password:
            message = login_user(username, password)
            if "muvaffaqiyatli" in message.lower():
                st.success(message)
            else:
                st.error(message)
        else:
            st.error("Iltimos, foydalanuvchi nomi va parolni kiriting.")
