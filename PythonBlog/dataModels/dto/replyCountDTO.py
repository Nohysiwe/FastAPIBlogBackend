
from pydantic import BaseModel, Field



__all__ = [
    "ReplyCountDTO",

]


class ReplyCountDTO(BaseModel):
    """
        回复数量
    """

    commentId: int = Field(
            ... ,
            title = "评论id"
        )
    replyCount: int = Field(
            ... ,
            title = "回复数量"
        )


