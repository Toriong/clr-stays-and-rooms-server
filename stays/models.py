from django.db import models

# Create your models here.
class Stay(models.Model):
    startDate = models.IntegerField()
    endDate = models.IntegerField()
    adultsNum = models.IntegerField(default=1)
    childrenNum = models.IntegerField(default=0)
    roomType = models.CharField(max_length=100)
    couponCode = models.CharField(max_length=100, blank=True, default=None)