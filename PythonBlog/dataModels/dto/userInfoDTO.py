
from typing import Set, TypeVar, Generic

from pydantic import Field
from pydantic.generics import GenericModel



__all__ = [
    "UserInfoDTO",

]


ArticleLike = TypeVar("ArticleLike")
CommentLike = TypeVar("CommentLike")

class UserInfoDTO(
        GenericModel,
        Generic[
            ArticleLike, 
            CommentLike
        ]
            ):

    id: int = Field(
            ... ,
            title = "用户账号id"
        )
    userInfoId: int = Field(
            ... ,
            title = "用户信息id"
        )
    userRole: str = Field(
            ... ,
            title = "用户角色"
        )
    nickname: str = Field(
            ... ,
            title = "用户昵称"
        )
    avatar: str = Field(
            ... ,
            title = "用户头像"
        )
    intro: str = Field(
            ... ,
            title = "用户简介"
        )
    webSite: str = Field(
            ... ,
            title = "个人网站"
        )
    isSilence: int = Field(
            ... ,
            title = "用户禁言状态"
        )
    articleLikeSet: Set[ArticleLike] = Field(
            set() ,
            title = "点赞文章集合"
        )
    commentLikeSet: Set[CommentLike] = Field(
            set(),
            title = "点赞评论集合"
        )


