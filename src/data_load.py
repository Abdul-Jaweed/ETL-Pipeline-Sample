import boto3
from io import StringIO
import os
from src.config import Config

class AWSS3Loader:
    def __init__(self):
        self.s3_client = boto3.client('s3')
        self.bucket_name = Config.AWS_S3_BUCKET_NAME

    def save_data(self, data, file_path):
        content = data.to_csv(index=False)
        file_name = os.path.basename(file_path)
        s3_key = f"{file_name}"

        self.s3_client.put_object(
            Bucket=self.bucket_name,
            Key=s3_key,
            Body=content.encode('utf-8')
        )
        print(f"{file_name} saved to S3 bucket")
