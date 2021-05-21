"""
    OV验证无误
"""


from typing import List
from pydantic import BaseModel, Field



__all__ = [
    "DeleteVO",
    
]


class DeleteVO(BaseModel):
    """
        逻辑删除
    """
    idList: List[int] = Field(
        ... ,
        description = "id列表"
    )
    
    isDelete: int = Field(
        ... ,
        description = "删除状态"
    )
    

    