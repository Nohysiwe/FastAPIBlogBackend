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


@BlogInfoRouter.get(
    path = "", description = "查看博客信息"
)
async def getBlogHomeInfo():
    pass


@BlogInfoRouter.get(
    path = "/backendinfo", description = "查询博客后台信息"
)
async def getBlogBackInfo():
    pass


@BlogInfoRouter.get(
    path = "/aboutme", description = "查看关于我的信息"
)
async def getAboutMe():
    pass



@BlogInfoRouter.get(
    path = "/notice", description = "查看公告"
)
async def getBlogNotice():
    pass







