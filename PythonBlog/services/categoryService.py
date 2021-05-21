
from typing import List, Optional


# 导入 数据库连接池对象
from ..databases.relationDatabase.relationDBCli import relation_db_cli
from ..databases.cacheDatabase.cacheDBCli import cache_db_cli

from ..dataModels.dto import (
    CategoryDTO,
    PageDTO,
)

from ..dataModels.entity import (
    Article,
    Category,

)

from ..dataModels.vo import (
    ConditionVO,

)

from ..daoOperation import (
    ArticleDao,
    CategoryDao,
)


class CategoryService:
    """
        分类操作逻辑实现
    """
    
    def __init__(self) -> None:
        pass
    

    async def listCategories(self) -> PageDTO[CategoryDTO]:
        """
            列出分类信息
        """
        category_dao = CategoryDao()
        async with relation_db_cli.pool.acquire() as conn:
            async with conn.transaction():
                categorydto_list: List[CategoryDTO] = await category_dao.listCategoryDTO(
                    conn = conn,
                    create_transaction = False
                )
                count: Optional[int] = await conn.fetchval(
                    "select count(1) from tb_category;"
                )

        pagedto = PageDTO[CategoryDTO](
            recordList = categorydto_list,
            count = count
        )
        
        return pagedto

    
    async def listCategoryBackDTO(
        self,
        conditionVO: ConditionVO ) -> PageDTO[Category]:
        """
            按页列出后台展示的分类信息数据
        """
        # :TODO 这里的count应该代表总数, 所以需要查询再查询一次表总数
        
        raise NotImplementedError("NotImplemented !!!")
