from service.instabot import InstabotService

POST_DIR = './static'


def main():
    is_ = InstabotService(POST_DIR)
    is_.upload_post()


if __name__ == '__main__':
    main()
