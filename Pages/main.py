import streamlit as st

def main():
    st.subheader("Welcome to the Recommendation Engine!")
    st.write("This is a demo of the recommendation logic. It would typically read your product data and run a recommendation algorithm here.")

    # Simple demo of recommendation input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        st.selectbox("Select a Category", ["Laptops", "Mobiles", "Headphones"])
    with col2:
        st.selectbox("Select a Brand", ["Apple", "Samsung", "Sony"])
    with col3:
        st.text_input("Enter Product Name")

    st.button("Get Recommendations")

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.success("Your recommendations will appear here!")

    # Add some dummy content to make this tab a bit taller
    for i in range(10):
        st.info(f"Recommendation for you: Product {i+1}")
