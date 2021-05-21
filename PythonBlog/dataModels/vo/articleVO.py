from typing import Optional, List
from pydantic import BaseModel, Field



__all__ = [
    "ArticleVO",

]


class ArticleVO(BaseModel):
    
    id: Optional[int] = Field(
        None,
        description = "文章id"
    )
    articleTitle: str = Field(
        ... , 
        description = "文章标题"
    )
    articleContent: str = Field(
        ... ,
        description = "文章内容"
    )
    articleCover: Optional[str] = Field(
        None,
        description = "文章缩略图url"
    )
    categoryId: Optional[int] = Field(
        None,
        description = "文章分类",
    )
    tagIdList: List[int] = Field(
        [],
        description = "文章标签"
    )
    isTop: Optional[int] = Field(
        None,
        description = "是否置顶"
    )
    isDraft: Optional[int] = Field(
        None,
        description = "是否为草稿"
    )
