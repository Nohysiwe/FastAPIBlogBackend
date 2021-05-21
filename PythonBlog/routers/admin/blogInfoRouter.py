"""
    博客信息 Admin 管理
"""

from fastapi import (
    APIRouter, 
    Path, 
    Query, 
    Body
)


BlogInfoRouter = APIRouter(
    prefix = "/bloginfo",
    tags = ["BlogInfo"],
    dependencies = []
)


@BlogInfoRouter.put(
    path = "/aboutme/alter", description = "修改关于我的信息"
)
async def uodateAboutMe(
    aboutContent: str = Query(
        ... ,
        description = "修改的信息"
    )
):
    pass


@BlogInfoRouter.put(
    path = "/notice/alter", description = "修改公告"
)
async def updateBlogNotice(
    notice: str = Query(
        ... ,
        description= "公告内容"
    )
):
    pass

