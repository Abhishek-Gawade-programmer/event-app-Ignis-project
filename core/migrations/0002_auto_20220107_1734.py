# Generated by Django 3.2.9 on 2022-01-07 17:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 7, 17, 34, 29, 603631, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Describe Your Event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='event_images', verbose_name='Event Image'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=150, verbose_name='Location Of Event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Name Of Event'),
        ),
    ]
