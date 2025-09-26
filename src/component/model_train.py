import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.logger import logging
from src.exception import CustomException
import sys

# Import your DataIngestion class
from component.data_ingestion import DataIngestion


def train_model(output_dir="artifacts", input_path="artifacts/cleaned_data.csv"):
    try:
        logging.info("Starting model training...")

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Initialize DataIngestion with input path
        ingestion = DataIngestion(input_path=input_path)
        df = ingestion.load_data()  # returns cleaned dataframe

        if 'clean_name' not in df.columns:
            raise ValueError("Column 'clean_name' not found in dataframe")

        # TF-IDF vectorization + cosine similarity
        tfidf = TfidfVectorizer(stop_words="english")
        tfidf_matrix = tfidf.fit_transform(df['clean_name'])
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

        # Save models
        with open(os.path.join(output_dir, "cosine_sim.pkl"), "wb") as f:
            pickle.dump(cosine_sim, f)
        with open(os.path.join(output_dir, "vectorizer.pkl"), "wb") as f:
            pickle.dump(tfidf, f)

        logging.info(f"Model training complete. Artifacts saved in '{output_dir}'.")
        return cosine_sim

    except Exception as e:
        logging.error("Error in model training")
        raise CustomException(e, sys)


# if __name__ == "__main__":
#     train_model(
#         output_dir="artifacts",
#         input_path="artifacts/cleaned_data.csv"  # path to your raw data
#     )

