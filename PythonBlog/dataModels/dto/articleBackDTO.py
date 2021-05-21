
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from .tagDTO import TagDTO



__all__ = [
    "ArticleBackDTO",

]


class ArticleBackDTO(BaseModel):
    """
        后台文章
    """
    
    id: int = Field(
            ... ,
            title = "文章id",
            description = "后台文章id"
        )
    articleTitle: str = Field(
            ... ,
            title = "文章标题",
            description = "后台文章标题"
        )
    createTime: datetime = Field(
            ... ,
            title = "文章发表时间",
            description = "后台文章发表时间"
        )
    updateTime: datetime = Field(
            ... ,
            title = "文章更新时间",
            description = "后台文章更新时间"
        )
    likeCount: int = Field(
            0 ,
            title = "文章点赞量",
            description = "后台文章点赞量",
            ge = 0
        )
    viewsCount: int = Field(
            0 ,
            title = "文章浏览量" ,
            description = "后台文章浏览量",
            ge = 0
        )
    categoryName: str = Field(
            ... ,
            title = "文章分类名",
            description = "后台文章分类名"
        )
    tagDTOList: List[TagDTO] = Field(
            [] ,
            title = "文章标签",
            description = "文章标签列表"
        )
    isTop: int = Field(
            ... ,
            title = "是否置顶",
            description = "文章是否置顶"
        )
    isDraft: int = Field(
            ... ,
            title = "是否为草稿",
            description = "文章是否为草稿状态"
        )
    isDelete: int = Field(
            ... ,
            title = "是否删除",
            description = "文章是否删除"
        )
    
    