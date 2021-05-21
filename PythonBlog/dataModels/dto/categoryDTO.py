
from typing import List, Optional
from pydantic import BaseModel, Field



__all__ = [
    "CategoryDTO",

]


class CategoryDTO(BaseModel):
    
    id: int = Field(
            ... ,
            description = "分类id"
        )
    categoryName: str = Field(
            ... ,
            description = "分类名"
        )
    articleCount: int = Field(
            ... ,
            description = "分类下的文章数量"
        )


