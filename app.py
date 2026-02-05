import streamlit as st
from supabase import create_client
import time

# بياناتك الخاصة من Supabase
URL = "https://ejlrrnoegmlqcfclonqa.supabase.co"
KEY = "ضع_هنا_مفتاح_anon_public_الذي_نسخته"

# تهيئة الاتصال
supabase = create_client(URL, KEY)

st.title("💎 AuraCoin Live Dashboard")
st.write("---")

# جلب آخر رصيد تم تسجيله في الجدول
def get_aura_balance():
    try:
        # جلب آخر سطر تم إضافته للجدول
        result = supabase.table("mining_stats").select("balance").order("created_at", desc=True).limit(1).execute()
        if result.data:
            return result.data[0]['balance']
        return "1,000,000" # رقم افتراضي
    except:
        return "1,000,000"

balance = get_aura_balance()
st.metric(label="Total Aura Mined", value=f"{balance} AC")

# تحديث الصفحة تلقائياً كل 10 ثواني
time.sleep(10)
st.rerun()
