
from typing import List, Optional

from pydantic import BaseModel, Field



__all__ = [
    "CommentVO",

]


class CommentVO(BaseModel):
    
    """
        评论 数据模型
    """
    
    replyId: Optional[int] = Field(
            None,
            description = "回复用户id"
        )
    articleId: Optional[int] = Field(
            None,
            description = "评论文章id"
        )
    commentContent: str = Field(
            ... ,
            description = "评论内容"
        )
    parentId: Optional[int] = Field(
            ... ,
            description = "父评论id"
        )