from datetime import datetime

from typing import List
from pydantic import BaseModel, Field

from .replyDTO import ReplyDTO



__all__ = [
    "CommentDTO",

]


class CommentDTO(BaseModel):
    """
        评论列表
    """
    
    id: int = Field(
            ... ,
            title = "评论id"
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
    replyCount: int = Field(
            0 ,
            title = "回复量"
        )
    replyDTOList: List[ReplyDTO] = Field(
            [] ,
            title = "回复列表"
        )
    
    