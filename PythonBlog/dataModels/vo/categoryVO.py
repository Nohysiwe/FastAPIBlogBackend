"""
    此OV确认无误
"""

from typing import Optional, List
from pydantic import BaseModel, Field



__all__ = [
    "CategoryVO",

]


class CategoryVO(BaseModel):
    
    id: Optional[int] = Field(
        None,
        description = "分类id"
    )
    
    categoryName: str = Field(
        ... ,
        description = "分类名"
    )
    