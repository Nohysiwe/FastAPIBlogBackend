
from typing import List, Optional

from asyncpg import Connection

# 导入数据库连接池
from ..databases.relationDatabase.relationDBCli import relation_db_cli

from ..dataModels.entity import (
    UniqueView,
)


class UniqueViewDao:
    
    def __init__(self):
        pass

    async def listUniqueViews(
        self,
        *,
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> List[int]:
        
        sql = "select views_count " \
            "from tb_unique_view " \
            "where to_char(create_time, 'YYYYWW') = to_char(now(), 'YYYYWW') " \
            "order by create_time;"
        
        ret_data: List[int] = []
        release_signal = False
        if conn is None:
            conn: Connection = await relation_db_cli.pool.acquire()
            release_signal = True
            create_transaction = True
        try:
            if create_transaction:
                tr = conn.transaction()
                await tr.start()
            try:
                async for record in conn.cursor(sql):
                    ret_data.append(record.views_count)
            except:
                if create_transaction:
                    await tr.rollback()
                raise
            else:
                if create_transaction:
                    await tr.commit()
        finally:
            if release_signal:
                await relation_db_cli.pool.release(conn)
        
        return ret_data


__all__ = [
   "UniqueViewDao",

]