# Generated by Django 4.1.1 on 2022-10-10 16:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newposts', '0010_newscategory_newsposts_alter_newposts_add_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsposts',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='newposts.newscategory', verbose_name='category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newposts',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 0, 44, 21, 803090), verbose_name='Add_Time'),
        ),
        migrations.AlterField(
            model_name='newscategory',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 0, 44, 21, 804073), verbose_name='news release time'),
        ),
        migrations.AlterField(
            model_name='newsposts',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 0, 44, 21, 804073), verbose_name='simd_Add_Time'),
        ),
        migrations.AlterField(
            model_name='simdfiles',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 0, 44, 21, 804073), verbose_name='File added time'),
        ),
        migrations.AlterField(
            model_name='simdposts',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 0, 44, 21, 804073), verbose_name='simd_Add_Time'),
        ),
    ]
