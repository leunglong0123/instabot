from service.instabot import InstabotService
from service.image import ImageService
POST_DIR = './output'
TMP_IMG = ''


def main():
    ImageService.png_to_jpg('static/temp-post-img.png', './output')
    is_ = InstabotService(POST_DIR)
    is_.upload_post()


if __name__ == '__main__':
    main()
