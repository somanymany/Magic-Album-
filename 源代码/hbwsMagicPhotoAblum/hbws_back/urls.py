from django.contrib import admin
from django.urls import re_path as url,include
from . import  views

urlpatterns = [
    url(r'^uploadImage/',views.uploadImageView.as_view()),
    url(r'^Campus_Graduation/',views.Campus_Graduation.as_view()),
    url(r'^NothingView/',views.NothingView.as_view()),
    url(r'^Ancient_Magic/',views.Ancient_Magic.as_view()),
    url(r'^Weird_Magic/',views.Weird_Magic.as_view()),
    url(r'^Animation_Magic/',views.Animation_Magic.as_view()),
    url(r'^DisneyStyle_face/',views.DisneyStyle_face.as_view()),
    url(r'^MiyazakiHayao_style/',views.MiyazakiHayao_style.as_view())
]