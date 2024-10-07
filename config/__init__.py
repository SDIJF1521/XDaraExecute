# config/__init__.py
from .creation_config import CreateConfigParent
from .create import *

def get_config_classes():
    rtn = {'mysql': MysqlConfig(),
            'sqlite': SqliteConfig(),
            'json': JasonConfig(),
            'redis': RedisConfig()}
    rtn.update()
    return rtn