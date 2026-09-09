import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLITECLOUD_CONNECTION = os.getenv("SQLITECLOUD_CONNECTION")