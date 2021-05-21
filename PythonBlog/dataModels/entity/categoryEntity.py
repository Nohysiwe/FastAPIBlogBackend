
from PythonBlog.dataModels.vo import categoryVO
from datetime import datetime

from typing import Optional
from pydantic import BaseModel, Field


from ..vo import (
    CategoryVO,

)



class Category(BaseModel):
    """
        tb_category 表结构
        分类
    """

    id: Optional[int] = Field(
        None,
        title = "id"
    )
    categoryName: Optional[str] = Field(
        None,
        title = "分类名"
    )
    createTime: Optional[datetime] = Field(
        None,
        title = "创建时间"
    )
    

class NewCategory:
    
    @staticmethod
    def ByCategoryOV(categoryVO: CategoryVO) -> Category:
        category = Category(
            id = categoryVO.id,
            categoryName = categoryVO.categoryName,
            createTime = datetime.now() if categoryVO.id is None else None
        )
        return category
    
    @staticmethod
    def Default() -> Category:
        return Category()


__all__ = [
    "Category",
    "NewCategory",

]