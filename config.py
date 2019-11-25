import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gertjioecoezte8912398182934jd'