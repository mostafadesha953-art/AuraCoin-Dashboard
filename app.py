import streamlit as st
import requests
import time

# إعدادات الصفحة
st.set_page_config(page_title="AuraCoin Live Monitor", page_icon="💎")

# رابط الـ API الخاص بـ Firebase (تأكد من وضع رابطك الصحيح هنا)
URL = "https://your-project-default-rtdb.firebaseio.com"

st.title("💎 AuraCoin Live Monitor")
st.write("متابعة حية لتعدين عملة Aura من ويندوز 7")

# حاوية لتحديث البيانات بدون إعادة تحميل الصفحة بالكامل
placeholder = st.empty()

# حلقة تكرار للتحديث التلقائي كل 10 ثوانٍ
while True:
    try:
        response = requests.get(URL)
        data = response.json()
        # التأكد من وجود بيانات أو وضع المليون كافتراضي
        live_balance = data.get('amount', "1,000,000")
    except Exception as e:
        live_balance = "Searching..."

    with placeholder.container():
        st.metric(label="إجمالي الرصيد الحالي", value=f"{live_balance} AC")
        st.info(f"آخر تحديث: {time.strftime('%H:%M:%S')}")
    
    # التوقف لمدة 10 ثوانٍ قبل التحديث القادم
    time.sleep(10)
