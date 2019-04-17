class Config:
    '''
    General configuration parent class
    '''
    pass

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: the parent configuration class with
        general configuration settingss
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: the parent configuration class with
        general configuration settingss
    '''
    DEBUG = True