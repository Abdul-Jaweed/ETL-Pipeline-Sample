from src.data_extractor import DataDownloaderExtractor
from src.data_transform import DataTransformer
import os

def main():

    print("")
    print("Data Extaction Started")
    print("")
    data_processor = DataDownloaderExtractor()
    data_processor.download_and_extract()
    extracted_data = data_processor.extract()
    print(extracted_data)

    print("")
    print("")
    print("Data Transformation Started")
    print("")
    data_transformer = DataTransformer()
    transformed_data = data_transformer.transform(extracted_data)
    data_transformer.save_transformed_data(transformed_data)
    print(transformed_data)



if __name__ == "__main__":
    main()
