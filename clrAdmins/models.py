from django.db import models


class Room(models.Model):
    _id = models.CharField(primary_key=True, max_length=255)
    ui_name = models.CharField(max_length=180)
    description = models.CharField(max_length=200)
    img_path: models.CharField(max_length=255, unique=True)
    amenities = models.CharField(max_length=1000)
    # a party of five plus can use this room 
    is_dorm = models.BooleanField(default=False)
    aws_photo_ids = models.CharField(max_length=2000, default='[]')