
from typing import Optional

from pydantic import BaseModel, Field



__all__ = [
    "UserRoleVO",

]


class UserRoleVO(BaseModel):
    
    """
        用户权限 数据模型
    """
    
    userInfoId: int = Field(
            ... ,
            description = "用户信息id"
        )
    nickname: str = Field(
            ... ,
            description = "用户昵称"
        )
    userRole: str = Field(
            ... ,
            description = "用户权限"
        )

