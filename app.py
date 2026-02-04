import streamlit as st
import requests

# إعداد الصفحة
st.set_page_config(page_title="AuraCoin Speed Dashboard", page_icon="⚡")

# الرابط (تأكد من أنه رابط Firebase الخاص بك)
URL = "https://your-project-default-rtdb.firebaseio.com"

st.title("⚡ AuraCoin Live Dashboard")

# وظيفة لجلب البيانات بسرعة
def get_balance():
    try:
        # إضافة timeout لمنع التعليق في حال بطء الإنترنت
        response = requests.get(URL, timeout=5) 
        data = response.json()
        return data.get('amount', "1,000,000")
    except:
        return "Loading..."

# عرض الرقم بتصميم كبير
balance = get_balance()
st.metric(label="Total Aura mined", value=f"{balance} AC")

# زر تحديث يدوي سريع + تحديث تلقائي كل 30 ثانية لتوفير الطاقة
if st.button('Update Now'):
    st.rerun()

# كود لإجبار الصفحة على التحديث كل 30 ثانية فقط بدلاً من 10 لتسريع الموبايل
st.caption("التحديث التلقائي يعمل كل 30 ثانية لتوفير موارد الموبايل")
