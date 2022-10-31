from django.shortcuts import render

from .serializers import NewPostsSerializers , SIMDPostsSerializers , SimdFilesSerializers ,NewsCategorySerializers,NewsPostsSerializers
from .models import newposts , simdposts , simdfiles , NewsCategory ,NewsPosts

from rest_framework import viewsets

class NewPostsView(viewsets.ModelViewSet):
    serializer_class =  NewPostsSerializers
    def get_queryset(self):
        return newposts.objects.all()

class SIMDPostsView(viewsets.ModelViewSet):
    serializer_class = SIMDPostsSerializers
    def get_queryset(self):
        return simdposts.objects.all()


class SimdFilesViews(viewsets.ModelViewSet):
    serializer_class = SimdFilesSerializers
    def get_queryset(self):
        return simdfiles.objects.all()

class NewCategoryView(viewsets.ModelViewSet):
    serializer_class = NewsCategorySerializers

    def get_queryset(self):
        return NewsCategory.objects.all()

class NewsPostsView(viewsets.ModelViewSet):
    serializer_class = NewsPostsSerializers
    def get_queryset(self):
        return NewsPosts.objects.all()