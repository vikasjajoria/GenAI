import streamlit as st

st.title("Product Form")

# Sidebar inputs
st.sidebar.header("Add New Product")

product_name = st.sidebar.text_input("Product Name")

category = st.sidebar.selectbox(
    "Category",
    ["Electronics", "Clothing", "Groceries", "Books", "Toys"]
)

price = st.sidebar.number_input("Price", min_value=0.0, step=0.5, format="%.2f")

add_clicked = st.sidebar.button("Add Product")

# Main area
if add_clicked:
    if product_name.strip() == "":
        st.error("Please enter a product name before adding.")
    else:
        st.success("Product added successfully!")

        st.subheader("Product Details")
        st.markdown(f"""
        - **Name:** {product_name}
        - **Category:** {category}
        - **Price:** ${price:.2f}
        """)
else:
    st.info("Fill in the product details in the sidebar and click 'Add Product'.")