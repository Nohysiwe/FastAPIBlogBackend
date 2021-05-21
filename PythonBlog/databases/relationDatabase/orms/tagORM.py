
from .. import DB_BASE as Base

from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy import Column, Integer, String, Sequence, text



class TagORM(Base):
    __tablename__ = 'tb_tag'
    __table_args__ = {'comment': '文章标签表'}

    id = Column(Integer, Sequence("tb_tag_id_seq"), primary_key=True, comment='主键id')
    tag_name = Column(String(20), nullable=False, comment='标签名')
    create_time = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='创建时间')


__all__ = ["TagORM"]