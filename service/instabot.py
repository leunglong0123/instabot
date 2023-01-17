import glob
import os
import sys
import time
import re
from io import open
from instabot import Bot  # noqa: E402


class InstabotService:
    def __init__(self, folder_path='/.pic') -> None:
        self.folder_path = folder_path
        pass

    def upload_post(self):
        sys.path.append(os.path.join(sys.path[0], "../../"))
        print(os.path.join(sys.path[0], "../../"))
        posted_pic_list = []
        try:
            with open("pics.txt", "r", encoding="utf8") as f:
                posted_pic_list = f.read().splitlines()
        except Exception:
            posted_pic_list = []

        bot = Bot()
        bot.login()

        pics = glob.glob(self.folder_path + "/*.jpg")
        pics = sorted(pics)
        try:
            for pic in pics:
                if pic in posted_pic_list:
                    continue

                pic_name = re.findall(r'[^\/]+(?=\.)', pic)[0]
                print("upload: " + pic_name)

                description_file = self.folder_path + "/" + pic_name + ".txt"

                if os.path.isfile(description_file):
                    with open(description_file, "r") as file:
                        caption = file.read()
                else:
                    caption = pic_name.replace("-", " ")

                bot.upload_photo(pic, caption=caption)
                if bot.api.last_response.status_code != 200:
                    print(bot.api.last_response)
                    # snd msg
                    break

                if pic not in posted_pic_list:
                    posted_pic_list.append(pic)
                    with open("pics.txt", "a", encoding="utf8") as f:
                        f.write(pic + "\n")

        except Exception as e:
            print(str(e))
            raise e
