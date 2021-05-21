from typing import List
from fastapi import (
    APIRouter, 
    Path, 
    Query, 
    Body,
    File,
    UploadFile,
    Depends
)

# 导入将查询参数转换为数据模型的类
from ...dependencies.utils import Query2Model


# 导入VO
from ...dataModels.vo import (
    ConditionVO,
    ArticleVO,
    DeleteVO,
    Result
)

# 导入DTO数据模型类
from ...dataModels.dto import (
    PageDTO,
    ArchiveDTO,
    ArticleBackDTO,
    ArticleOptionDTO

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
    tags = ["Admin-Articles"],
    dependencies = []
)



@ArticleRouter.get(
    path = "", description = "按条件查看后台文章 #### 请不要使用测试的页面API对其进行测试",
    response_model = Result[PageDTO[ArticleBackDTO]]
)
async def listArticleBackDTO(
    conditionVO: ConditionVO = Depends(
            Query2Model(ConditionVO)
            # description = "筛选条件"
        )
) -> Result[PageDTO[ArticleBackDTO]]:
    
    page_back_articles = await ArticleService().listArticleBackDTO(conditionVO)
    ret_result = Result[PageDTO[ArticleBackDTO]](
        flag = True,
        code = StatusConst.OK,
        message = "查询成功",
        data = page_back_articles
    )
    return ret_result



@ArticleRouter.post(
    path = "", description = "添加或修改文章",
)
async def saveArticle(
    articleVO: ArticleVO = Body(
            ...,
            description = "添加或修改文章的配置信息"
        )
):
    pass



@ArticleRouter.delete(
    path = "",
    description = "物理删除文章"
)
async def deleteArticles(
    articleIdList: List[int] = Body(
            ... ,
            description = "删除文章的id列表"
        )
):
    pass


# 暂未实现逻辑
@ArticleRouter.put(
    path = "", description = "恢复或删除文章"
)
async def updateArticleDelete(
    deleteVO: DeleteVO = Depends(
            Query2Model(DeleteVO)
            # description = "操作的文章目标"
        )
):
    pass



@ArticleRouter.get(
    path = "/options", description = "查看文章选项",
    response_model = Result[ArticleOptionDTO]
)
async def listArticleOptionDTO() -> Result[ArticleOptionDTO]:
    pass 



@ArticleRouter.put(
    path = "/top/{articleId}", description = "修改文章置顶"
)
async def updateArticleTop(
    articleId: int = Path(
            ..., 
            description = "被修改文章的id"    
        ),
    isTop: int = Query(
            ..., 
            description = "修改为置顶/不置顶" 
        )
):
    pass 



@ArticleRouter.post(
    path = "/images", description = "上传文章图片"
)
async def saveArticleImages(
    file: UploadFile = File(
            ...,
            description = "上传的文章图片" 
        )
):
    pass



@ArticleRouter.get(
    path = "/{articleId}",
    description = "根据id查看后台文章"
)
async def getArticleBackById(
    articleId: int = Path(
            ... ,
            description = "文章id"
        )
):
    pass

