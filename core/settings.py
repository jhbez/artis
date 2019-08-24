import os
import logging

class Settings:
    
    LIVE = "live"
    SANDBOX = "sandbox"
    
    
    def __init__():
        pass
    
    @classmethod
    def get_env(cls):
        _env = os.getenv("BLAK_ARTIS_ENV", "")
        if _env  in [cls.LIVE, cls.SANDBOX]:
            return _env
        else:
            Settings.log.info("demo")
        return SANDBOX
    
    
class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    DATABASE_URI = "sqlite:///db/blackarits.sqlite"
    ENV = "production"
    
class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = "sqlite:///db/blackaritsdev.sqlite"
    ENV = "development"

class TestingConfig(Config):
    TESTING = True
    ENV = "testing"