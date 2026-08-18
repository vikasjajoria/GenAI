# ---------price calculator-----------

import streamlit as st

st.title("Price Calculator")

price = st.number_input("Enter Product price",min_value=0.0)

discount= st.slider("Select Discount(%)",0,50,10)

if st.button("Calculate Discount"):
    discount_amount = price * discount/100

    final_price = price - discount_amount

    st.success(f"Final Price: {final_price}")

    table = [
        ["Before", price],
        ["After", final_price]
    ]

    st.table(table)