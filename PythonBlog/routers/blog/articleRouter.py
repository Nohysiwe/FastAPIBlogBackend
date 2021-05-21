from PythonBlog.dataModels.dto.articleHomeDTO import ArticleHomeDTO
from typing import List
from fastapi import (
    APIRouter, 
    Path, 
    Query, 
    Body,
    Depends
)

# 导入将查询参数转换为数据模型的类
from ...dependencies.utils import Query2Model

# 导入OV数据模型
from ...dataModels.vo import (
    Result,
    ConditionVO,

)

# 导入DTO数据模型类
from ...dataModels.dto import (
    PageDTO,
    ArchiveDTO
)

# 导入 配置常量
from ...configs.constant import (
    StatusConst,

)

# 导入所需 service
from ...services import (
    ArticleService,
)



ArticleRouter = APIRouter(
    prefix = "/articles",
    tags = ["Blog-Articles"],
    dependencies = []
)


@ArticleRouter.get(
    path = "/archives", description = "查看文章归档",
    response_model = Result[PageDTO[ArchiveDTO]]
)
async def listArchives(
    current: int = Query(
            1,
            description = "当前页码",
            ge = 1
        )
) -> Result[PageDTO[ArchiveDTO]]: 
    
    page_archives = await ArticleService().listArchives(current)
    ret_result = Result[PageDTO[ArchiveDTO]](
        flag = True,
        code = StatusConst.OK,
        message = "查询成功",
        data = page_archives,
    )

    return ret_result


@ArticleRouter.get(
    path = "", description = "查看首页文章",
    response_model = Result[List[ArticleHomeDTO]]
)
async def listArticles(
    current: int = Query(
        1,
        description = "当前页码",
        ge = 1
    )
) -> Result[List[ArticleHomeDTO]]:
    
    home_page_articles = await ArticleService().listArticles(current)
    ret_result = Result[List[ArticleHomeDTO]](
        flag = True,
        code = StatusConst.OK,
        message = "查询成功",
        data = home_page_articles
    )
    return ret_result


@ArticleRouter.get(
    path = "/{articleId}", description = "根据id查看文章"
)
async def getArticleById (
    articleId: int = Path(
            ... ,
            description = "文章id"
        )
):
    pass


@ArticleRouter.get(
    path = "/search", description = "搜索文章"
)
async def listArticlesBySearch(
    condition: ConditionVO = Depends(
            Query2Model(ConditionVO)
            # description = "搜索文章条件"
        )
):
    pass


@ArticleRouter.post(
    path = "/like", description = "点赞文章"
)
async def saveArticleLike(
    articleId: int = Query(
        ... ,
        description = "文章id"
    )
):
    pass

