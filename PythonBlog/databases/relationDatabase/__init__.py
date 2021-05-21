"""
    感觉SQLAlchemy 使用好复杂呀 直接使用 asyncpg 吧 
    反正其返回对象Record对象就与字典对象差不多
    
    等后面有空再用ORM吧
"""


from sqlalchemy.ext.declarative import declarative_base


DB_BASE = declarative_base()



# 方便逻辑查询导入 
# 也方便 alembic 对Model进行数据库迁移

from .orms import *


