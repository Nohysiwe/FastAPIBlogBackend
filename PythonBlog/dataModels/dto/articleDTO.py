
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field
from .tagDTO import TagDTO



__all__ = [
    "ArticleDTO",

]


class ArticleDTO(BaseModel):
    """
        文章数据模型对象
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
    articleContent: str = Field(
            ... ,
            title = "文章内容",
            description = "文章内容"
        )
    likeCount: int = Field(
            ... ,
            title = "文章点赞量",
            description = "文章点赞量",
            ge = 0
        )
    viewsCount: int = Field(
            ... ,
            title = "文章浏览量",
            description = "文章浏览量",
            ge = 0 
        )
    createTime: datetime = Field(
            ... ,
            title = "文章发表时间",
            description = "文章发表时间",
        )
    updateTime: datetime = Field(
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

