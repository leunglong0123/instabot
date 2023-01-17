from PIL import Image
import os
import re


class ImageService:
    def __init__(self) -> None:
        pass

    @staticmethod
    def png_to_jpg(image_dir, output_dir):
        im = Image.open(image_dir)
        if not im.mode == 'RGB':
            im = im.convert('RGB')
            image_dir = re.findall(r'[^\/]+(?=\.)', image_dir)[0]
            print(os.path.join(output_dir, image_dir, 'jpg'))
            im.save(os.path.join(output_dir, image_dir + '.jpg'))

        else:
            raise Exception('ImageService.png_to_jpg Exception')
