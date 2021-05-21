from fastapi import APIRouter
from .articleRouter import ArticleRouter
from .blogInfoRouter import BlogInfoRouter
from .categoryRouter import CategoryRouter


# 博客路由
BlogRouter = APIRouter(
    prefix = "/blog",
    tags = ["Blog"],
    dependencies = []
)

# 该路由下的子路由
sub_routers = [
    ArticleRouter,
    BlogInfoRouter,
    CategoryRouter,
]

# 将子路由添加到当前路由下
for sub_router in sub_routers:
    BlogRouter.include_router(sub_router)


