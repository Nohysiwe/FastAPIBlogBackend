from typing import Optional

from datetime import datetime

from pydantic import BaseModel, Field



__all__ = [
    "ReplyDTO",

]


class ReplyDTO(BaseModel):
    """
        回复列表
    """
    
    id: int = Field(
            ... ,
            title = "评论id"
        )
    parentId: Optional[int] = Field(
            None ,
            title = "父评论id"
        )
    userId: int = Field(
            ... ,
            title = "用户id"
        )
    nickname: str = Field(
            ... ,
            title = "用户昵称"
        )
    avatar: str = Field(
            ... ,
            title = "用户头像"
        )
    webSite: str = Field(
            ... ,
            title = "个人网站"
        )
    replyId: int = Field(
            ... ,
            title = "被回复用户id"
        )
    replyNickname: str = Field(
            ... ,
            title = "被回复用户昵称"
        )
    replyWebSite: str = Field(
            ... ,
            title = "被回复个人网站"
        )
    commentContent: str = Field(
            ... ,
            title = "评论内容"
        )
    likeCount: int = Field(
            0 ,
            title = "点赞数",

            ge = 0
        )
    createTime: datetime = Field(
            ... ,
            title = "评论时间",
            description = "评论时间"
        )