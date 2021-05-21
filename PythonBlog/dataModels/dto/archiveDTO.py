
from typing import Optional, List

from pydantic import BaseModel, Field

from datetime import datetime



__all__ = [
    "ArchiveDTO",

]


class ArchiveDTO(BaseModel):
    
    """
        归档文章
    """
    
    id: Optional[int] = Field(
            None,
            description = "文章id"
        )
    articleTitle: Optional[str] = Field(
            None,
            description = "文章标题"
        )
    createTime: Optional[datetime] = Field(
            None,
            description = "发表时间"
        )


