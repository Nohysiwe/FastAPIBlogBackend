
from .. import DB_BASE as Base

from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy import Column, Integer, String, Sequence



class FriendLinkORM(Base):
    __tablename__ = 'tb_friend_link'
    __table_args__ = {'comment': '友情连接表'}

    id = Column(Integer, Sequence("tb_friend_link_id_seq"), primary_key=True, comment='友情链接唯一id')
    link_name = Column(String(20), nullable=False, index=True, comment='链接名')
    link_avatar = Column(String(255), nullable=False, comment='链接头像')
    link_address = Column(String(50), nullable=False, comment='链接地址')
    link_intro = Column(String(50), nullable=False, comment='链接介绍')
    create_time = Column(TIMESTAMP(precision=0), nullable=False, comment='创建时间')


__all__ = ["FriendLinkORM"]
