

from typing import Optional
from fastapi import FastAPI


class AbstractEventFuncClass:
    """
        所有App事件处理方法类都应该继承自该类
    """
    @staticmethod
    async def startup(  *, 
                        app:FastAPI ) -> None:
        """
            App 启动时 执行的函数
        """
        raise NotImplementedError("这是抽象类的启动事件函数请勿调用 !!!")

    @staticmethod
    async def shutdown( *, 
                        app: Optional[FastAPI] = None ) -> None:
        """
            App 关闭时 执行的函数
        """
        raise NotImplementedError("这是抽象类的关闭事件函数请勿调用 !!!")