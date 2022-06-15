## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgA3oS4RAQCh2N1i9WlAkxZ2BZ2-nMFnxQCVEscAs80Qn6I02VXYJQ5uaj8kukeM3dvHzALZxiypoCTXusAvH5BuWKlvCEbpWNcPvwZ5zV8q4hxxzxopZxCkcaTWx6hJWUukBxlGVK4ZAHC1g6NWM4EbDqtVSFLgsSiVozNfnHeljV9RdjiOMN7N3mfk8kkccvgVs00y4ix2D91IablA9VonXQBOYFwqe98-It6Hl2kvvvtRElHO-0f5962CBYnSTEanyIUhYH6R2C3Jo5Sg7TkAqstK2RnOyZ0w1O0-MuY4amy2RFMej6X7bI3c4xJhERxjU2fx9LqpQYKv57HMY34XAAAAATL2FpYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5071806155:AAEWzAC_n5FdXV-d5NablKtwBGiXRqhRzwc")
BOT_NAME = getenv("BOT_NAME", "s")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "𝖠𝗅𝗂 𝖺𝖱𝗄𝖺𝖭")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@GGGuu")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "@PDYDBoT")
OWNER_ID = getenv("OWNER_ID", "1936682943")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "PDYDP")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "SZZZV")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SZZZV")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1936682943").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
