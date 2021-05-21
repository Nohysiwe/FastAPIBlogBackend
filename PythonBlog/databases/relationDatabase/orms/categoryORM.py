
from .. import DB_BASE as Base

from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy import Column, Integer, String, Sequence, text



class CategoryORM(Base):
    __tablename__ = 'tb_category'
    __table_args__ = {'comment': '文章分类对象表'}

    id = Column(Integer, Sequence("tb_category_id_seq"), primary_key=True)
    category_name = Column(String(20), nullable=False, comment='分类名')
    create_time = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='创建时间')


__all__ = ["CategoryORM"]
