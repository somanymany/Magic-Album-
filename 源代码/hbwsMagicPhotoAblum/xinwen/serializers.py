
from rest_framework import serializers
from .models import xinwen

#if you want add a new function views,just add fields in here
class XinwenSerializer(serializers.ModelSerializer):
    class Meta:
        model = xinwen
        fields = ["biaoti","zuozhe","neirong","img_url","add_time"]
