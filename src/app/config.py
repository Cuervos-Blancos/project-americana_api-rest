class Config():
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """
    Development configurations:
    """
    DEBUG=True
    DEVELOPMENT=True
    HOST="0.0.0.0"
    PORT="8080"
        
class ProductionConfig (Config):
    """
    Production configurations
        debug:false
    """
    DEBUG = False
    DEVELOPMENT = False