

from pydantic import BaseModel, Field



__all__ = [
    "CategoryBackDTO",

]


class CategoryBackDTO(BaseModel):
    
    """
        后台分类列表
    """

    id: int = Field(
            ... ,
            title = "分类id",
            description = "后台分类id"
        )
    categoryName: str = Field(
            ... ,
            title = "分类名",
            description = "分类名"
        )
    