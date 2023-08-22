import os
import requests
import zipfile
from dotenv import load_dotenv

class DataDownloaderExtractor:
    def __init__(self):
        load_dotenv()
        self.zip_url = os.getenv("ZIP_URL")
        self.target_dir = "extracted_data"
        self.zip_filename = os.path.join(self.target_dir, "source.zip")
        self.extracted_dir = os.path.join(self.target_dir, "extracted_data")
    
    def download_data(self):
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)
        
        if not os.path.exists(self.zip_filename):
            print("Downloading the zip file...")
            response = requests.get(self.zip_url)
            with open(self.zip_filename, "wb") as f:
                f.write(response.content)
            print("Zip file downloaded.")
        else:
            print("Zip file already exists.")
    
    def extract_data(self):
        if not os.path.exists(self.extracted_dir):
            print("Extracting the data...")
            with zipfile.ZipFile(self.zip_filename, "r") as zip_ref:
                zip_ref.extractall(self.extracted_dir)
            print("Data extracted.")
        else:
            print("Data already extracted.")
    
    def download_and_extract(self):
        self.download_data()
        self.extract_data()
        print("Data download and extraction completed.")

# data_processor = DataDownloaderExtractor()
# data_processor.download_and_extract()
