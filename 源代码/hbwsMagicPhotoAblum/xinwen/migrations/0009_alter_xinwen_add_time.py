# Generated by Django 4.1.1 on 2022-10-09 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xinwen', '0008_alter_xinwen_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xinwen',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 10, 0, 45, 20, 808872), verbose_name='Add_Time'),
        ),
    ]
