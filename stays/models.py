from django.db import models

import os
import sys
from django.conf import settings

project_name = settings.BASE_DIR








# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from ..clrAdmins.models import Room

class Stay(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    adults_num = models.IntegerField(default=1)
    children_num = models.IntegerField(default=0)
    room_id = models.ForeignKey(Room)
    coupon_code = models.CharField(max_length=100, blank=True, null=True)

# the below will be Room model. It will have the following fields: name, "serverName": "DORMITORY_2",
        # "ui_name": "Dormitory #2",
        # "description": "the description of the room goes here",
        # "img_path": "/images/bedImgs/dorm1.jpeg",
        # "amenities": [
        #     "wifi",
        #     "Family",
        #     "Bathroom",
        #     "Closet",
        #     "Bathroom"
        # ]

