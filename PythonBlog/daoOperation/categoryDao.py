from typing import List, Optional

from asyncpg import Connection

# 导入数据库连接池
from ..databases.relationDatabase.relationDBCli import relation_db_cli


from ..dataModels.dto import (
    CategoryDTO
)



class CategoryDao:

    def __init__(self):
        pass 


    async def listCategoryDTO(
        self,
        *, 
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> List[CategoryDTO]:
        """
            查询分类和对应文章数量
            
            @return 分类集合
        """
        sql = "select c.id, c.category_name as categoryName, " \
            "count(1) as articleCount " \
            "from tb_category as c " \
            "join tb_article as a on c.id = a.category_id " \
            "group by c.id, c.category_name;"
        
        categorydto_list: List[CategoryDTO] = []
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
                    categorydto_list.append(
                        CategoryDTO.parse_obj(record)
                    )
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

        return categorydto_list

    
        
__all__ = [
    "CategoryDao",
]