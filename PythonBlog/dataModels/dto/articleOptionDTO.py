
from typing import List

from pydantic import BaseModel, Field

from .tagDTO import TagDTO
from .categoryBackDTO import CategoryBackDTO



__all__ = [
    "ArticleOptionDTO",

]


class ArticleOptionDTO(BaseModel):
    
    """
        文章选项
    """
    
    tagDTOList: List[TagDTO] = Field(
            [] ,
            title = "文章标签列表",
            description = "文章标签列表"
        )
    categoryDTOList: List[CategoryBackDTO] = Field(
            [],
            title = "文章分类列表",
            description = "文章分类列表"
        )
    
    