

from .. import DB_BASE as Base

from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy import Column, Integer, String, SmallInteger, Sequence, text


class UserInfoORM(Base):
    __tablename__ = 'tb_user_info'
    __table_args__ = {'comment': '用户信息表'}

    id = Column(Integer, Sequence("tb_user_info_id_seq"), primary_key=True, comment='用户id')
    user_role = Column(String(20), server_default=text("'user'::character varying"), comment='用户角色')
    nickname = Column(String(20), nullable=False, comment='用户昵称')
    avatar = Column(String(1024), nullable=False, comment='用户头像[链接]')
    intor = Column(String(255), server_default=text("NULL::character varying"), comment='用户简介')
    web_site = Column(String(255), server_default=text("NULL::character varying"), comment='个人网站')
    create_time = Column(TIMESTAMP(precision=0), nullable=False, comment='创建时间')
    is_silence = Column(SmallInteger, server_default=text("0"), comment='是否禁言')


__all__ = ["UserInfoORM"]