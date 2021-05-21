"""
    OV检测无误
"""
from typing import Optional
from pydantic import BaseModel, Field



__all__ = [
    "ConditionVO",
    
]


class ConditionVO(BaseModel):
    
    categoryId: Optional[int] = Field(
        None,
        description = "分类id"
    )
    tagId: Optional[int] = Field(
        None, 
        description = "标签id"
    )
    current: int = Field(
        1 ,
        description = "当前页码", 
        gt = 0      # 页码数最小为 1 
    )
    size: int = Field(
        10 , 
        description = "显示数量",
        ge = 1
    )
    keywords: Optional[str] = Field(
        None, 
        description = "搜索内容"
    )
    isDelete: Optional[int] = Field(
        None, 
        description = "是否删除"
    )
    isDraft: Optional[int] = Field(
        None, 
        description = "草稿状态"
    )


