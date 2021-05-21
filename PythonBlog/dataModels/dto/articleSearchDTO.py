
from pydantic import BaseModel, Field



__all__ = [
    "ArticleSearchDTO",

]


class ArticleSearchDTO(BaseModel):
    """
        文章搜索结果
    """
    
    id: int = Field(
            ... ,
            title = "文章id",
            description = "文章id"
        )
    articleTitle: str = Field(
            ... ,
            title = "文章标题",
            description = "搜索结果中文章标题"
        )
    articleContent: str = Field(
            ... ,
            title = "文章内容",
            description = "搜索结果中文章内容"
        )
    isDelete: int = Field(
            ... ,
            title = "文章状态",
            description = "文章是否是已删除状态"
        )


    
    