
from datetime import datetime

from typing import List

from pydantic import BaseModel, Field



__all__ = [
    "CommentBackDTO",

]


class CommentBackDTO(BaseModel):
    """
        后台评论列表
    """
    id: int = Field(
            ... ,
            title = "id"
        )
    avatar: str = Field(
            ... ,
            title = "用户头像"
        )
    nickname: str = Field(
            ... ,
            title = "用户昵称" 
        )
    replyNickName: str = Field(
            ... ,
            title = "回复用户昵称"
        )
    articleTitle: str = Field(
            ... ,
            title = "文章标题",
            description = "文章标题"
        )
    commentContent: str = Field(
            ... ,
            title = "评论内容"
        )
    likeCount: int = Field(
            0 ,
            title = "点赞量",

            ge = 0
        )
    createTime: datetime = Field(
            ... ,
            title = "发表时间",
            description = "文章发表时间"
        )
    isDelete: int = Field(
            ... ,
            title = "是否删除",
            description = "文章是否删除"
        )