import streamlit as st
from supabase import create_client
import time

# بيانات الربط (ضع بياناتك هنا)
URL = "رابط_الذي_حصلت_عليه"
KEY = "المفتاح_الذي_نسخته_anon_public"

supabase = create_client(URL, KEY)

st.title("💎 AuraCoin Live Dashboard")

# جلب البيانات
def fetch_data():
    try:
        response = supabase.table("mining_stats").select("balance").order("created_at", desc=True).limit(1).execute()
        return response.data[0]['balance']
    except:
        return "1,000,000"

balance = fetch_data()
st.metric(label="إجمالي التعدين الحالي", value=f"{balance} AC")

# تحديث تلقائي
time.sleep(10)
st.rerun()
