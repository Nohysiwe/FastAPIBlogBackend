
from typing import List
from fastapi import (
    APIRouter, 
    Path, 
    Query, 
    Body
)



CategoryRouter = APIRouter(
    prefix = "/categories",
    tags = ["Category"],
    dependencies = []
)



@CategoryRouter.get(
    path = "", description = "查看分类列表"
)
async def listCategories():
    pass


@CategoryRouter.get(
    path = "/categories/{categoryId}", description = "查看分类下对应的文章"
)
async def listArticlesByCategoryId(
    categoryId: int = Path(
            ... ,
            description= "分类id"
        ),
    current: int = Query(
            ... ,
            description = "当前页码"
        )
):
    pass





