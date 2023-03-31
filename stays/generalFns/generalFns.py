from datetime import datetime
from django.utils.timezone import make_aware

def makeDateTimeZoneAware(dateTime: str) -> datetime:
    dateTimeDict = datetime.strptime(dateTime, "%Y-%m-%d")

    return make_aware(dateTimeDict)
    