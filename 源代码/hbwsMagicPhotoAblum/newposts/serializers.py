from rest_framework import  serializers
from .models import newposts
from .models import simdposts , simdfiles , NewsCategory ,NewsPosts
class NewPostsSerializers(serializers.ModelSerializer):
    class Meta:
        model = newposts
        fields = ["title","add_time","content","all_content"]

class SIMDPostsSerializers(serializers.ModelSerializer):
    class Meta:
        model = simdposts
        fields = ["title","all_content","add_time"]

class SimdFilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = simdfiles
        fields = ["title","name","img","file","add_time","get_ceshi_display"]



class NewsPostsSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsPosts
        fields = "__all__"

class NewsCategorySerializers(serializers.ModelSerializer):
    # for
    posts = NewsPostsSerializers(many=True)
    class Meta:
        model = NewsCategory
        fields = "__all__"

