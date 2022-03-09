import os

class BaseConfig(object):
    'Base config class'
    SECRET_KEY = '5d5dd856305f4eccaf147fff12107db92d3bcd63dec94569ae0234797d9ce112'
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARIABLE = 'my value'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    


class Docker(BaseConfig):
    'Docker'
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = os.getenv("CACHE_TYPE","redis")
    CACHE_REDIS_HOST = os.getenv('CACHE_REDIS_HOST','redis')
    CACHE_REDIS_PORT = os.getenv('CACHE_REDIS_PORT',6379)
    CACHE_REDIS_DB = os.getenv('CACHE_REDIS_DB','0')
    CACHE_REDIS_URL = os.getenv('CACHE_REDIS_URL','redis://redis:6379/0')
    CACHE_DEFAULT_TIMEOUT = os.getenv('CACHE_DEFAULT_TIMEOUT',500)

    

class ProductionConfig(BaseConfig):
    'Production specific config'
    DEBUG = False
    SECRET_KEY = '62a6d063665287a56e828d15c179f0b4dc4186c0c70c504c1d457558e22d7c50'

class StagingConfig(BaseConfig):
    'Staging specific config'
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    'Development environment specific config'
    DEBUG = False
    TESTING = True
    SECRET_KEY = 'fdcd7fec3e1f2d86fe0732c0f6392c61ff4f6192a51625b09989360e5779816d'
    CACHE_TYPE = os.getenv('CACHE_TYPE','simple')
    CACHE_DEFAULT_TIMEOUT = os.getenv('CACHE_DEFAULT_TIMEOUT',500)
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mateme@localhost/learecordshop'
    FLASK_ENV = os.getenv('FLASK_ENV','development')
    