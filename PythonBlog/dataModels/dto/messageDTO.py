
from pydantic import BaseModel, Field



__all__ = [
    "MessageDTO",

]


class MessageDTO(BaseModel):
    """
        留言列表
    """
    
    id: int = Field(
            ... ,
            title = "主键id"
        )
    nickname: str = Field(
            ... ,
            title = "昵称"
        )
    avatar: str = Field(
            ... ,
            title = "头像",
            description = "留言内容" 
        )
    messageContent: str = Field(
            ... ,
            title = "留言内容"
        )
    time: int = Field(
            ... ,
            title = "弹幕速度"
        )


