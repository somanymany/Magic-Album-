from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include, re_path as url


from rest_framework import routers

from hbws import settings

router = routers.DefaultRouter()

from xinwen.views import XinwenView
from xinwen import urls

from newposts.views import NewPostsView , SIMDPostsView , SimdFilesViews

from hbws.settings import MEDIA_ROOT
from django.views.static import serve
"""
    key webpage
"""
from newposts.views import NewCategoryView

"""
    foreign webpage
"""
from newposts.views import NewsPostsView



router.register(r'xinwen',XinwenView,basename='xinwen')
router.register(r'newposts',NewPostsView,basename="newposts")
router.register(r'simdposts',SIMDPostsView,basename="simdposts")
router.register(r'simdfiles',SimdFilesViews,basename="simdfiles")
router.register(r'category',NewCategoryView,basename='category')
router.register(r'newpost',NewsPostsView,basename='newpost')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('simditor/', include('simditor.urls')),
    path('',include(router.urls)),#although in Django3 must use path to write address,but Get Images should using url
    url(r'^upimg/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),
    url(r'^api/',include('hbws_back.urls')), #from this url to get all prog
    #url(r'^shangchuan/',include('xinwen.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

#the static need import urls.static and write path in settings . must notice it