
from pydantic import BaseModel
from fastapi import Request



class Query2Model:
    """
        从查询参数中获取参数,将其通过 pydantic 转换为指定的 model
    """

    def __init__(self, query_model: BaseModel) -> None:
        self._query_model = query_model


    def __call__(self, request: Request) -> BaseModel:        
        return self._query_model.parse_obj(request.query_params)




__all__ = [
    "Query2Model"
]