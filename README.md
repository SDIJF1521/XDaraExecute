
# XDataExecute
## 项目介绍
  该项目旨在帮助开发者更轻松地进行数据操作目前提供了与 MySQL、Redis 和 SQLite 数据库json的简化交互接口，。库使用配置文件管理数据库连接信息，支持数据的读取和存储操作。

## 项目文件结构
```
your_project/
│
├── fun/
|   ├── __init__.py
│   ├── mysql_execute.py    # MySQL 数据库操作
│   ├── redis_execute.py     # Redis 数据库操作
│   └── sqlite_execute.py     # SQLite 数据库操作
│
├── config/
|   ├── __init__.py
│   ├── config_data.py       # 配置数据处理
│   └── ...                   # 其他配置处理库
│
├── CreateConfig.py
|
└── README.md                 # 本文档
```
## 库使用文档
### 配置
  - 使用该库前我们需要进行一下简单的配置
      1. 在要主程序文件夹下我们要创建两个文件夹文件夹名称分别为`DataExecute1` $数据容器拓展文件夹和$ `ConfigPlug`配置拓展文件夹
      2.在主程序文件夹下使用CreateConfig命令程序，CreateConfig命令程序语法如下：
       ```shell
       python -m CreateConfig.py <config_type> [--filename <file_name>]
       参数说明：
            1.config_type: 必填参数，表示你想要生成的配置文件类型。该值必须从配置类的可用类型中选择。
            2.--filename: 可选参数，指定生成的配置文件名。如果不提供该参数，则默认为 data_config.json。
       例：
            python -m CreateConfig.py sqlite
       ```
### 便携查询
  - 便携查询的方法对于
### 便携存储
### 高阶查询
### 高阶存储
### 拓展库
