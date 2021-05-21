
from .. import DB_BASE as Base

from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy import Column, Integer, String, SmallInteger, Sequence


class MessageORM(Base):
    __tablename__ = 'tb_message'
    __table_args__ = {'comment': 'Message表'}

    id = Column(Integer, Sequence("tb_message_id_seq"), primary_key=True, comment='主键id')
    ip_address = Column(String(50), nullable=False, comment='用户ip')
    ip_source = Column(String(255), nullable=False, comment='用户地址')
    nickname = Column(String(255), nullable=False, comment='昵称')
    avatar = Column(String(255), nullable=False, comment='头像')
    message_content = Column(String(255), nullable=False, comment='留言内容')
    time = Column(SmallInteger, nullable=False, comment='弹幕速度')
    create_time = Column(TIMESTAMP(precision=0), nullable=False, comment='发布时间')


__all__ = ["MessageORM"]
