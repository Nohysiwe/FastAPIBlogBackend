
from typing import Optional

from datetime import datetime

from pydantic import BaseModel, Field



__all__ = [
    "UserBackDTO",
]


class UserBackDTO(BaseModel):
    
    """
        后台用户列表
    """

    id: int = Field(
            ... ,
            title = "id"
        )
    userInfoId: int = Field(
            ... ,
            title = "用户信息id"
        )
    avatar: str = Field(
            ... ,
            title = "头像",
            description = "头像Url"
        )
    nickname: str = Field(
            ... ,
            title = "昵称"
        )
    userRole: str = Field(
            ... ,
            title = "用户角色"
        )
    loginType: int = Field(
            ... ,
            title = "登录类型"
        )
    ipAddr: str = Field(
            ... ,
            title = "用户登录ip"
        )
    ipSource: str = Field(
            ... ,
            title = "ip来源"
        )
    createTime: datetime = Field(
            ... ,
            title = "创建时间"
        )
    lastLoginTime: datetime = Field(
            ... ,
            title = "最近登录时间"
        )
    isSilence: int = Field(
            ... ,
            title = "用户评论状态"
        )
    status: Optional[int] = Field(
            None ,
            title = "状态"
        )


