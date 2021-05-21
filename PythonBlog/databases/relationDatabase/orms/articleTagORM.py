
from .. import DB_BASE as Base

from sqlalchemy import Column, Integer, Sequence


class ArticleTagORM(Base):
    __tablename__ = 'tb_article_tag'
    __table_args__ = {'comment': '文章 标签关系表'}

    id = Column(Integer, Sequence("tb_article_tag_id_seq"), primary_key=True, comment='文章 标签关系id')
    article_id = Column(Integer, nullable=False, index=True, comment='文章id')
    tag_id = Column(Integer, nullable=False, index=True, comment='标签id')


__all__ = ["ArticleTagORM"]