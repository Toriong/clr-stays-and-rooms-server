from django.db import models

# Create your models here.
class Stay(models.Model):
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    adultsNum = models.IntegerField(default=1)
    childrenNum = models.IntegerField(default=0)
    roomName = models.CharField(max_length=100)
    couponCode = models.CharField(max_length=100, blank=True, null=True)


