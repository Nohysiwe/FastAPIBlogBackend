
from PythonBlog.dataModels.vo import userRoleVO
import time

from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


from ...utils.userUtil import (
    UserUtil,
)

from ..vo import (
    UserInfoVO,
    UserRoleVO,

)


class UserInfo(BaseModel):
    """
        tb_user_info 数据结构
        用户信息
    """
    id: Optional[int] = Field(
            None ,
            title = "用户id"
        )
    userRole: Optional[str] = Field(
            None ,
            title = "用户角色"
        )
    nickname: Optional[str] = Field(
            None ,
            title = "用户昵称"
        )
    avatar: Optional[str] = Field(
            None ,
            title = "用户头像"
        )
    intro: Optional[str] = Field(
            None ,
            title = "用户简介"
        )
    webSite: Optional[str] = Field(
            None ,
            title = "个人网站"
        )
    isSilence: Optional[int] = Field(
            None ,
            title = "是否禁言"
        )
    createTime: Optional[datetime] = Field(
        None ,
        title = "创建时间"
    )



class NewUserInfo:
    """
        定制 UserInfo数据模型
    """
    @staticmethod
    def Default() -> UserInfo:
        userinfo = UserInfo(
            nickname = f"用户{int(time.time()*1000)}",
            createTime = datetime.now()
        )
    
    @staticmethod
    def ByNicknameAndAvatar(
        nickname: str, 
        avatar: str ) -> UserInfo:
        
        userinfo = UserInfo(
            nickname = nickname,
            avatar = avatar,
            createTime = datetime.now()
        )

        return userinfo
    
    @staticmethod
    def ByUserInfoVO(userInfoVO: UserInfoVO) -> UserInfo:
        
        userinfo = UserInfo(
            id = UserUtil.getLoginUser().userInfoId,
            nickname = userInfoVO.nickname,
            intro = userInfoVO.intro,
            webSite = userInfoVO.webSite
        )
        
        return userinfo
    
    @staticmethod
    def ByAvatar(avatar: str ) -> UserInfo:
        
        userinfo = UserInfo(
            id = UserUtil.getLoginUser().userInfoId,
            avatar = avatar
        )
        
        return userinfo
    
    @staticmethod
    def ByUserRoleVO(userRoleVO: UserRoleVO) -> UserInfo:
        
        userinfo = UserInfo(
            id = userRoleVO.userInfoId,
            nickname = userRoleVO.nickname,
            userRole = userRoleVO.userRole
        )
        return userinfo
    
    @staticmethod
    def ByIdAndisSilence(id: int, isSilence: int) -> UserInfo:

        userinfo = UserInfo(
            id = id,
            isSilence = isSilence
        ) 
        
        return userinfo
    
    

    __all__ = [
        "UserInfo",
        "NewUserInfo",
    ]