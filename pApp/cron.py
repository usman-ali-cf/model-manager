from datetime import datetime
from pytz import timezone


def my_cron_job():
    from .models import DateTime, DateTimezone
    date_timezone = DateTimezone.objects.first()

    if date_timezone.zone == 'UTC':
        all_object = DateTime.objects.filter(format="PST").order_by('time_id').first()
        if all_object is not None:
            all_objects = DateTime.objects.all().order_by('time_id')
            index = all_object.time_id - 1
            selected_objects = all_objects[index:index + 10]
            for object in selected_objects:
                date = datetime.now(timezone('UTC'))
                object.time = date
                object.format = "UTC"
                object.save()
        else:
            date_timezone.zone = "PST"
            date_timezone.save()

    if date_timezone.zone == 'PST':
        all_object = DateTime.objects.filter(format="UTC").order_by('time_id').first()
        if all_object is not None:
            all_objects = DateTime.objects.all().order_by('time_id')
            index = all_object.time_id - 1
            selected_objects = all_objects[index:index + 10]
            for object in selected_objects:
                date = datetime.now(timezone('Asia/Karachi'))
                object.time = date
                object.format = "PST"
                object.save()
        else:
            date_timezone.zone = "UTC"
            date_timezone.save()
