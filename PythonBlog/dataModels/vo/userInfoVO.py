
from typing import Optional

from pydantic import BaseModel, Field



__all__ = [
    "UserInfoVO",

]


class UserInfoVO(BaseModel):

    """
        用户信息 数据模型
    """ 
    
    nickname: str = Field(
            ... ,
            description = "昵称"
        )
    intro: Optional[str] = Field(
            None,
            description = "用户介绍"
        )
    webSite: Optional[str] = Field(
            None,
            description = "个人网站"
        )

