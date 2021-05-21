
from datetime import datetime

from pydantic import BaseModel, Field



__all__ = [
    "FriendLinkBackDTO",

]


class FriendLinkBackDTO(BaseModel):

    """
        后台友链列表
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
    createTime: datetime = Field(
            ... ,
            title = "创建时间"
        )


