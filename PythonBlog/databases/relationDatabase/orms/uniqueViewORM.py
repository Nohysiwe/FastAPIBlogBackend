
from .. import DB_BASE as Base

from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy import Column, Integer, Sequence



class UniqueViewORM(Base):
    __tablename__ = 'tb_unique_view'
    __table_args__ = {'comment': '访问量表'}

    id = Column(Integer, Sequence("tb_unique_view_id_seq"), primary_key=True, comment='主键id')
    create_time = Column(TIMESTAMP(precision=0), nullable=False, comment='时间')
    views_count = Column(Integer, nullable=False, comment='访问量')


__all__ = ["UniqueViewORM"]