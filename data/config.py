import os

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = str(os.environ.get("TOKEN"))  # Bot token
ADMINS = str(os.environ.get("ADMINS"))  # Admin ID
