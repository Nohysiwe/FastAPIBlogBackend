
from PythonBlog.configs.cacheDatabase.config import CACHE_DB_PASSWORD, CACHE_DB_USE_DB
from typing import Optional

import aioredis
from aioredis import ConnectionsPool

from ...configs.cacheDatabase import (
    CACHE_DB_HOST,
    CACHE_DB_PORT,
    CACHE_DB_PASSWORD,
    CACHE_DB_USE_DB,
    CACHE_DB_ENCODING,
    CACHE_DB_POOL_MINSIZE,
    CACHE_DB_POOL_MAXSIZE,
    CACHE_DB_CREATE_CONNECTION_TIMEOUT
)



class RedisCli:
    """
        Redis缓存数据库连接池管理类
    """
    
    def __init__(self, 
                *,
                db_host: str = CACHE_DB_HOST,
                db_port: int = CACHE_DB_PORT,
                db_password: str = str(CACHE_DB_PASSWORD),
                db_use_db: int = CACHE_DB_USE_DB,
                db_encoding: str = CACHE_DB_ENCODING,
                db_pool_min_size: int = CACHE_DB_POOL_MINSIZE,
                db_pool_max_size: int = CACHE_DB_POOL_MAXSIZE,
                db_create_connection_timeout: int = CACHE_DB_CREATE_CONNECTION_TIMEOUT) -> None:
        
        # redis 连接池
        self.pool: Optional[ConnectionsPool] = None
        
        # 记录连接池配置
        self.db_host = db_host 
        self.db_port = db_port
        self.db_password = db_password
        self.db_use_db = db_use_db
        self.db_encoding = db_encoding
        self.db_pool_min_size = db_pool_min_size
        self.db_pool_max_size = db_pool_max_size
        self.db_create_connection_timeout = db_create_connection_timeout
        

    async def initPool(self):
        """
            初始化 Redis 连接池
        """
        address = f"redis://{self.db_host}:{self.db_port}"
    
        self.pool = await aioredis.create_pool(
            address = address,
            db = self.db_use_db,
            password = self.db_password,
            encoding = self.db_encoding,
            minsize = self.db_pool_min_size,
            maxsize = self.db_pool_max_size,
            create_connection_timeout= self.db_create_connection_timeout
        )
        
        
    async def closePool(self):
        """
            关闭 Redis 连接池
        """
        
        if self.pool is not None:
            if not self.pool.closed:
                self.pool.close()
                await self.pool.wait_closed()
            

cache_db_cli = RedisCli()


__all__ = [
    "cache_db_cli"
]
        
        
        