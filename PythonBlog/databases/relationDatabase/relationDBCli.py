from typing import Optional

import asyncpg
from asyncpg.pool import Pool

# 导入配置
from ...configs.relationDatabase import (
    DB_DSN,
    DB_POOL_MIN_SIZE,
    DB_POOL_MAX_SIZE,
    DB_POOL_CONNECTION_MAX_QUERIES,
    DB_POOL_CONNECTION_MAX_LIFETIME,
    DB_SSL,
    DB_CONNECTION_COMMAND_TIMEOUT,
    DB_CONNECTION_TIMEOUT,

)


class PostgreSQLCli:
    """
        PostgreSQL 数据库连接池管理类
    """
    def __init__(self,
                 *,
                 db_dsn: str = str(DB_DSN),
                 db_pool_min_size: int = DB_POOL_MIN_SIZE,
                 db_pool_max_size: int = DB_POOL_MAX_SIZE,
                 db_pool_connection_max_queries: int = DB_POOL_CONNECTION_MAX_QUERIES,
                 db_pool_connection_max_lifetime: float = DB_POOL_CONNECTION_MAX_LIFETIME,
                 db_ssl: str = DB_SSL,
                 db_connection_command_timeout: int = DB_CONNECTION_COMMAND_TIMEOUT,
                 db_connection_timeout: int = DB_CONNECTION_TIMEOUT ) -> None:
        
        self.pool: Optional[Pool] = None

        self.db_dsn = db_dsn
        self.db_pool_min_size = db_pool_min_size
        self.db_pool_max_size = db_pool_max_size
        self.db_pool_connection_max_queries = db_pool_connection_max_queries
        self.db_pool_connection_max_lifetime = db_pool_connection_max_lifetime
        self.db_ssl = db_ssl
        self.db_connection_command_timeout = db_connection_command_timeout
        self.db_connection_timeout = db_connection_timeout

    
    async def initPool(self):
        """
            初始化PostgreSQL连接池
        """
        self.pool = await asyncpg.create_pool(
            dsn = self.db_dsn,
            min_size = self.db_pool_min_size,
            max_size = self.db_pool_max_size,
            max_queries = self.db_pool_connection_max_queries,
            max_inactive_connection_lifetime = self.db_pool_connection_max_lifetime,
            ssl = self.db_ssl,
            command_timeout = self.db_connection_command_timeout,
            timeout = self.db_connection_timeout,
            # 不太清除这个到底是用来干什么的使用默认的配置先
            # statement_cache_size = 100, # 不太清除这个到底是用来干什么的使用默认的配置先
            # max_cached_statement_lifetime = 300 
        )


    async def closePool(self):
        """
            关闭PostgreSQL连接池
        """        
        if self.pool is not None:
            await self.pool.close()
    


relation_db_cli = PostgreSQLCli()


__all__ = [
    "relation_db_cli"
]