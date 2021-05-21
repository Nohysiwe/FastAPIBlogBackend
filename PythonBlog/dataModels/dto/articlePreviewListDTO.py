
from typing import List

from pydantic import BaseModel, Field

from .articlePreviewDTO import ArticlePreviewDTO



__all__ = [
    "ArticlePreviewListDTO",

]


class ArticlePreviewListDTO(BaseModel):
    
    """
        分类或标签下的文章列表
    """

    articlePreviewDTOList: List[ArticlePreviewDTO] = Field(
            ... ,
            title = "条件对应的文章列表",
            description = "条件对应的预览文章列表"
        )
    name: str = Field(
            ... ,
            title = "条件名",
            description = "条件名"
        )
