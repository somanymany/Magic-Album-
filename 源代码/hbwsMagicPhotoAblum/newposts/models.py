from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from simditor.fields import RichTextField

class newposts(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"Title")
    content = RichTextField(verbose_name=u"basic rich text")
    all_content = RichTextUploadingField(verbose_name=u"fruitful rich text")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name=u"Add_Time")

class simdposts(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"Title")
    all_content = RichTextField(verbose_name=u"simdposts rich text")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name=u"simd_Add_Time")

class simdfiles(models.Model):
    # default optional parameters  the left imf is truth choice , and the right is describing content
    CESHI = (
        ('1', 'Original Content'),
        ('2', 'not Original'),
        ('3', 'bu zhi dao')
    )

    title = models.CharField(max_length=100, verbose_name=u"File Name")
    name = models.CharField(max_length=100,default="lzhenz",verbose_name=u"author")
    #null and blank setting the attruites should be null
    img = models.ImageField(upload_to='file_url/',null=True,blank=True,verbose_name=u"Image Upload address")
    file = models.FileField(upload_to='file_url/',verbose_name=u"File upload address")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name=u"File added time")
    ceshi = models.CharField(choices=CESHI,default='1',max_length=50,verbose_name=u"default optional parameters")


"""
    this is a key 
"""

class NewsCategory(models.Model):
    """
        news category
    """
    name = models.CharField(max_length =30,verbose_name=u"new category")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name=u"news release time")

    class Meta:
        verbose_name = "News Category"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.name



class NewsPosts(models.Model):
    """
     news contents webpage
    """
    title = models.CharField(max_length=100, null=True,blank=True,verbose_name=u"Title")
    all_content = RichTextField(verbose_name=u"simdposts rich text")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name=u"simd_Add_Time")
    category = models.ForeignKey(NewsCategory,on_delete=models.CASCADE,verbose_name=u"category",related_name="posts")
