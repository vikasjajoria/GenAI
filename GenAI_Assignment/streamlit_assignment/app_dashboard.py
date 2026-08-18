import streamlit as st

st.title("Simple Sales Dashboard")
st.write("A quick overview of monthly sales performance.")

months = ["January", "February", "March", "April"]

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

selected_month = st.selectbox("Select a month", months)

st.metric(label=f"Sales in {selected_month}", value=sales[selected_month])

st.subheader("Monthly Sales Overview")
st.bar_chart(list(sales.values()))