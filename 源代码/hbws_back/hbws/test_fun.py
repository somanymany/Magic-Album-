import io,os,argparse,torch,base64,PIL,cv2

from PIL import Image
from torchvision.transforms.functional import to_tensor, to_pil_image
from model import Generator
import numpy as np
import matplotlib.pyplot as plt
import torchvision.transforms as transforms


torch.backends.cudnn.enabled = False
torch.backends.cudnn.benchmark = False
torch.backends.cudnn.deterministic = True

def load_image(image_path, x32=False):
    img = Image.open(image_path).convert("RGB")

    if x32:
        def to_32s(x):
            return 256 if x < 256 else x - x % 32
        w, h = img.size
        img = img.resize((to_32s(w), to_32s(h)))
        print('load_image')
        print(img)
    return img



def test(args):
    device = args.device

    net = Generator()
    net.load_state_dict(torch.load(args.checkpoint, map_location=device))
    print(f"model loaded: {args.checkpoint}")

    os.makedirs(args.output_dir, exist_ok=True)

    for image_name in sorted(os.listdir(args.input_dir)):
        if os.path.splitext(image_name)[-1].lower() not in [".jpg", ".png", ".bmp", ".tiff"]:
            continue

        image = load_image(os.path.join(args.input_dir, image_name), args.x32)
        # print(image)

        with torch.no_grad():
            image = to_tensor(image).unsqueeze(0) * 2 - 1
            out = net(image.to(device), args.upsample_align).cpu()
            out = out.squeeze(0).clip(-1, 1) * 0.5 + 0.5
            out = to_pil_image(out)
            print('out type', type(out))
            print('image type', type(image))

            b_img = io.BytesIO()
            out.save(b_img, format('jpeg'))
            b_img = b_img.getvalue()
            b64_img = base64.b64encode(b_img)
            print(b64_img)

        # print(out_image)
        # if that have two images, and there will rotate twice
        out.save(os.path.join(args.output_dir, image_name))
        print(f"image saved: {image_name}")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--checkpoint',
        type=str,
        default='./weights/face_paint_512_v2.pt',
    )
    parser.add_argument(
        '--input_dir',
        type=str,
        default='./samples/inputs',
    )
    parser.add_argument(
        '--output_dir',
        type=str,
        default='./samples/results/',
    )
    parser.add_argument(
        '--device',
        type=str,
        default='cpu',
    )
    parser.add_argument(
        '--upsample_align',
        type=bool,
        default=False,
        help="Align corners in decoder upsampling layers"
    )
    parser.add_argument(
        '--x32',
        action="store_true",
        help="Resize images to multiple of 32"
    )
    args = parser.parse_args()

    test(args)






