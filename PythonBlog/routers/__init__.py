
from fastapi import APIRouter
from .admin import AdminRouter
from .blog import BlogRouter


# API起始路由
MainRouter = APIRouter(
    prefix = "/api",
    tags = ["Total-API"],
    dependencies = []
)

# 该路由下的子路由
sub_routers = [
    AdminRouter,
    BlogRouter,
]

# 将子路由添加到当前路由下
for sub_router in sub_routers:
    MainRouter.include_router(sub_router)
