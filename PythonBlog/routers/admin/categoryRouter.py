
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


from ...dataModels.vo.conditionVO import ConditionVO
from ...dataModels.vo.categoryVO import CategoryVO



CategoryRouter = APIRouter(
    prefix = "/categories",
    tags = ["Category"],
    dependencies = []
)


@CategoryRouter.get(
    path = "", description = "查看后台分类列表"
)
async def listCategoryBackDTO(
    condition: ConditionVO = Depends(
        Query2Model(ConditionVO)
        # description= "查询条件"
    )
):
    pass


@CategoryRouter.post(
    path = "",
    description = "添加或修改分类"
)
async def saveOrUpdateCategory(
    categoryVO: CategoryVO = Body(
            ... ,
            description = "分类内容"
        )
):
    pass


@CategoryRouter.delete(
    path = "", description = "删除分类"
)
async def deleteCategories(
    categoryIdList: List[int] = Body(
        ... ,
        description = "分类id列表"
    )
):
    pass


