
from .. import DB_BASE as Base

from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy import Column, Integer, String, Sequence, Text, SmallInteger, text



class CommentORM(Base):
    __tablename__ = 'tb_comment'
    __table_args__ = {'comment': '评论内容表'}

    id = Column(Integer, Sequence("tb_comment_id_seq"), primary_key=True, comment='评论唯一id')
    user_id = Column(Integer, nullable=False, index=True, comment='评论用户id')
    article_id = Column(Integer, index=True, comment='评论文章id')
    comment_content = Column(Text, nullable=False, comment='评论内容')
    create_time = Column(TIMESTAMP(precision=0), nullable=False, comment='评论时间')
    reply_id = Column(Integer, comment='回复用户id')
    parent_id = Column(Integer, index=True, comment='父评论id')
    is_delete = Column(SmallInteger, server_default=text("0"), comment='是否删除')


__all__ = ["CommentORM"]