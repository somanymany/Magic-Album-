import os.path,io,os,argparse,torch,base64,test_fun,json

from PIL import Image
from model import Generator
from django.http import HttpResponse
from rest_framework.views import APIView
from tencentcloud.common import credential
from rest_framework.response import Response
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from torchvision.transforms.functional import to_tensor, to_pil_image
from tencentcloud.facefusion.v20181201 import facefusion_client, models
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException


#Animation Style Photo-nonHuman
class Animation_Magic(APIView):
    def load_image(image_path, x32=False):
        img = Image.open(image_path).convert("RGB")

        if x32:
            def to_32s(x):
                return 256 if x < 256 else x - x % 32

            w, h = img.size
            img = img.resize((to_32s(w), to_32s(h)))
        return img

    # prog start here
    def post(self, request, *args, **kwargs):
        b64_img = ""  # global var
        if request.method == 'POST':
            image = request.FILES['myImage']
            open_id = request.POST.get('open_id')
            print(open_id)
            # basedir = 'D:\\HBWS\\hbws\\'
            # path = basedir + '\\samples\\inputs\\'
            basedir = '//opt/prog//hbws//'
            path = basedir + '//samples//inputs//'
            image_name = open_id +'.jpg'
            if not os.path.exists(path + open_id + '.jpg'):
                with open(path + open_id + '.jpg', 'wb+') as f:
                    f.write(image.read())
                    f.close()
                    print('success')
                # self.parse_args()
            parser = argparse.ArgumentParser()
            parser.add_argument( '--checkpoint',type=str,default='./weights/face_paint_512_v1.pt')
            parser.add_argument('--input_dir',type=str,default='./samples/inputs')
            parser.add_argument('--output_dir',type=str,default='./samples/results')
            parser.add_argument('--device',type=str,default='cpu')
            parser.add_argument('--upsample_align',type=bool,default=False,
                                help="Align corners in decoder upsampling layers")
            parser.add_argument('--x32',action="store_true",help="Resize images to multiple of 32")
            args = parser.parse_args(args=[])

            device = args.device

            net = Generator()
            net.load_state_dict(torch.load(args.checkpoint, map_location=device))
            print(f"model loaded: {args.checkpoint}")

            os.makedirs(args.output_dir, exist_ok=True)

            # for image_name in sorted(os.listdir(args.input_dir)):
            #     if os.path.splitext(image_name)[-1].lower() not in [".jpg", ".png", ".bmp", ".tiff"]:
            #         continue

            image = test_fun.load_image(os.path.join(args.input_dir, image_name), args.x32)

            with torch.no_grad():
                image = to_tensor(image).unsqueeze(0) * 2 - 1
                out = net(image.to(device), args.upsample_align).cpu()
                out = out.squeeze(0).clip(-1, 1) * 0.5 + 0.5
                out = to_pil_image(out)

                b_img = io.BytesIO()
                out.save(b_img, format('jpeg'))

            # print(out_image)
            out.save(os.path.join(args.output_dir, image_name))
            print(f"image saved: {image_name}")#show success saved image
            b_img = io.BytesIO()
            out.save(b_img, format('jpeg'))
            b_img = b_img.getvalue()
            b64_img = base64.b64encode(b_img)
            print('now is test image correctly')
        return HttpResponse(b64_img)

#DisneyStyle_face
class DisneyStyle_face(APIView):
    def load_image(image_path, x32=False):
        img = Image.open(image_path).convert("RGB")

        if x32:
            def to_32s(x):
                return 256 if x < 256 else x - x % 32

            w, h = img.size
            img = img.resize((to_32s(w), to_32s(h)))
        return img

    # prog start here
    def post(self, request, *args, **kwargs):
        b64_img = ""  # global var
        # from wx get Image
        if request.method == 'POST':
            image = request.FILES['myImage']
            open_id = request.POST.get('open_id')
            print(open_id)
            # basedir = 'D:\\HBWS\\hbws\\'
            # path = basedir + '\\samples\\inputs\\'
            basedir = '//opt/prog//hbws//'
            path = basedir + '//samples//inputs//'
            image_name = open_id + '.jpg'
            if not os.path.exists(path + open_id + '.jpg'):
                with open(path + open_id + '.jpg', 'wb+') as f:
                    f.write(image.read())
                    f.close()
                    print('success')
                # self.parse_args()
            parser = argparse.ArgumentParser()
            parser.add_argument('--checkpoint', type=str, default='./weights/face_paint_512_v2.pt')
            parser.add_argument('--input_dir', type=str, default='./samples/inputs')
            parser.add_argument('--output_dir', type=str, default='./samples/results')
            parser.add_argument('--device', type=str, default='cpu')
            parser.add_argument('--upsample_align', type=bool, default=False,
                                help="Align corners in decoder upsampling layers")
            parser.add_argument('--x32', action="store_true", help="Resize images to multiple of 32")
            args = parser.parse_args(args=[])
            # test(args)
            device = args.device

            net = Generator()
            net.load_state_dict(torch.load(args.checkpoint, map_location=device))
            print(f"model loaded: {args.checkpoint}")

            os.makedirs(args.output_dir, exist_ok=True)

            image = test_fun.load_image(os.path.join(args.input_dir, image_name), args.x32)

            # print(image)

            with torch.no_grad():
                image = to_tensor(image).unsqueeze(0) * 2 - 1
                out = net(image.to(device), args.upsample_align).cpu()
                out = out.squeeze(0).clip(-1, 1) * 0.5 + 0.5
                out = to_pil_image(out)

                b_img = io.BytesIO()
                out.save(b_img, format('jpeg'))

            # print(out_image)
            out.save(os.path.join(args.output_dir, image_name))
            print(f"image saved: {image_name}")  # show success saved image
            b_img = io.BytesIO()
            out.save(b_img, format('jpeg'))
            b_img = b_img.getvalue()
            b64_img = base64.b64encode(b_img)
            print('now is test image correctly')
        return HttpResponse(b64_img)

class MiyazakiHayao_style(APIView):
    def load_image(image_path, x32=False):
        img = Image.open(image_path).convert("RGB")

        if x32:
            def to_32s(x):
                return 256 if x < 256 else x - x % 32

            w, h = img.size
            img = img.resize((to_32s(w), to_32s(h)))
        return img

    # prog start here
    def post(self, request, *args, **kwargs):
        b64_img = ""  # global var
        if request.method == 'POST':
            image = request.FILES['myImage']
            open_id = request.POST.get('open_id')
            print(open_id)
            # basedir = 'D:\\HBWS\\hbws\\'
            # path = basedir + '\\samples\\inputs\\'
            basedir = '//opt/prog//hbws//'
            path = basedir + '//samples//inputs//'
            image_name = open_id + '.jpg'
            if not os.path.exists(path + open_id + '.jpg'):
                with open(path + open_id + '.jpg', 'wb+') as f:
                    f.write(image.read())
                    f.close()
                    print('success')
                # self.parse_args()
            parser = argparse.ArgumentParser()
            parser.add_argument('--checkpoint', type=str, default='./weights/celeba_distill.pt')
            parser.add_argument('--input_dir', type=str, default='./samples/inputs')
            parser.add_argument('--output_dir', type=str, default='./samples/results')
            parser.add_argument('--device', type=str, default='cpu')
            parser.add_argument('--upsample_align', type=bool, default=False,
                                help="Align corners in decoder upsampling layers")
            parser.add_argument('--x32', action="store_true", help="Resize images to multiple of 32")
            args = parser.parse_args(args=[])

            # test(args)

            device = args.device

            net = Generator()
            net.load_state_dict(torch.load(args.checkpoint, map_location=device))
            print(f"model loaded: {args.checkpoint}")

            os.makedirs(args.output_dir, exist_ok=True)

            image = test_fun.load_image(os.path.join(args.input_dir, image_name), args.x32)
            # print(image)

            with torch.no_grad():
                image = to_tensor(image).unsqueeze(0) * 2 - 1
                out = net(image.to(device), args.upsample_align).cpu()
                out = out.squeeze(0).clip(-1, 1) * 0.5 + 0.5
                out = to_pil_image(out)

                b_img = io.BytesIO()
                out.save(b_img, format('jpeg'))

            # print(out_image)
            out.save(os.path.join(args.output_dir, image_name))
            print(f"image saved: {image_name}")  # show success saved image
            b_img = io.BytesIO()
            out.save(b_img, format('jpeg'))
            b_img = b_img.getvalue()
            b64_img = base64.b64encode(b_img)
            print('now is test image correctly')
        return HttpResponse(b64_img)

#Face Merge-Campus Graduation Photo-Female
class Campus_Graduation(APIView):
    def post(self, request, *args, **kwargs):
        base64Img = request.data

        try:
            cred = credential.Credential("AKIDX1jDSTFqDLDqEWbgaFfqTvBDB2wvrmfP",
                                         "iHe2oeOvX8hCkIlCZPRQRQLD6vfMxcDi")
            httpProfile = HttpProfile()
            httpProfile.endpoint = "facefusion.tencentcloudapi.com"

            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = facefusion_client.FacefusionClient(cred, "ap-beijing", clientProfile)
            req = models.FaceFusionRequest()


            params = {
                "ProjectId": "312856",
                "ModelId": "qc_312856_682801_17",
                "Image" : base64Img['myImage'] ,
                "RspImgType": "url",
                "PornDetect": 0,
                "CelebrityIdentify": 0
            }
            req.from_json_string(json.dumps(params))
            resp = client.FaceFusion(req)
            print(resp.to_json_string())

        except TencentCloudSDKException as err:
            print(err)

        return HttpResponse(resp)

#Face Merge-Ancient Style Photo-Male
class Ancient_Magic(APIView):
    def post(self, request, *args, **kwargs):
        base64Img = request.data

        try:
            cred = credential.Credential("AKIDX1jDSTFqDLDqEWbgaFfqTvBDB2wvrmfP",
                                         "iHe2oeOvX8hCkIlCZPRQRQLD6vfMxcDi")
            httpProfile = HttpProfile()
            httpProfile.endpoint = "facefusion.tencentcloudapi.com"

            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = facefusion_client.FacefusionClient(cred, "ap-beijing", clientProfile)
            req = models.FaceFusionRequest()

            params = {
                "ProjectId": "312856",
                "ModelId": "qc_312856_123324_16",
                "Image": base64Img['myImage'],
                "RspImgType": "url",
                "PornDetect": 0,
                "CelebrityIdentify": 0
            }
            req.from_json_string(json.dumps(params))
            resp = client.FaceFusion(req)
            print(resp.to_json_string())

        except TencentCloudSDKException as err:
            print(err)

        return HttpResponse(resp)

#Face Merge Weird_Magic Photo-nonHuman
class Weird_Magic(APIView):
    def post(self, request, *args, **kwargs):
        base64Img = request.data

        try:
            cred = credential.Credential("AKIDX1jDSTFqDLDqEWbgaFfqTvBDB2wvrmfP",
                                         "iHe2oeOvX8hCkIlCZPRQRQLD6vfMxcDi")
            httpProfile = HttpProfile()
            httpProfile.endpoint = "facefusion.tencentcloudapi.com"

            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = facefusion_client.FacefusionClient(cred, "ap-beijing", clientProfile)
            req = models.FaceFusionRequest()

            params = {
                "ProjectId": "312856",
                "ModelId": "qc_312856_212613_15",
                "Image": base64Img['myImage'],
                "RspImgType": "url",
                "PornDetect": 0,
                "CelebrityIdentify": 0
            }
            req.from_json_string(json.dumps(params))
            resp = client.FaceFusion(req)
            print(resp.to_json_string())

        except TencentCloudSDKException as err:
            print(err)

        return HttpResponse(resp)

class NothingView(APIView):
    def post(self, request, *args, **kwargs):

        return HttpResponse("Let life be beautiful like summer flowers and death like autumn leaves - Gan Bian Dou Jiao Ji Ding")

#Test
class uploadImageView(APIView):
    def load_image(image_path, x32=False):
        img = Image.open(image_path).convert("RGB")

        if x32:
            def to_32s(x):
                return 256 if x < 256 else x - x % 32

            w, h = img.size
            img = img.resize((to_32s(w), to_32s(h)))
        return img

    # prog start here
    def post(self, request, *args, **kwargs):
        b64_img = ""  # global var
        if request.method == 'POST':
            image = request.FILES['myImage']
            open_id = request.POST.get('open_id')
            print(open_id)
            # basedir = '\\.\\HBWS\\hbws\\'
            # path = basedir + '\\samples\\inputs\\'
            basedir = '//opt/prog//hbws//'
            path = basedir + '//samples//inputs//'
            image_name = open_id + '.jpg'
            if not os.path.exists(path + open_id + '.jpg'):
                with open(path + open_id + '.jpg', 'wb+') as f:
                    f.write(image.read())
                    f.close()
                    print('success')
                # self.parse_args()
            parser = argparse.ArgumentParser()
            parser.add_argument('--checkpoint', type=str, default='./weights/face_paint_512_v1.pt')
            parser.add_argument('--input_dir', type=str, default='./samples/inputs')
            parser.add_argument('--output_dir', type=str, default='./samples/results')
            parser.add_argument('--device', type=str, default='cpu')
            parser.add_argument('--upsample_align', type=bool, default=False,
                                help="Align corners in decoder upsampling layers")
            parser.add_argument('--x32', action="store_true", help="Resize images to multiple of 32")
            args = parser.parse_args(args=[])

            device = args.device

            net = Generator()
            net.load_state_dict(torch.load(args.checkpoint, map_location=device))
            print(f"model loaded: {args.checkpoint}")

            os.makedirs(args.output_dir, exist_ok=True)

            # for image_name in sorted(os.listdir(args.input_dir)):
            #     if os.path.splitext(image_name)[-1].lower() not in [".jpg", ".png", ".bmp", ".tiff"]:
            #         continue

            image = test_fun.load_image(os.path.join(args.input_dir, image_name), args.x32)

            with torch.no_grad():
                image = to_tensor(image).unsqueeze(0) * 2 - 1
                out = net(image.to(device), args.upsample_align).cpu()
                out = out.squeeze(0).clip(-1, 1) * 0.5 + 0.5
                out = to_pil_image(out)

                b_img = io.BytesIO()
                out.save(b_img, format('jpeg'))

            # print(out_image)
            out.save(os.path.join(args.output_dir, image_name))
            print(f"image saved: {image_name}")  # show success saved image
            b_img = io.BytesIO()
            out.save(b_img, format('jpeg'))
            b_img = b_img.getvalue()
            b64_img = base64.b64encode(b_img)
            print('now is test image correctly')
        return HttpResponse(b64_img)
        #Response of Image alreadly existed



    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            return Response('get ok')

            # Image to base64 format
            # b_img = io.BytesIO()
            # out.save(b_img, format('jpeg'))
            # b_img = b_img.getvalue()
            # b64_img = base64.b64encode(b_img)
            # print(b64_img)






