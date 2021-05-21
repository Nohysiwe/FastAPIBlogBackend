
# 导入类型注释所需内容 (类型注释是一个优良的习惯, 也是未来趋势)
from typing import Optional
from fastapi import FastAPI

from .abstractEventFuncClass import AbstractEventFuncClass
from ..databases.relationDatabase.relationDBCli import relation_db_cli


class InitiateRelationDBPool(AbstractEventFuncClass):
    """
        初始化关系型数据库连接池
    """
    @staticmethod
    async def startup( *, 
                       app:FastAPI ) -> None:
        """
            App 启动时 创建关系型数据库的数据库连接池
        """

        await relation_db_cli.initPool()

    @staticmethod
    async def shutdown( *, 
                        app: Optional[FastAPI] = None ) -> None:
        """
            App 关闭时 关闭关系型数据库的数据库连接池
        """

        await relation_db_cli.closePool()
        
        