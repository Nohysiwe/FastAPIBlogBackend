
from typing import List, Optional, TypeVar, Generic
from pydantic import Field
from pydantic.generics import GenericModel

from ...configs.constant.statusConst import StatusConst



__all__ = [
    "Result",

]


DataT = TypeVar("DataT")

class Result(GenericModel, Generic[DataT]):
    
    """
        response 泛型数据模型
    """
    
    flag: bool = Field(
            True,
            description = "响应状态标识" 
        )
    code: int = Field(
            StatusConst.OK,
            description = "响应返回码"
        )
    message: str = Field(
            "操作成功",
            description = "响应简略信息"
        )
    data: Optional[DataT] = Field(
            None,
            description = "响应返回数据内容"
        )



