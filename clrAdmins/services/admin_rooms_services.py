import os

import boto3

from datetime import datetime
from stays.models import Stay
from decouple import config
from django.core.files.uploadedfile import UploadedFile
from typing import Dict



def add_rooms():
    pass


def upload_photos(files: Dict[str, UploadedFile]):
    # GOAL: save the files onto the server 


    session = boto3.Session(aws_access_key_id=config('AWS_ACCESS_KEY'), aws_secret_access_key=config('AWS_SECRET_KEY'))
    aws_S3 = session.resource('s3')
    # aws_S3.meta.client.upload_file
    
    

def edit_rooms():
    pass