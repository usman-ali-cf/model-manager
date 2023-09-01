import logging
from datetime import datetime
from pytz import timezone
from .models import DateTime as datemodel


index = 0
current_status = 'UTC'


def my_cron_job():
    global index, current_status
    from .models import DateTime
    if index < 100 and current_status == 'UTC':
        date_objects = DateTime.objects.all().order_by('id')
        objects = date_objects[index:index + 10]
        index += 10
        for object in objects:
            date = datetime.now(timezone('UTC'))
            object.time = date
            object.format = "UTC"
            object.save()
    if index < 100 and current_status == 'PTC':
        date_objects = DateTime.objects.all().order_by('id')
        objects = date_objects[index:index + 10]
        index += 10
        for object in objects:
            date = datetime.now(timezone('Asia/Karachi'))
            object.time = date
            object.format = "PTC"
            object.save()
    if index > 100:
        index = 0
        if current_status == "UTC":
            current_status = "PTC"
        else:
            current_status = "UTC"
