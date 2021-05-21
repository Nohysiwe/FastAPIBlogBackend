
from os import name
from ..dataModels.dto import (
    UserInfoDTO,

)



class UserUtil:
    
    # 暂时跳过
    @staticmethod
    def getLoginUser() -> UserInfoDTO:
        """
            获取调用该函数的用户的信息
        """
        return UserInfoDTO()