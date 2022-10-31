# Generated by Django 4.1.1 on 2022-10-10 15:53

import datetime
from django.db import migrations, models
import simditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newposts', '0005_simdposts_add_time_alter_newposts_add_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='simdFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='File Name')),
                ('file', models.FileField(upload_to='file_url/', verbose_name='File upload address')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2022, 10, 10, 23, 53, 58, 318852), verbose_name='File added time')),
            ],
        ),
        migrations.AlterField(
            model_name='newposts',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 10, 23, 53, 58, 317851), verbose_name='Add_Time'),
        ),
        migrations.AlterField(
            model_name='newposts',
            name='content',
            field=simditor.fields.RichTextField(verbose_name='basic rich text'),
        ),
        migrations.AlterField(
            model_name='simdposts',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 10, 23, 53, 58, 318852), verbose_name='simd_Add_Time'),
        ),
        migrations.AlterField(
            model_name='simdposts',
            name='all_content',
            field=simditor.fields.RichTextField(verbose_name='simdposts rich text'),
        ),
    ]
