import redis
import logging
from config.config_data import GaiJson
from .data_class_port import *

# 配置日志记录
logging.basicConfig(level=logging.INFO)

class Redis(metaclass=MyData):
    data_name = 'redis'

    def __init__(self):
        self.host = None
        self.port = None

    def execute(self):

        if self.host is None:
            self.host = GaiJson().gain().redis设置['redis-host']
        if self.port is None:
            self.port = GaiJson().gain().redis设置['redis-port']
            pool = redis.ConnectionPool(
            host=self.host,
            port=self.port,
            decode_responses=True
        )

        return redis.Redis(connection_pool=self.pool)

    def data_read_execute(self, form_name: str, screening_condition: str = None, field: str = None):
        try:
            r = self.execute()
            keys = r.keys(f"{form_name}:*")

            results = []
            for key in keys:
                value = r.hgetall(key)
                if screening_condition:
                    # 用安全的方式来处理条件
                    if self.check_condition(value, screening_condition):
                        results.append(value)
                else:
                    results.append(value)

            if field:
                return [{field: result.get(field)} for result in results]

            return results if results else None  # 返回空列表或 None
        except Exception as e:
            logging.error(f"读取数据时出错: {e}")
            return None

    def data_deposit_execute(self, form_name: str, data: dict = None):
        try:
            r = self.execute()
            key = f"{form_name}:{data.get('id')}"
            r.hset(key, mapping=data)  # 使用 hset 替代 hmset
            logging.info(f"成功存储数据: {data} 到 {key}")
        except Exception as e:
            logging.error(f"存储数据时出错: {e}")

    def check_condition(self, value: dict, condition: str) -> bool:
        # 自定义条件检查的方法，确保安全
        # 实现条件的解析和检查逻辑
        # 示例：将条件转为一个可执行的函数
        return True  # 这里返回 True 表示条件匹配，实际实现需替换
