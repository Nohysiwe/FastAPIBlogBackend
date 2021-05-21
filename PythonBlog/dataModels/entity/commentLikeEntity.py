
from typing import Optional
from pydantic import BaseModel, Field



class CommentLike(BaseModel):
    """
        tb_comment_like 表
        评论点赞
    """
    
    id: Optional[int] = Field(
        None,
        title = "id"
    )
    userId: Optional[int] = Field(
        None,
        title = "点赞用户"
    )
    commentId: Optional[int] = Field(
        None,
        title = "点赞评论"
    )


class NewCommentLike:
    
    @staticmethod
    def Default() -> CommentLike:
        return CommentLike()


__all__ = [
    "CommentLike",
    "NewCommentLike",

]