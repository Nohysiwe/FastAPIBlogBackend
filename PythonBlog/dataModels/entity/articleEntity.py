
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from ...utils.userUtil import (
    UserUtil,
)


from ..vo import (
    ArticleVO,

)


class Article(BaseModel):
    """
        Article 表结构
        文章
    """
    
    id: Optional[int] = Field(
        None,
        title = "id"
    )
    userId: Optional[int] = Field(
        None,
        title = "作者"
    )
    categoryId: Optional[int] = Field(
        None,
        title = "文章分类"
    )
    articleCover: Optional[str] = Field(
        None,
        title = "文章缩略图"
    )
    articleTitle: Optional[str] = Field(
        None,
        title = "标题"
    )
    articleContent: Optional[str] = Field(
        None,
        title = "内容"
    )
    createTime: Optional[datetime] = Field(
        None,
        title = "发表时间"
    )
    updateTime: Optional[datetime] = Field(
        None,
        title = "更新时间"
    )
    isTop: Optional[int] = Field(
        None,
        title = "是否置顶"
    )
    isDraft: Optional[int] = Field(
        None,
        title = "是否为草稿"
    )
    isDelete: Optional[int] = Field(
        None,
        title = "状态码"
    )


class NewArticle:
    """
        这段代码的样式结构 参考 go 语言的样式
        工厂模式返回定制的 Article 数据模型
    """
    @staticmethod
    def ByArticleVO(articleVO: ArticleVO) -> Article:
        
        article = Article(
            id = articleVO.id,
            userId = UserUtil.getLoginUser().userInfoId,
            categoryId = articleVO.categoryId,
            articleCover = articleVO.articleCover,
            articleTitle = articleVO.articleTitle,
            articleContent = articleVO.articleContent,
            createTime = datetime.now() if articleVO.id is None else None,
            updateTime = datetime.now() if articleVO.id is not None else None,
            isTop = articleVO.isTop,
            isDraft = articleVO.isDraft()
        )
        return article
    
    @staticmethod
    def ById(id: int) -> Article:
        
        article = Article(
            id = id,
            isTop = 0
        )
        return article
    
    @staticmethod
    def ByIdAndisTop(id: int , isTop: int):
        
        article = Article(
            id = id,
            isTop = isTop
        )
        return article
    
    @staticmethod
    def Default() -> Article:
        return Article()

        

__all__ = [
    "Article",
    "NewArticle",

]