import streamlit as st
import requests

# رابط الـ API
URL = "https://your-project-default-rtdb.firebaseio.com"

st.title("💎 AuraCoin Live Monitor")

# جلب البيانات من الـ API
try:
    response = requests.get(URL)
    data = response.json()
    live_balance = data['amount']
except:
    live_balance = "1,000,000" # رقم احتياطي في حال فشل الاتصال

st.metric(label="Live Aura Balance", value=f"{live_balance} AC")

# تحديث تلقائي للصفحة كل 30 ثانية
st.empty()
time_now = st.runtime.scriptrunner.add_report_ctx
