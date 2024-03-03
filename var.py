import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "13328710"))
    API_HASH = os.getenv("API_HASH", "3f217dce997731657ba235ed0b0f784b")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7004724865:AAFmqAecN3LiYJXV4sfEPaZGiNMOXjymCJM")
    sudo = os.getenv("SUDO")
    SUDO = [1544179149, 6693496289]
    if sudo:
        SUDO = make_int(sudo)
