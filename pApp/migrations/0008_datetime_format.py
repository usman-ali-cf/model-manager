# Generated by Django 4.2.4 on 2023-09-01 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pApp', '0007_datetime_remove_book_authors_remove_book_publisher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datetime',
            name='format',
            field=models.CharField(default='PST', null=True),
        ),
    ]
