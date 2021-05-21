
from typing import List, TypeVar
from pydantic import BaseModel, Field

from .categoryDTO import CategoryDTO
from .articleRankDTO import ArticleRankDTO



__all__ = [
    "BlogBackInfoDTO",

]


class BlogBackInfoDTO(BaseModel):

    """
        博客后台信息 数据模型 
    """

    viewsCount: int = Field(
            ... ,
            title = "访问量" 
        )
    messageCount: int = Field(
            ... ,
            title = "留言量" 
        )
    userCount: int = Field(
            ... , 
            title = "用户量" 
        )
    articleCount: int = Field(
            ... ,
            title = "文章量" 
        )
    categoryDTOList: List[CategoryDTO] = Field(
            [], 
            title = "分类统计"
        )
    uniqueViewDTOList: List[int] = Field(
            ... ,
            title = "一周用户量集合"
        )
    articleRankDTOList: List[ArticleRankDTO] = Field(
            [],
            title = "文章浏览量排行"
        )
    