

from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field

# 导入 加盐的哈希算法
import bcrypt

from ...utils.userUtil import (
    UserUtil,
)



class UserAuth(BaseModel):
    """
        tb_user_auth 表结构
        用户账号
    """

    id: Optional[int] = Field(
        None,
        title = "id"
    )
    userInfoId: Optional[int] = Field(
        None,
        title = "用户信息id"
    )
    username: Optional[str] = Field(
        None,
        title = "用户名"
    )
    password: Optional[str] = Field(
        None,
        title = "密码"
    )
    loginType: Optional[int] = Field(
        None,
        title = "登录类型"
    )
    ipAddr: Optional[str] = Field(
        None,
        title = "用户登录ip"
    )
    ipSource: Optional[str] = Field(
        None,
        title = "ip来源"
    )
    createTime: Optional[datetime] = Field(
        None,
        title = "创建时间"
    )
    lastLoginTime: Optional[datetime] = Field(
        None,
        title = "最近登录时间"
    )
    


class NewUserAuth:
    """
        定制UserAuth数据模型
    """
    
    @staticmethod
    def Default() -> UserAuth:
        return UserAuth()
    
    
    @staticmethod
    def ByFourParams(
        userInfoId: int,
        username: str,
        password: str,
        loginType: int ) -> UserAuth:
        
        userauth = UserAuth(
            userInfoId = userInfoId,
            username = username,
            password = password,
            loginType = loginType,
            createTime = datetime.now()
        )
        return userauth
    
    @staticmethod
    def BySixParams(
        userInfoId: int,
        username: str,
        password: str,
        loginType: int,
        ipAddr: str,
        ipSource: str ) -> UserAuth:
        
        userauth = UserAuth(
            userInfoId = userInfoId,
            username = username,
            password = password,
            loginType = loginType,
            ipAddr = ipAddr,
            ipSource = ipSource,
            createTime = datetime.now(),
            lastLoginTime = datetime.now()
        )
        
        return userauth
    
    @staticmethod
    def ByTwoParams(
        ipAddr: str, 
        ipSource: str ) -> UserAuth:
        
        userauth = UserAuth(
            id = UserUtil.getLoginUser().id,
            ipAddr = ipAddr,
            ipSource = ipSource,
            lastLoginTime = datetime.now()
        )
        
        return userauth
    
    @staticmethod
    def ByOneParam(password: str) -> UserAuth:
        
        userauth = UserAuth(
            id = UserUtil.getLoginUser().id,
            # 因为只能 hash bytes类型 所以需转换下
            password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        )
        
        return userauth
    

__all__ = [
    "UserAuth",
    "NewUserAuth",
]