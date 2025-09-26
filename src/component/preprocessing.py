import re
import os
import sys
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from src.logger import logging
from src.exception import CustomException
from component.data_ingestion import DataIngestion

def clean_text(text):
    try:
        text = str(text).lower()
        text = re.sub(r"[^a-z0-9\s]", "", text)  # keep letters + numbers
        tokens = text.split()
        tokens = [t for t in tokens if t not in stopwords.words("english")]
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(t) for t in tokens]
        return " ".join(tokens)
    except Exception as e:
        logging.error(f"Error cleaning text: {text}")
        raise CustomException(e, sys)

def preprocess_data(input_path="artifacts/raw.csv", output_dir="artifacts", save_clean_csv=True):
    """
    Loads raw data, cleans 'Product Name', saves cleaned CSV, and returns the cleaned dataframe.
    """
    try:
        logging.info("Starting data preprocessing...")

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Load raw data
        ingestion = DataIngestion(input_path=input_path)
        df = ingestion.load_data()
        logging.info(f"Raw data loaded successfully with {len(df)} records.")

        # Check if Product Name column exists
        if "Product Name" not in df.columns:
            raise ValueError("Column 'Product Name' not found in data.")

        # Apply text cleaning
        df["clean_name"] = df["Product Name"].apply(clean_text)
        logging.info("Text cleaning completed for 'Product Name' column.")

        # Save cleaned data as CSV
        if save_clean_csv:
            clean_csv_path = os.path.join(output_dir, "cleaned_data.csv")
            df.to_csv(clean_csv_path, index=False)
            logging.info(f"Cleaned data saved as CSV at '{clean_csv_path}'.")

        # return df

    except Exception as e:
        logging.error("Error during preprocessing.")
        raise CustomException(e, sys)


# if __name__ == "__main__":
#     preprocess_data(
#         input_path="artifacts/raw.csv",  # path to your raw data
#         output_dir="artifacts"
#     )