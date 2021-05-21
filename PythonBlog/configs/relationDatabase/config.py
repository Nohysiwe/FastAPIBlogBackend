
from sqlalchemy.engine.url import URL, make_url
from starlette.datastructures import Secret

from .. import config




DB_DRIVER = config("DB_DRIVER", default="postgresql")
DB_HOST = config("DB_HOST", default="127.0.0.1")
DB_PORT = config("DB_PORT", cast=int, default=5432)
DB_USER = config("DB_USER", default="postgres")
DB_PASSWORD = config("DB_PASSWORD", cast=Secret, default="your_password")
DB_DATABASE = config("DB_DATABASE", default="Test_Blog")

# sqlalchemy连接数据库使用的类url的字符串
DB_DSN = config(
    "DB_DSN",
    cast=make_url,
    default=URL(
        drivername=DB_DRIVER,
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE,
    ),
)

# SQLAlchemy 所用参数 当前使用的是asyncpg 注释掉参数
# DB_ECHO = config("DB_ECHO", cast=bool, default=False)

# DB_USE_CONNECTION_FOR_REQUEST = config(
#     "DB_USE_CONNECTION_FOR_REQUEST", cast=bool, default=True
# )

# DB_RETRY_LIMIT = config("DB_RETRY_LIMIT", cast=int, default=1)
# DB_RETRY_INTERVAL = config("DB_RETRY_INTERVAL", cast=int, default=1)


# 连接是否使用 ssl连接 
# Pass True or an ssl.SSLContext instance to require an SSL connection. If True, a default SSL context returned by ssl.create_default_context() will be used. The value can also be one of the following strings:

# 'disable' - SSL is disabled (equivalent to False)
# 'prefer' - try SSL first, fallback to non-SSL connection if SSL connection fails
# 'allow' - currently equivalent to 'prefer'
# 'require' - only try an SSL connection. Certificate verification errors are ignored
# 'verify-ca' - only try an SSL connection, and verify that the server certificate is issued by a trusted certificate authority (CA)
# 'verify-full' - only try an SSL connection, verify that the server certificate is issued by a trusted CA and that the requested server host name matches that in the certificate.
# The default is 'prefer': try an SSL connection and fallback to non-SSL connection if that fails.

DB_SSL = config("DB_SSL", default=None)

# 连接池 大小设置
DB_POOL_MIN_SIZE = config("DB_POOL_MIN_SIZE", cast=int, default=1)
DB_POOL_MAX_SIZE = config("DB_POOL_MAX_SIZE", cast=int, default=4)

# asyncpg 特性(disposition)参数


# 连接池相关设置
# (1) 连接池中每个连接查询多少次后重新建立一个连接(默认50000次)
DB_POOL_CONNECTION_MAX_QUERIES = config("DB_POOL_CONNECTION_MAX_QUERIES", cast=int, default=50000)
# (2) 连接池中每个连接存在的最大时间(默认一小时)
DB_POOL_CONNECTION_MAX_LIFETIME = config("DB_POOL_CONNECTION_MAX_LIFETIME", cast=float, default=float(60*60))


# Connection 相关配置
# (1) SQL语句操作超时时间
DB_CONNECTION_COMMAND_TIMEOUT = config("DB_CONNECTION_OPERATION_TIMEOUT", cast=int, default=30)
# (2) Connection超时时间
DB_CONNECTION_TIMEOUT = config("DB_CONNECTION_TIMEOUT", cast=int, default=60)


__all__ = [
    "DB_DSN",
    # "DB_ECHO",
    # "DB_USE_CONNECTION_FOR_REQUEST",
    # "DB_RETRY_LIMIT",
    # "DB_RETRY_INTERVAL",
    "DB_SSL",
    "DB_POOL_MIN_SIZE",
    "DB_POOL_MAX_SIZE",
    "DB_POOL_CONNECTION_MAX_QUERIES",
    "DB_POOL_CONNECTION_MAX_LIFETIME",
    "DB_CONNECTION_COMMAND_TIMEOUT",
    "DB_CONNECTION_TIMEOUT",
]



