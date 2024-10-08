import os
import sqlite3
from config.config_data import *
from .data_class_port import *


class SqlIte(metaclass=MyData):
    data_name = 'sqlite'

    def __init__(self,config_json=None):
        self.database = None

    def execute(self, expression: str, *data):
        if self.database is None:
            self.database = f'./xbbot/data/{GaiJson.gain().数据库名称}.db'
        print(expression % data)
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute(expression % data)
        return_data = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return return_data
