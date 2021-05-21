
from typing import Optional
from pydantic import BaseModel, Field


class ArticleLike(BaseModel):
    
    """
        文章点赞记录
        tb_article_like
    """
    
    id: Optional[int] = Field(
        None,
        title = "id"
    )
    userId: Optional[int] = Field(
        None,
        title = "点赞用户"
    )
    articleId: Optional[int] = Field(
        None,
        title = "点赞文章"
    )

class NewArticleLike:
    

    @staticmethod
    def Default() -> ArticleLike:
        return ArticleLike()


__all__ = [
    "ArticleLike",
    "NewArticleLike",

]