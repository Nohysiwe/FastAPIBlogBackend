
from typing import List, Optional
from pydantic import BaseModel, Field



__all__ = [
    "BlogHomeInfoDTO",

]


class BlogHomeInfoDTO(BaseModel):
    
    """
        博客首页信息数据模板
    """
    nickname:str = Field(
            ... ,
            description = "博主名称"
        )
    avatar: str = Field(
            ... ,
            description = "博主头像"
        )
    intro: str = Field(
            ... ,
            description = "博主简介"    
        )
    articleCount: int = Field(
            ... ,
            description = "文章数量"
        )
    categoryCount: int = Field(
            ... ,
            description = "分类数量"
        )
    tagCount: int = Field(
            ... ,
            description = "标签数量"
        )
    notice: str = Field(
            ... ,
            description = "公告"
        )
    viewsCount: str = Field(
            ... ,
            description = "访问量"
        )