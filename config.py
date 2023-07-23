
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"
    OPENAI_KEY = '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'

config = {
'development': DevelopmentConfig,
'testing': DevelopmentConfig,
'production': DevelopmentConfig
}