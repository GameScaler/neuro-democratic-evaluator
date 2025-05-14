import os
from dotenv import load_dotenv

load_dotenv()

XHS_COOKIE = os.getenv("XHS_COOKIE")  # 小红书登录cookie
LLM_API_KEY = os.getenv("LLM_API_KEY")  # 大模型平台密钥