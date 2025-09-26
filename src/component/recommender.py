import pandas as pd
import pickle
from src.logger import logging
from src.exception import CustomException
import sys

def recommendor_input(df=None, cosine_sim=None, brand="", category="", product="", top_n=5):
    """
    Recommend products based on brand, category, and product name.
    Ensures recommendations belong to the same brand/category if provided.
    Removes duplicates even if cosine similarity is the same.
    """
    try:
        # Load artifacts if not provided
        if df is None:
            df = pd.read_csv("artifacts/cleaned_data.csv")
        if cosine_sim is None:
            with open("artifacts/cosine_sim.pkl", "rb") as f:
                cosine_sim = pickle.load(f)

        if not product:
            logging.warning("No product name provided to recommender_input.")
            return []

        # Match product name (partial match allowed)
        matched_products = [p for p in df['clean_name'].values if product.lower() in p.lower()]
        if not matched_products:
            logging.info(f"No matching product found for input: {product}")
            return []

        # Take first matched product
        matched_product = matched_products[0]
        product_index = df[df['clean_name'] == matched_product].index[0]

        # Get similarity scores
        similarity_list = list(cosine_sim[product_index])
        ranked_products = sorted(
            enumerate(similarity_list),
            key=lambda x: x[1],
            reverse=True
        )[0:]  # exclude self

        # Build recommendation list
        recommendations = []
        seen_products = set()  # to avoid duplicates

        for idx, _ in ranked_products:
            candidate = df.iloc[idx]

            # Enforce brand and category filters
            if brand and candidate["Brand"] != brand:
                continue
            if category and candidate["Category"].lower() != category.lower():
                continue

            # Skip duplicate products
            if candidate["Product Name"] in seen_products:
                continue

            rec = {
                "Product Name": candidate["Product Name"],
                "Brand": candidate["Brand"],
                "Category": candidate["Category"],
                "Discount Price": candidate["Discount_price"],
                "Original Price": candidate["Original_price"],
                "Image_URL": candidate.get("Image_url", ""),
                "Flipkart_Link": candidate.get("Url", "")
            }
            recommendations.append(rec)
            seen_products.add(candidate["Product Name"])

            # Stop when enough unique recommendations are collected
            if len(recommendations) >= top_n:
                break

        if not recommendations:
            logging.info(f"No recommendations generated for product: {product}")

        return recommendations

    except Exception as e:
        logging.error(f"Error in recommendor_input: {e}")
        raise CustomException(e, sys)
