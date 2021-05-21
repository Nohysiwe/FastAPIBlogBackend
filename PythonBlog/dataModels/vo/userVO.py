
from typing import Optional
from pydantic import BaseModel, Field, EmailStr



__all__ = [
    "UserVO",

]


class UserVO(BaseModel):
    
    """
        用户注册
    """

    username: EmailStr = Field(
            ... ,
            title = "用户名",
            description = "用户名 使用邮箱格式"
        )
    password: str = Field(
            ... ,
            title = "用户密码",
            description = "用户密码",
            min_length = 6
        )
    code: str = Field(
            ... ,
            title = "验证码",
            description = "邮箱验证码"
        )

