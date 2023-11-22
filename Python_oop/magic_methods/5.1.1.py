def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class Config:
    def __init__(self):
        self.program_name = 'GenerationPy'
        self.environment = 'release'
        self.loglevel = 'verbose'
        self.version = '1.0.0'


config = Config()

print(config.program_name)
print(config.environment)
print(config.loglevel)
print(config.version)

config1 = Config()
config2 = Config()
config3 = Config()

print(config1 is config2)
print(config1 is config3)
