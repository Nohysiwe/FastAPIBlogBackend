
from datetime import datetime

from typing import List
from pydantic import BaseModel, Field

from .tagDTO import TagDTO



__all__ = [
    "ArticlePreviewDTO",

]


class ArticlePreviewDTO(BaseModel):
    
    """
        分类或标签下的文章
    """

    id: int = Field(
            ... ,
            title = "文章id",
            description = "文章id"
        )
    articleCover: str = Field(
            ... ,
            title = "文章缩略图",
            description = "文章缩略图Url"
        )
    articleTitle: str = Field(
            ... ,
            title = "文章标题",
            description = "文章标题"
        )
    createTime: datetime = Field(
            ... ,
            title = "文章发表时间",
            description = "文章发表时间",
        )
    categoryId: int = Field(
            ... ,
            title = "文章分类id",
            description = "文章分类id"
        )
    categoryName: str = Field(
            ... ,
            title = "文章分类名",
            description = "文章分类名"
        )
    tagDTOList: List[TagDTO] = Field(
            [] ,
            title = "文章标签",
            description = "文章标签列表"
        )