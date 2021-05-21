
from typing import Optional
from pydantic import BaseModel, Field



__all__ = [
    "TagVO",

]


class TagVO(BaseModel):
    """
        标签 数据对象
    """
    
    id: Optional[int] = Field(
            None,
            description = "标签id"
        )
    
    tagName: str = Field(
            ... ,
            description = "标签名"
        )
    
