import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '79dcd7a2dba0e38ebb4d52b46ce38fecd1333e61aca4ed67'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dev:password@localhost/makkarriz'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#    JWT_SECRET_KEY = '79dcd7a2dba0e38ebb4d52b46ce38fecd1333e61aca4ed67'
