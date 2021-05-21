
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


from ..vo import (
    MessageVO,

)



class Message(BaseModel):
    """
        tb_message 表结构
        留言
    """
    id: Optional[int] = Field(
        None,
        title = "主键id"
    )
    ipAddress: Optional[str] = Field(
        None,
        title = "用户ip"
    )
    ipSource: Optional[str] = Field(
        None,
        title = "用户地址"
    )
    nickname: Optional[str] = Field(
        None,
        title = "昵称"
    )
    avatar: Optional[str] = Field(
        None,
        title = "头像"
    )
    messageContent: Optional[str] = Field(
        None,
        title = "留言内容"
    )
    time: Optional[int] = Field(
        None,
        title = "弹幕速度"
    )
    createTime: Optional[datetime] = Field(
        None,
        title = "留言时间"
    )



class NewMessage:
    """
        定制 Meassage数据模型
    """
    
    @staticmethod
    def ByMessageVOipAddressAndipSource(
        messageVO: MessageVO,
        ipAddress: str,
        ipSource: str
    ) -> Message:
        
        message = Message(
            ipAddress = ipAddress,
            ipSource = ipSource,
            nickname = messageVO.nickname,
            avatar = messageVO.avatar,
            messageContent = messageVO.messageContent,
            time = messageVO.time,
            createTime = datetime.now()
        )
        
        return message
    
    
    @staticmethod
    def Default() -> Message:
        return Message()
    

__all__ = [
    "Message",
    "NewMessage",
]
        
    