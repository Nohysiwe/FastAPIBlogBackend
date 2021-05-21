
from typing import Optional 
from pydantic import BaseModel, Field



__all__ = [
    "MessageVO",

]


class MessageVO(BaseModel):
    """
        留言 数据模型
    """

    nickname: str = Field(
            ... ,
            description = "昵称"
        )
    avatar: str = Field(
            ... ,
            description = "头像url"
        )
    messageContent: str = Field(
            ... ,
            description = "留言内容"
        )
    time: int = Field(
            ... ,
            description = "弹幕速度"
        )
    