# Generated by Django 4.1.1 on 2022-10-05 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='xinwen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biaoti', models.CharField(max_length=100)),
                ('zuozhe', models.CharField(max_length=20)),
                ('neirong', models.CharField(max_length=1000)),
            ],
        ),
    ]
