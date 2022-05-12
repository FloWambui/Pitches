import os



class Config:
    '''
    General configuration parent class
    '''
  
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    


class ProdConfig(Config):
    # uri = os.getenv('DATABASE_URL')
    # if uri and uri.startswith('postgres://'):
    #     uri = uri.replace('postgres://', 'postgresql://', 1)    
    # SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://flora:wambui@localhost/pitches'


class DevConfig(Config):
    '''
    Development configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://flora:wambui@localhost/pitches'


    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
