
from typing import Optional
from pydantic import BaseModel, Field


class ArticleTag(BaseModel):
    """
        tb_article_tag表结构
        标签
    """
    
    id: Optional[int] = Field(
        None,
        title = "id"
    )
    articleId: Optional[int] = Field(
        None,
        title = "文章id"
    )
    tagId: Optional[int] = Field(
        None,
        title = "标签id"
    )


class NewArticleTag:
    
    @staticmethod
    def ByArticleIdAndtagId(articleId: int, tagId: int) -> ArticleTag:
        
        articletag = ArticleTag(
            articleId = articleId,
            tagId = tagId
        )
        return articletag
    
    @staticmethod
    def Default() -> ArticleTag:
        return ArticleTag()


__all__ = [
    "ArticleTag",
    "NewArticleTag",

]
