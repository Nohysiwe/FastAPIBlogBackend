
from .. import DB_BASE as Base

from sqlalchemy import Column, Integer, Sequence, Text



class BlogInfoORM(Base):
    __tablename__ = 'tb_blog_info'
    __table_args__ = {'comment': '博客简介信息表'}

    id = Column(Integer, Sequence("tb_blog_info_id_seq"), primary_key=True)
    about_content = Column(Text, nullable=False, comment='关于我的内容')


__all__ = ["BlogInfoORM"]