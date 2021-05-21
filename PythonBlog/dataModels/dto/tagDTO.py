
from pydantic import BaseModel, Field



__all__ = [
    "TagDTO",

]


class TagDTO(BaseModel):
    """
        标签DTO数据类
    """
    
    id: int = Field(
            ... ,
            title = "标签id",
            description = "标签id"
        )
    tagName: str = Field(
            ... ,
            title = "标签名",
            description = "标签名"
        )
    