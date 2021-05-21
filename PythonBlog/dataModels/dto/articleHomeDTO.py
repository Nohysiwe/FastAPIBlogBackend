
from datetime import datetime

from typing import List

from pydantic import BaseModel, Field

from .tagDTO import TagDTO



__all__ = [
    "ArticleHomeDTO",

]


class ArticleHomeDTO(BaseModel):
    """
        首页文章列表
    """
    
    id: int = Field(
            ... ,
            title = "id",
            description = "首页文章id"
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
    articleContent: str = Field(
            ... ,
            title = "文章内容",
            description = "文章内容"
        )
    createTime: datetime = Field(
            ... ,
            title = "文章发表时间",
            description = "文章发表时间",
        )
    isTop: bool = Field(
            ... ,
            title = "文章是否置顶",
            description = "文章是否置顶"
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