from typing import List 
from pydantic import BaseModel, Field



__all__ = [
    "ArticleRankDTO",

]


class ArticleRankDTO(BaseModel):
    
    articleTitle: str = Field(
            ... ,
            description = "文章标题"
        )
    viewCount: int = Field(
            ... ,
            description = "文章浏览量"
        )

