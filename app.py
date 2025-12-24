import streamlit as st
import random

# تنظیمات صفحه
st.set_page_config(page_title="شکار عدد مرموز", page_icon="🎯")

st.title("🎯 بازی شکار عدد مرموز")
st.write("من یک عدد بین **1 تا 100** انتخاب کردم. بتونی حدسش بزنی؟")

# مقداردهی اولیه متغیرهای بازی در session_state
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# تابع برای شروع مجدد بازی
def reset_game():
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# طراحی رابط کاربری
col1, col2 = st.columns([3, 1])

with col1:
    guess = st.number_input("حدس شما چیست؟", min_value=1, max_value=100, step=1, key="user_guess")

with col2:
    st.write("") # فاصله عمودی
    submit = st.button("ثبت حدس")

# منطق بازی
if submit and not st.session_state.game_over:
    st.session_state.attempts += 1
    
    if guess < st.session_state.secret_number:
        st.warning("🔼 عدد بزرگتره! دوباره سعی کن.")
    elif guess > st.session_state.secret_number:
        st.warning("🔽 عدد کوچکتره! دوباره سعی کن.")
    else:
        st.balloons()
        st.success(f"🎉 تبریک! عدد {st.session_state.secret_number} بود. تو در {st.session_state.attempts} مرحله برنده شدی!")
        st.session_state.game_over = True

# نمایش تعداد تلاش‌ها
st.info(f"تعداد حدس‌های تا الان: {st.session_state.attempts}")

# دکمه بازی مجدد
if st.session_state.game_over:
    if st.button("شروع دوباره بازی"):
        reset_game()
        st.rerun()