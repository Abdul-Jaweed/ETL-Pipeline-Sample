import pandas as pd
import os

class DataTransformer:
    @staticmethod
    def transform(data):
        data['height'] = round(data['height'] * 0.0254, 2)
        data['weight'] = round(data['weight'] * 0.45359237, 2)
        return data
    
    @staticmethod
    def save_transformed_data(transformed_data):
        # Create a directory if it doesn't exist
        transformed_dir = "data_transformed"
        if not os.path.exists(transformed_dir):
            os.makedirs(transformed_dir)
        
        # Save the transformed data to the data_transformed directory
        transformed_file = os.path.join(transformed_dir, "transformed_data.csv")
        transformed_data.to_csv(transformed_file, index=False)
        print(f"Transformed data saved to {transformed_file}")
