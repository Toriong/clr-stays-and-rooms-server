from datetime import datetime
from stays.models import Stay
import os
import boto3



def add_rooms():
    pass


def upload_photos():
    # GOAL: upload the photos into google cloud storage 
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
    aws_S3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

    print('aws_S3: ', aws_S3)
    


def edit_rooms():
    pass