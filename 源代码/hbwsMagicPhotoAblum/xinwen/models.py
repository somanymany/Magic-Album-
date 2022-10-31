from django.db import models
from datetime import datetime

class xinwen(models.Model):
    biaoti = models.CharField(max_length=100,verbose_name=u"Title")
    zuozhe = models.CharField(max_length=20,verbose_name=u"Author")
    neirong = models.CharField(max_length=1000,verbose_name=u"Content")
    img_url = models.ImageField(upload_to='img_url/',verbose_name=u"Image address")
    add_time = models.DateTimeField(default=datetime.now(),verbose_name=u"Add_Time")
