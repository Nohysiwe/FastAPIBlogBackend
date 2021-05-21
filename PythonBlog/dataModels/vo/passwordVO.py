
from pydantic import BaseModel, Field



__all__ = [
    "PasswordVO",

]


class PasswordVO(BaseModel):
    
    """
        密码数据类型
    """

    oldPassword: str = Field(
            ... ,
            description = "旧密码"
        )
    
    newPassword: str = Field(
            ... ,
            description = "新密码",
            min_length = 6  # 最小不能少于6位
        )
    