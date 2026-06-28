import streamlit as st

# ساخت کادرهای دریافت ورودی روی سایت
name = st.text_input("give me a name:")
number = st.text_input("give me number:")

# دکمه برای اجرای برنامه
if st.button("Make User"):
    username = f"{name}@{number}"
    st.success(f"for your name and number we make this user: {username}")
