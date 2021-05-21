

from .. import DB_BASE as Base

from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy import Column, Integer, String, SmallInteger, Sequence, text



class UserAuthORM(Base):
    __tablename__ = 'tb_user_auth'
    __table_args__ = {'comment': '用户认证表'}

    id = Column(Integer, Sequence("tb_user_auth_id_seq"), primary_key=True, comment='主键id')
    user_info_id = Column(Integer, nullable=False, comment='用户信息id')
    username = Column(String(50), nullable=False, comment='用户名')
    password = Column(String(100), nullable=False, comment='密码')
    login_type = Column(SmallInteger, nullable=False, comment='登陆类型')
    ip_addr = Column(String(50), server_default=text("NULL::character varying"), comment='用户登录ip')
    ip_source = Column(String(50), server_default=text("NULL::character varying"), comment='ip来源')
    create_time = Column(TIMESTAMP(precision=0), nullable=False, comment='创建时间')
    last_login_time = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='上次登录时间')


__all__ = ["UserAuthORM"]