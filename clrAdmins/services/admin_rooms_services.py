import os

import boto3
import uuid

from datetime import datetime
from stays.models import Stay
from decouple import config
from django.core.files.uploadedfile import UploadedFile
from typing import Dict
from ..customTypes import Upload_File_AWS_Result



def add_rooms():
    pass


def upload_photos(files: Dict[str, UploadedFile]) -> Upload_File_AWS_Result:
    try: 
        session = boto3.Session(aws_access_key_id=config('AWS_ACCESS_KEY'), aws_secret_access_key=config('AWS_SECRET_KEY'))
        aws_S3 = session.resource('s3')

        for file in files.getlist('files'):
            file_name = f'{uuid.uuid4()}-{file.name}'
            aws_S3.meta.client.upload_fileobj(file, config('AWS_STORAGE_BUCKET_NAME'), file_name)

        return Upload_File_AWS_Result(msg="Photos were uploaded successfully.", wasSuccessful=True)
    except Exception as error:
        print("An error has occurred while uploading a photo to AWS S3: ", error)

        return Upload_File_AWS_Result(msg="An error has occurred while uploading a photo to AWS S3.", wasSuccessful=False)
    

def edit_rooms():
    pass