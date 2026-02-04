# -*- coding: utf-8 -*-
import streamlit as st

st.set_page_config(page_title="AuraCoin", layout="wide")

# كود لعرض المليون AuraCoin بدون مشاكل لغة
st.title("AuraCoin Dashboard")
st.write("---")
st.metric(label="Total Balance", value="1,000,000 AC")
st.success("Congratulations! 1 Million Aura reached.")

# إضافة كود بسيط لمنع أخطاء الترميز المستقبيلة
st.info("System Status: Online")
