class BaseConfig:
  """Base configuration"""
  TESTING = False

class DevelopmentConfig(BaseConfig):
  """Development configuration"""
  pass

class TestingConfig(BaseConfig):
  """Development configuration"""
  TESTING = True

class ProductionConfiguration(BaseConfig):
  """Production configuration"""
  pass