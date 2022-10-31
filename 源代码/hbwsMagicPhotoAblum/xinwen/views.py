from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import base64

from .serializers import XinwenSerializer
from .models import xinwen
# both of these imports are just created

# mixins  are not used in early stages
from rest_framework import  viewsets ,mixins,status

class XinwenView(viewsets.ModelViewSet):

    serializer_class = XinwenSerializer
    def get_queryset(self):
        return xinwen.objects.all()


class Image_ConvertView(APIView):
    def post(self, request, *args, **kwargs):
        #image2base64 = request.data.get('myImage')
        # temple = request.data.get('targetValue1')
        temple = 2
        import cv2
        import numpy as np
        import base64

        # b64_de_img = base64.b64decode(image2base64[-1])
        # np_arr = np.fromstring(b64_de_img, np.uint8)
        # c_img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # if temple == 2:
        #
        #     x = cv2.Sobel(c_img, cv2.CV_16S, 1, 0)
        #     y = cv2.Sobel(c_img, cv2.CV_16S, 0, 1)
        #
        #     absX = cv2.convertScaleAbs(x)
        #     absY = cv2.convertScaleAbs(y)
        #
        #     dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

        # elif temple == 1:
        #
        #     img = cv2.GaussianBlur(c_img, (3, 3), 0)
        #     canny = cv2.Canny(img, 50, 150)
        #     dst = canny
        # elif temple == 0:
        #
        #     gray_lap = cv2.Laplacian(c_img, cv2.CV_16S, ksize=3)
        #     dst = cv2.convertScaleAbs(gray_lap)

        # b64_img = cv2.imencode('.jpg', dst)[1].tostring()
        # b64_img = base64.b64encode(b64_img)
        return Response({'status': True})

