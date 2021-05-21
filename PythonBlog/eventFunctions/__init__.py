
from typing import List, Callable, Tuple
from fastapi import FastAPI

from ..utils.myPartial import myPartial

from .abstractEventFuncClass import AbstractEventFuncClass

# 导入 事件处理函数类
from .initiateRelattionDBPool import InitiateRelationDBPool
from .initateCacheDBPool import InitiateCacheDBPool


# app事件处理函数承载类
event_func_classes = [
    InitiateRelationDBPool,
    InitiateCacheDBPool,

]

def get_event_functions(event_func_name:str) -> List[Callable]:
    """
        从event_func_classes 获取 {event_func_name}函数的列表集合
    """
    ret_func_list: List[Callable] = []

    for event_func_class in event_func_classes:
        if issubclass(event_func_class, AbstractEventFuncClass):
            func = getattr(
                event_func_class,
                event_func_name, 
                None
            )
            if func:
                ret_func_list.append(func)
        else:
            raise TypeError(f"{event_func_class} is not a subclass of {AbstractEventFuncClass}")

    return ret_func_list
            

# 启动 时需要执行的操作 列表
startup_functions: List[Callable] = get_event_functions("startup") 

# 关闭服务器时需要执行的操作 列表
shutdown_functions: List[Callable] = get_event_functions("shutdown")


# 向 app 中增加事件处理函数
def addEventFunctions(app: FastAPI, 
                      event_type:str, 
                      event_functions:List[Callable] ) -> None:
    
    for func in event_functions:
        app.add_event_handler(event_type, myPartial(func, app=app))


# 用于app调用 绑定启动任务使用
addStartupEventFunctions = myPartial(addEventFunctions, 
                                    event_type = "startup",
                                    event_functions = startup_functions)


addShutdownEventFunctions = myPartial(addEventFunctions,
                                    event_type = "shutdown", 
                                    event_functions = shutdown_functions)


__all__ = [
    "startup_functions",
    "shutdown_functions",
    "addStartupEventFunctions",
    "addShutdownEventFunctions",
]
    


