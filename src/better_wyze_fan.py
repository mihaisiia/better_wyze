import os
from wyze_sdk import Client

client = Client(email=os.getenv('WYZE_EMAIL'), password=os.getenv('WYZE_PASSWORD'))
