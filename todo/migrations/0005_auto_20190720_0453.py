# Generated by Django 2.2.3 on 2019-07-19 22:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20190227_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 19, 22, 53, 39, 855049, tzinfo=utc)),
        ),
    ]