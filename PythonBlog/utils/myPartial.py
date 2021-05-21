"""
    提供 将 coroutine函数转换为 被封装的 coroutine函数
    同时兼容 普通函数
"""

import asyncio
from types import FunctionType
from functools import partial


def myPartial(func, *args, **kwargs):
    """
        为常规函数或async函数设置参数默认值, 
        且返回修饰后的函数
    """
    if not asyncio.iscoroutinefunction(func):
        if not isinstance(func, FunctionType):
            raise TypeError("Funciton of asyncPartial need coroutinefunction or normal function !!!")
        else:
            # 如果是普通函数 直接返回partial的函数
            return partial(func, *args, **kwargs)
    else:
        async def wrapper():
            return await func(*args, **kwargs)        

        return wrapper


