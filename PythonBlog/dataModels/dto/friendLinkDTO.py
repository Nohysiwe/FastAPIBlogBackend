
from pydantic import BaseModel, Field



__all__ = [
    "FriendLinkDTO",

]


class FriendLinkDTO(BaseModel):
    
    """
        友链列表
    """
    
    id: int = Field(
            ... ,
            title = "友链id"
        )
    linkName: str = Field(
            ... ,
            title = "链接名"
        )
    linkAvatar: str = Field(
            ... ,
            title = "链接头像"
        )
    linkAddress: str = Field(
            ... ,
            title = "链接地址"
        )
    linkIntro: str = Field(
            ... ,
            title = "链接介绍"
        )