from environs import Env

env = Env()
env.read_env()

TG_API_TOKEN = env.str("TG_API_TOKEN")
VK_API_TOKEN = env.str("VK_API_TOKEN")
CACHE_DIR = "cache"
