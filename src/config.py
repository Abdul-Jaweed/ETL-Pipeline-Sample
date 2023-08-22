import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AWS_S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")
