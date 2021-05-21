
from typing import List, Optional
from pydantic import BaseModel, Field



__all__ = [
    "FriendLinkVO",

]


class FriendLinkVO(BaseModel):
    
    """
        友链
    """
    id: Optional[int] = Field(
            None,
            description = "友链id"
        )
    linkName: str = Field(
            ... ,
            description = "友链名"
        )
    linkAvatar: str = Field(
            ... ,
            description = "链接头像地址"
        )
    linkAddress: str = Field(
            ... ,
            description = "链接地址"
        )
    linkIntro: str = Field(
            ... , 
            description = "链接介绍"
        )
    