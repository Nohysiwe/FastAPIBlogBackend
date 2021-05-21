
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field



class UniqueView(BaseModel):
    """
        tb_unique_view 表结构
        网站访问量
    """
    
    id: Optional[int] = Field(
        None,
        title = "id"
    )
    createTime: Optional[datetime] = Field(
        None,
        title = "时间"
    )
    viewsCount: Optional[int] = Field(
        None,
        title = "访问量"
    )


class NewUniqueView:
    """
        定制UniqueView 数据模型
    """
    
    @staticmethod
    def ByCreateTimeAndviewsCount(
        createTime: datetime,
        viewsCount: int
    ) -> UniqueView:
        
        uniqueview = UniqueView(
            createTime = createTime,
            viewsCount = viewsCount
        )
        
        return uniqueview


    @staticmethod
    def Default() -> UniqueView:
        return UniqueView()


__all__ = [
    "UniqueView",
    "NewUniqueView",

]