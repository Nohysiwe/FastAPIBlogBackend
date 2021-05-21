"""
    处理分页问题
    获取数据分页的数据并返回结果集以及结果集常数
"""
from typing import Awaitable, List 

import asyncpg
from asyncpg import Record
from asyncpg.cursor import Cursor

from pydantic import (
    BaseModel, 
    Field,
)

class PageParam(BaseModel):
    
    current: int = Field(
        1,
        titile = "当前页",
        ge = 1
    )
    capacity: int = Field(
        10,
        titile = "每页容量",
        ge = 1
    )
    data: List[Record] = Field(
        [],
        titile = "返回的数据列表"
    )
    total: int = Field(
        0,
        title = "查询结果总量",
        ge = 0
    )


async def GetPageData(
    cursor: Cursor,
    *,
    current: int = 1,
    capacity: int = 10 ) -> PageParam: 
    """
        从Cursor对象中
        取指定页指定条数据   
    """
    page_data = PageParam(
        current = current,
        capacity = capacity
    )
    total = 0
    if current > 1:
        require_forward_num: int = (current - 1) * capacity
        real_forward_num: int = await cursor.forward(require_forward_num)
        # 当结果 不一致时 
        # 说明 查询总条数就比要求的少 此时应该返回对应的数据
        if real_forward_num != require_forward_num:
            page_data.total = real_forward_num
            return page_data
        else:
            total += real_forward_num
    # 获取指定数据    
    fetch_data: List[Record] = await cursor.fetch(capacity)
    
    raise NotImplementedError("尚未实现完全")
            
    