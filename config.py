import os

class BaseConfig(object):
    'Base config class'
    SECRET_KEY = '5d5dd856305f4eccaf147fff12107db92d3bcd63dec94569ae0234797d9ce112'
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARIABLE = 'my value'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mateme@localhost/learecordshop'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Docker(BaseConfig):
    'Docker'
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = os.environ['CACHE_TYPE']
    CACHE_REDIS_HOST = os.environ['CACHE_REDIS_HOST']
    CACHE_REDIS_PORT = os.environ['CACHE_REDIS_PORT']
    CACHE_REDIS_DB = os.environ['CACHE_REDIS_DB']
    CACHE_REDIS_URL = os.environ['CACHE_REDIS_URL']
    CACHE_DEFAULT_TIMEOUT = os.environ['CACHE_DEFAULT_TIMEOUT']

    

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