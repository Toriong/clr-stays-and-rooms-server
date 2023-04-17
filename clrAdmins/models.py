from django.db import models




class Room(models.Model):
    _id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=180)
    description = models.CharField(max_length=200)
    # this will be displayed when the user searches for the rooms in the search bar
    main_img = models.CharField(max_length=255, unique=True)
    amenities = models.CharField(max_length=1000)
    # a party of five plus can use this room 
    is_dorm = models.BooleanField(default=False)
    aws_photo_ids = models.CharField(max_length=2000, default='[]')