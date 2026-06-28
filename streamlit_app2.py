import streamlit as st

st.title("📸 نمایش عکس بر اساس نام")

# گرفتن نام از کاربر و حذف فاصله‌های اضافی
name = st.text_input("نام را وارد کنید (حسن، احمد، محمد):").strip()

# بررسی شرط‌ها برای نمایش عکس
if name == "حسن":
    st.image("IMG-20260628-WA0005.jpg")
elif name == "احمد":
    st.image("Screenshot_20260628_104620_Gallery.jpg")
elif name == "محمد":
    st.image("IMG-20260621-WA0029.jpg")
elif name != "":
    st.error("این نام در سیستم تعریف نشده است! ❌")
