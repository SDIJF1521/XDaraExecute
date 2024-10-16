
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
       3. 配置文件书写
          - 对于生成的配置书写
            - 生成的mysql的配置文件内容如下：
                ``` json
                {
                  "数据库主机": "127.0.0.1",
                  "数据库账号": "root",
                  "数据库密码": "root",
                  "数据库名称": "data_base_name",
                  "表单": {
                      "2表单": {
                          "表单名称": "1_table",
                          "字段": ["1_field", "2_field", "3_field", "4_field"],
                          "类型": ["varchar (255)", "int", "varchar (255)", "int"]
                      },
                      "1表单": {
                          "表单名称": "2_table",
                          "字段": ["1_field", "2_field", "3_field"],
                          "类型": ["varchar (255)", "int", "varchar (255)"]
                      }
                  }}
                ```
            - 这里我们需要提供数据库主机ip,数据库账号，密码，数据库名称以及数据库的表单及其字段，现在假设我们用一个如下表的数据库,其用户，密码为root，主机ip为127.0.0.1
              - <table>
                    <tr>
                      <th>数据库名称</th>
                      <th>表单</th>
                      <th>字段</th>
                      <th>数据类型</th>
                    </tr>
                    <tr>
                      <td rowspan="10">XB</td>
                      <td rowspan="4">sign</td>
                      <td>user</td>
                      <td>varchar (255)</td>
                    </tr>
                    <tr>
                      <td>积分</td>
                      <td>int</td>
                    </tr>
                    <tr>
                      <td>日期</td>
                      <td>varchar (255)</td>
                    </tr>
                    <tr>
                      <td>天数</td>
                      <td>int</td>
                    </tr>
                    <tr>
                      <td rowspan="3">cq</td>
                      <td>user</td>
                      <td>varchar (255)</td>
                    </tr>
                    <tr>
                      <td>id</td>
                      <td>int</td>
                    </tr>
                    <tr>
                      <td>日期</td>
                      <td>varchar (255)</td>
                    </tr>
                    <tr>
                      <td rowspan="3">sgin</td>
                      <td>id</td>
                      <td>int</td>
                    </tr>
                    <tr>
                      <td>签诗</td>
                      <td>varchar (255)</td>
                    </tr>
                    <tr>
                      <td>签诗</td>
                      <td>varchar (255)</td>
                    </tr>
              </table>
            - 修改后的如下
              ```json
                {
                  "数据库主机": "127.0.0.1",
                  "数据库账号": "root",
                  "数据库密码": "root",
                  "数据库名称": "XB",
                  "表单": {
                      "签到表单": {
                          "表单名称": "pd",
                          "字段": [
                              "user",
                              "积分",
                              "日期",
                              "天数"
                          ],
                          "类型": [
                              "varchar (255)",
                              "int",
                              "varchar (255)",
                              "int"
                          ]
                      },
                      "抽签表单": {
                          "表单名称": "cq",
                          "字段": [
                              "user",
                              "id",
                              "日期"
                          ],
                          "类型": [
                              "varchar (255)",
                              "int",
                              "varchar (255)"
                          ]
                      },
                      "存签表单": {
                          "表单名称": "sgin",
                          "字段": [
                              "id",
                              "签诗",
                              "意思"
                          ],
                          "类型": [
                              "int",
                              "varchar (255)",
                              "varchar (255)"
                          ]
                      }
                  }}
              ```
### 便携查询
  - 便携查询功能依赖于配置文件，功能是通过配置文件来确定字段的正确，便捷方法都是使用DataExecute()类调用下面提供案例一及语法
    - 便携查询的的便捷函数是`DataExecute()`$类的data_read_execute方法该方法的参数信息如下$
      ```python
      DataExecute(name).data_read_execute(form_name,creening_condition,field)
      '''
      name：容器名称，该参数为必填参数
      form_name：表单名称,该参数为必填参数
      creening_conditio：字段名，该参数为可选参数不填时默认为None在不写时为所有字段
      field：筛选条件，该参数为该参数为可选参数不填时默认为None
      '''
      ```
        - 现在假设配置文件如上我们要在mysql数据库内查找pd表内的所有数据我们可以这样来做
          ```python
          data = DataExecute('mysql'，).data_read_execute(form_name = 'pd')
          ```
        - 如果我们只要的是 `qd` $表单中的$ `user` $字段内容那么我们需要填写$ `creening_conditio` $参数$
          ```python
          data = DateExecute('mysql').data_read_execute(form_name = 'pd',creening_conditio=user)
          # 注意creening_conditio参数的内容要为字符串
          ```
        - 现在假设我们需要 `pd` $表单中的$`积分`$字段大于等于20的所有用户我们可以用如下代码$
          ```python
          data = DateExecute('mysql').data_read_execute(form_name = 'pd',creening_conditio=user,field = '积分 > 20')
          # 当我们在便捷查询方法中需要用到条件筛选查询时我们就要将field参数填写上，其内容为筛选的条件，数据类型要为字符串
          ```
        - 若我们的配置文件并不在当前文件夹下面或者配置文件的名称不为`data_config.json` $那么$
          
### 便携存储
### 高阶查询
### 高阶存储
### 拓展库
#### 拓展容器类
#### 拓展操作类
