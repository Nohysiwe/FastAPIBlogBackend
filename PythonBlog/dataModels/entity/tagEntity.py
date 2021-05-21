
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from ..vo import (
    TagVO,

)


class Tag(BaseModel):
    """
        tb_tag 表结构
        标签
    """
    
    id: Optional[int] = Field(
        None,
        title = "id"
    )
    tagName: Optional[str] = Field(
        None,
        title = "标签名" 
    )
    createTime: Optional[datetime] = Field(
        None,
        title = "创建时间"
    )



class NewTag:
    """
        定制 Tag数据模型
    """

    @staticmethod
    def ByTagVO(tagVO: TagVO) -> Tag:
        tag = Tag(
            id = tagVO.id,
            tagName = tagVO.tagName,
            createTime = datetime.now() if tagVO.id is None else None
        )
        return tag


    @staticmethod
    def Default() -> Tag:
        return Tag()
    

__all__ = [
    "Tag",
    "NewTag",
]