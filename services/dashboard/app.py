# app.py
# داشبورد مدیریتی با Streamlit

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="سامانه سلامت زنجیره اروند", layout="wide")

st.title("سامانه سلامت زنجیره کلرآلکالی تا پی‌وی‌سی")
st.markdown("پایش سلامت سلول‌های الکترولیز و پیش‌بینی فولینگ راکتورهای پلیمریزاسیون")

# داده نمونه
data = pd.DataFrame({
    "زمان": pd.date_range(start="2026-09-14", periods=100, freq="H"),
    "ولتاژ سلول": np.random.normal(3.05, 0.02, 100),
    "راندمان جریان": np.random.normal(96.5, 0.3, 100),
    "ضریب انتقال حرارت": np.random.normal(850, 15, 100),
})

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("ولتاژ سلول", f"{data['ولتاژ سلول'].iloc[-1]:.3f} V", delta="-0.001")

with col2:
    st.metric("راندمان جریان", f"{data['راندمان جریان'].iloc[-1]:.2f} %", delta="-0.05")

with col3:
    st.metric("ضریب انتقال حرارت", f"{data['ضریب انتقال حرارت'].iloc[-1]:.1f}", delta="-2.0")

st.subheader("روند ولتاژ سلول")
st.line_chart(data.set_index("زمان")["ولتاژ سلول"])

st.subheader("روند راندمان جریان")
st.line_chart(data.set_index("زمان")["راندمان جریان"])

st.subheader("روند ضریب انتقال حرارت")
st.line_chart(data.set_index("زمان")["ضریب انتقال حرارت"])
