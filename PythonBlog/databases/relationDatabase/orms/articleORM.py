
from sqlalchemy import Column, Index, Integer, SmallInteger, String, Text, text, Sequence
from sqlalchemy.dialects.postgresql import TIMESTAMP

from .. import DB_BASE as Base


class ArticleORM(Base):
    __tablename__ = 'tb_article'
    __table_args__ = (
        Index('fk_title_content', 'article_title', 'article_content'),
        {'comment': '文章结构表'}
    )

    id = Column(Integer, Sequence("tb_article_id_seq"), primary_key=True, comment='文章id')
    user_id = Column(Integer, nullable=False, index=True, comment='作者id')
    category_id = Column(Integer, index=True, comment='文章分类')
    article_cover = Column(String(1024), server_default=text("NULL::character varying"), comment='文章缩略图地址')
    article_title = Column(String(50), nullable=False, comment='文章标题')
    article_content = Column(Text, nullable=False, comment='文章内容')
    create_time = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='发表时间')
    update_time = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    is_top = Column(SmallInteger, comment='是否置顶')
    is_draft = Column(SmallInteger, server_default=text("0"), comment='是否为草稿')
    is_delete = Column(SmallInteger, server_default=text("0"), comment='是否删除')


__all__ = ["ArticleORM"]

