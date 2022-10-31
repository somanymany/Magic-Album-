from xinwen.views import Image_ConvertView
from django.urls import path,include, re_path as url
from . import views
urlpatterns = [
    url(r'^uploadImage/',views.Image_ConvertView.as_view()),
]