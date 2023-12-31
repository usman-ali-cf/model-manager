# Generated by Django 4.2.4 on 2023-08-22 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pApp', '0004_author_book_publisher_store_book_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('salary', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
