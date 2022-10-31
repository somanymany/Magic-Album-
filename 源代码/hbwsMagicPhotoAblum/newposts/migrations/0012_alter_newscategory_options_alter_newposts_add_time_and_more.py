# Generated by Django 4.1.2 on 2022-10-14 16:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("newposts", "0011_newsposts_category_alter_newposts_add_time_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="newscategory",
            options={
                "verbose_name": "News Category",
                "verbose_name_plural": "News Category",
            },
        ),
        migrations.AlterField(
            model_name="newposts",
            name="add_time",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 15, 0, 44, 3, 885968),
                verbose_name="Add_Time",
            ),
        ),
        migrations.AlterField(
            model_name="newscategory",
            name="add_time",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 15, 0, 44, 3, 886970),
                verbose_name="news release time",
            ),
        ),
        migrations.AlterField(
            model_name="newsposts",
            name="add_time",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 15, 0, 44, 3, 886970),
                verbose_name="simd_Add_Time",
            ),
        ),
        migrations.AlterField(
            model_name="newsposts",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="newposts.newscategory",
                verbose_name="category",
            ),
        ),
        migrations.AlterField(
            model_name="simdfiles",
            name="add_time",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 15, 0, 44, 3, 885968),
                verbose_name="File added time",
            ),
        ),
        migrations.AlterField(
            model_name="simdposts",
            name="add_time",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 15, 0, 44, 3, 885968),
                verbose_name="simd_Add_Time",
            ),
        ),
    ]
