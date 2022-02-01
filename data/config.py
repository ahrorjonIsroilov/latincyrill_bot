from environs import Env
import os
# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
