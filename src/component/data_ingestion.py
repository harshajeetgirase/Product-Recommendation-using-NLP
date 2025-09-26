import os 
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from pathlib import Path

class DataIngestion:
    def __init__(self, input_path: str, output_path: str = "artifacts/raw.csv"):
        self.input_path = input_path
        self.output_path = output_path

    def load_data(self) -> pd.DataFrame:
        try:
            logging.info(f"Loading data from {self.input_path}")
            df = pd.read_csv(self.input_path)

            # Save a raw copy
            os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
            df.to_csv(self.output_path, index=False)
            logging.info(f"Raw data saved at {self.output_path} with shape {df.shape}")

            return df
        except Exception as e:
            raise CustomException(e, sys)


# if __name__ == "__main__":
#     input_path = Path.home() / "Desktop" / "00Recomm" / "Data" / "Major.csv"
#     data_ingestion = DataIngestion(input_path=input_path)
#     df = data_ingestion.load_data()
#     print("Yes")