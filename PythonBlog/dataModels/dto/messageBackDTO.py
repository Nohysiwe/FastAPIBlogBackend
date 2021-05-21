
from datetime import datetime

from pydantic import BaseModel, Field



__all__ = [
    "MessageBackDTO",

]


class MessageBackDTO(BaseModel):
    """
        后台留言列表
    """
    
    id: int = Field(
            ... ,
            title = "主键id"
        )
    ipAddress: str = Field(
            ... ,
            title = "用户ip"
        )
    ipSource: str = Field(
            ... ,
            title = "用户ip地址"
        )
    nickname: str = Field(
            ... ,
            title = "昵称"
        )
    avatar: str = Field(
            ... ,
            title = "头像",
            description = "头像url" 
        )
    messageContent: str = Field(
            ... ,
            title = "留言内容",
            description = "留言内容"
        )
    createTime: datetime = Field(
            ... ,
            title = "留言时间",
            description = "留言时间"
        )


