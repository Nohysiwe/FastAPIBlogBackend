
from typing import List, TypeVar, Generic

import pydantic
from pydantic import Field
from pydantic.generics import GenericModel



__all__ = [
    "PageDTO",

]


T = TypeVar('T')

class PageDTO(GenericModel, Generic[T]):
    """
        分页列表
    """

    recordList: List[T] = Field(
            [] ,
            title = "分页列表"
        )
    count: int = Field(
            ... ,
            title = "总数",
            # ge = 0,   # 此加上会报错 pydantic尚未解决的 bug 
        )


