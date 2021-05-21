from fastapi import FastAPI 

# 导入最上层路由
from .routers import MainRouter

# 导入事件初始化函数
from .eventFunctions import (
    addShutdownEventFunctions, 
    addStartupEventFunctions
)



def get_app():
    "BlogApp的工厂函数"

    BlogApp = FastAPI(
        title = "Nohysiwe's Blog",
        
        description = 
        """
        这个博客根据某个开源的博客(后端用Java的)迁移过来，原版的博客使用的是Java SpringBoot框架实现的，我用Python3.7 + FastAPI将其重写了一遍
        """,
        
        version = "0.0.1",
        on_startup = [],    
        on_shutdown = [],
        middleware = [],     # 里面必须是starlette.Middleware类型 
        reload = True       # 启动更改重新启动

    )

    # 初始化路由
    BlogApp.include_router(MainRouter)

    # 绑定APP 启动以及关闭时执行的 函数
    addStartupEventFunctions(app=BlogApp)
    addShutdownEventFunctions(app=BlogApp)

    # 绑定 App middleware (CORSMiddleWare 等一系列MiddleWare) 
    # 暂不需要, 无需实现

    return BlogApp



    






