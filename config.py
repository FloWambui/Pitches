import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://flora:wambui@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    '''
    Development configuration child class
    '''
    
DEBUG = True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}