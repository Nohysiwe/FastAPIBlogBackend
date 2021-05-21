"""
    CacheDB 连接池初始化 方法类
"""

from typing import Optional
from fastapi import FastAPI

from .abstractEventFuncClass import AbstractEventFuncClass
from ..databases.cacheDatabase.cacheDBCli import cache_db_cli


class InitiateCacheDBPool(AbstractEventFuncClass):
    """
        初始化缓存数据库连接池
    """
    @staticmethod
    async def startup( *, 
                       app: FastAPI) -> None:
        """
            App 启动时 创建缓存数据库(Redis)的数据库连接池
        """
        
        await cache_db_cli.initPool()
    
    @staticmethod
    async def shutdown(*, app: Optional[FastAPI]) -> None:
        """
            App 启动时 关闭缓存数据库(Redis)的数据库连接池
        """
        
        await cache_db_cli.closePool()

    