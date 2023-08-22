from src.data_extractor import DataDownloaderExtractor

def main():

    print("Data Extaction Started")
    data_processor = DataDownloaderExtractor()
    data_processor.download_and_extract()
    extracted_data = data_processor.extract()
    print(extracted_data)


if __name__ == "__main__":
    main()
