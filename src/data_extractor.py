import os
import requests
import zipfile
import pandas as pd
import glob
import xml.etree.ElementTree as ET
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
    
    def extract_from_csv(self, file_to_process):
        return pd.read_csv(file_to_process)
    
    def extract_from_json(self, file_to_process):
        return pd.read_json(file_to_process, lines=True)
    
    def extract_from_xml(self, file_to_process):
        data = []
        tree = ET.parse(file_to_process)
        root = tree.getroot()
        for person in root:
            name = person.find("name").text
            height = float(person.find("height").text)
            weight = float(person.find("weight").text)
            data.append({"name": name, "height": height, "weight": weight})
        return pd.DataFrame(data)
    
    def extract(self):
        extracted_data = pd.DataFrame(columns=['name', 'height', 'weight'])
        
        for csvfile in glob.glob(os.path.join(self.extracted_dir, "*.csv")):
            extracted_data = pd.concat([extracted_data, self.extract_from_csv(csvfile)], ignore_index=True)

        for jsonfile in glob.glob(os.path.join(self.extracted_dir, "*.json")):
            extracted_data = pd.concat([extracted_data, self.extract_from_json(jsonfile)], ignore_index=True)

        for xmlfile in glob.glob(os.path.join(self.extracted_dir, "*.xml")):
            extracted_data = pd.concat([extracted_data, self.extract_from_xml(xmlfile)], ignore_index=True)

        return extracted_data
    
    def download_and_extract(self):
        self.download_data()
        self.extract_data()
        print("Data download and extraction completed.")



# data_processor = DataDownloaderExtractor()
# data_processor.download_and_extract()
# extracted_data = data_processor.extract()
# print(extracted_data)
