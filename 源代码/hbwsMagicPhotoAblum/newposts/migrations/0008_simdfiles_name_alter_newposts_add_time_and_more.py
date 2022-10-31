# Generated by Django 4.1.1 on 2022-10-10 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newposts', '0007_simdfiles_img_alter_newposts_add_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='simdfiles',
            name='name',
            field=models.CharField(default='lzhenz', max_length=100, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='newposts',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 0, 19, 9, 458526), verbose_name='Add_Time'),
        ),
        migrations.AlterField(
            model_name='simdfiles',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 0, 19, 9, 458526), verbose_name='File added time'),
        ),
        migrations.AlterField(
            model_name='simdposts',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 0, 19, 9, 458526), verbose_name='simd_Add_Time'),
        ),
    ]
