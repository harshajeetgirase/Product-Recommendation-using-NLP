# pages/demo.py
import streamlit as st
import pandas as pd
from src.component.recommender import recommendor_input

def main():
    # Load cleaned data
    cleaned_csv_path = "artifacts/cleaned_data.csv"
    df_cleaned = pd.read_csv(cleaned_csv_path)

    st.title("🛒 Product Recommendation System")

    st.markdown("### 🎯 Filter Products")

    # --- Input filters inside page content (no sidebar) ---
    col1, col2 = st.columns(2)
    with col1:
        category = st.selectbox(
            "Select Category (optional)", 
            options=[""] + [
                'headphones and earphones', 'Laptop Bag', 'Laptop Charges',
                'Laptop', 'Laptop Cooling Pad', 'Mobile', 'Mobile Charge',
                'Mobiles', 'Mobile Covers', 'Smart Tv'
            ]
        )
    with col2:
        def brand_category(category):
            brand_type = df_cleaned[df_cleaned['Category'] == category.title()]['Brand'].unique().tolist()
            return brand_type

        brand = st.selectbox("Select Brand (optional)", options=[""] + brand_category(category))

    product = st.text_input("Enter Product Name (required)")
    top_n = st.number_input("Number of Recommendations", min_value=1, max_value=50, value=5)

    # --- Display product card function ---
    def display_product_card(product):
        st.markdown("---")
        st.subheader(product['Product Name'])
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write(f"**Brand:** {product['Brand']}")
            st.write(f"**Category:** {product['Category']}")
        with col2:
            st.write(f"💰 Discount: {product['Discount Price']} | Original: {product['Original Price']}")
            if product.get("Flipkart_Link"):
                st.markdown(f"[🔗 View on Flipkart]({product['Flipkart_Link']})")

        image_url = product.get("Image_URL", "")
        if image_url and image_url.startswith("https"):
            st.image(image_url, width=200)
        else:
            st.image("https://via.placeholder.com/200x200.png?text=No+Image", width=200)

    # --- Button to get recommendations ---
    if st.button("🚀 Get Recommendations"):
        if not product:
            st.error("❌ Product name is required.")
        else:
            recommendations = recommendor_input(
                brand=brand,
                category=category,
                product=product,
                top_n=top_n
            )
            if recommendations:
                st.subheader("🔎 Top Recommendations")
                for rec in recommendations:
                    display_product_card(rec)
            else:
                st.error("❌ No recommendations found.")



# if __name__ == "__main__":
#     main()