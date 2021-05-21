
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


from ...utils.userUtil import (
    UserUtil,
)


from ..vo import (
    CommentVO,

)




class Comment(BaseModel):
    """
        Comment 表结构
        评论
    """
    
    id: Optional[int] = Field(
        None,
        title = "id"
    )
    userId: Optional[int] = Field(
        None,
        title = "评论用户Id"
    )
    replyId: Optional[int] = Field(
        None,
        title = "回复用户id"
    )
    articleId: Optional[int] = Field(
        None,
        title = "评论文章id"
    )
    commentContent: Optional[str] = Field(
        None,
        title = "评论内容"
    )
    createTime: Optional[datetime] = Field(
        None,
        title = "评论时间"
    )
    parentId: Optional[int] = Field(
        None,
        title = "父评论id"
    )
    isDelete: Optional[int] = Field(
        None,
        title = "状态码"
    )
    


class NewComment:
    """
        返回定制的Comment 数据模型
    """
    @staticmethod
    def ByCommentVO(commentVO: CommentVO) -> Comment:
        
        comment = Comment(
            userId = UserUtil.getLoginUser().userInfoId,
            replyId = commentVO.replyId,
            articleId = commentVO.articleId,
            commentContent = commentVO.commentContent,
            parentId = commentVO.parentId,
            createTime = datetime.now()
        )
        
        return comment

    @staticmethod
    def ByCommentIdAndisDelete(commentId: int, isDelete: int) -> Comment:
        
        comment = Comment(
            id = commentId,
            isDelete = isDelete
        )

        return comment
    

__all__ = [
    "Comment",
    "NewComment",

]