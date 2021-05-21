
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from ..vo import (
    FriendLinkVO,

)



class FriendLink(BaseModel):
    """
        tb_friend_link 表结构
        友链列表
    """
    
    id: Optional[int] = Field(
        None,
        title = "id"
    )
    linkName: Optional[str] = Field(
        None,
        title = "链接名"
    )
    linkAvatar: Optional[str] = Field(
        None,
        title = "链接头像"
    )
    linkAddress: Optional[str] = Field(
        None,
        title = "链接地址"
    )
    linkIntro: Optional[str] = Field(
        None,
        title = "介绍"
    )
    createTime: Optional[datetime] = Field(
        None,
        title = "创建时间"
    )



class NewFriendLink:
    """
        定制 FriendLink 对象
    """
    @staticmethod
    def ByFriendLinkVO(friendLinkVO: FriendLinkVO) -> FriendLink:
        friendlink = FriendLink(
            id = friendLinkVO.id,
            linkName = friendLinkVO.linkName,
            linkAvatar = friendLinkVO.linkAvatar,
            linkAddress = friendLinkVO.linkAddress,
            linkIntro = friendLinkVO.linkIntro,
            createTime = datetime.now() if friendLinkVO.id is None else None 
        )
        
        return friendlink
    
    @staticmethod
    def ByFriendLinkIdAndisDelete(
        friendLinkId: int,
        isDelete: int ) -> FriendLink:
        
        friendlink = FriendLink(
            id = friendLinkId
        )
        
        return friendlink 
    
    @staticmethod
    def Default() -> FriendLink:
        return FriendLink()


__all__ = [
    "FriendLink",
    "NewFriendLink",

]

