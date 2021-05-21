
from starlette.datastructures import Secret

from .. import config


CACHE_DB_NAME = config("CACHE_DB_NAME", default="redis")
CACHE_DB_HOST = config("CACHE_DB_HOST", default="localhost")
CACHE_DB_PORT = config("CACHE_DB_PORT", cast=int, default=6379)
CACHE_DB_PASSWORD = config("CACHE_DB_PASSWORD", cast=Secret, default="your_password")

CACHE_DB_USE_DB = config("CACHE_DB_NAME", cast=int, default=0)
CACHE_DB_ENCODING = config("CACHE_DB_ENCODING", cast=str, default="utf-8")
CACHE_DB_POOL_MINSIZE = config("CACHE_DB_POOL_MINSIZE", cast=int, default=1)
CACHE_DB_POOL_MAXSIZE = config("CACHE_DB_POOL_MAXSIZE", cast=int, default=2)
CACHE_DB_CREATE_CONNECTION_TIMEOUT = config("CACHE_DB_CREATE_CONNECTION_TIMEOUT", cast=float, default=15) 





__all__ = [
    "CACHE_DB_HOST",
    "CACHE_DB_PORT",
    "CACHE_DB_PASSWORD",
    "CACHE_DB_USE_DB",
    "CACHE_DB_ENCODING",
    "CACHE_DB_POOL_MINSIZE",
    "CACHE_DB_POOL_MAXSIZE",
    "CACHE_DB_CREATE_CONNECTION_TIMEOUT",
]
