import os

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("TOKEN")  # Bot token
ADMINS = env.str("ADMINS")  # Admin ID
