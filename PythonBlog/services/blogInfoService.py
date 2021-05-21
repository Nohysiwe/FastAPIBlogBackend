from typing import Dict, Optional, List

# 导入 数据库连接池对象
from ..databases.relationDatabase.relationDBCli import relation_db_cli
from ..databases.cacheDatabase.cacheDBCli import cache_db_cli


from ..dataModels.dto import (
    BlogBackInfoDTO,
    BlogHomeInfoDTO,
    CategoryDTO,
    ArticleRankDTO,
)

from ..configs.constant import (
    UserConst,
)

from ..dataModels.entity import (
    Article, NewArticle,
)

from ..daoOperation import (
    UniqueViewDao,
    CategoryDao,
    ArticleDao,
)

from ..utils.translateUtil import (
    translateHList2Zip,
)

class BlogInfoService:

    """
        获取首页数据
        @return 博客首页信息
    """
    
    async def getBlogInfo(self) -> BlogHomeInfoDTO:
        """
            查询博客展示前台展示信息
        """
        async with relation_db_cli.pool.acquire() as conn:
            # (1) 查询博主信息
            async with conn.transaction():
                user_info = await conn.fetchrow(
                    "select avatar, nickname, intro " \
                    "from tb_user_info where id = $1;",
                    UserConst.BLOGGER_ID )
            # 没必要多此一举
            # userinfo: UserInfo = UserInfo.parse_obj(user_info)
            # (2) 查询文章数量
                article_count: int = await conn.fetchval(
                    "select count(1) from tb_article;" )
            # (3) 查询分类数量
                category_count: int = await conn.fetchval(
                    "select count(1) from tb_category;" )
            # (4) 查询标签数量
                tag_count: int = await conn.fetchval(
                    "select count(1) from tb_tag;" )
        # 下面使用redis 获取相关缓存数据
        with await cache_db_cli.pool as conn:
            # (5) 查询公告
            notice: Optional[str] = await conn.execute("get", "notice")
            # (6) 查询访问量
            views_count: Optional[str] = await conn.execute("get", "blog_views_count")
        
        # 当数据没有时处理数据
        if notice is None:
            notice = "发布你的第一篇公告吧"
        if views_count is None:
            views_count = "0"
        
        blog_homeinfo_dto = BlogHomeInfoDTO(
            nickname = user_info.nickname,
            avatar = user_info.avatar,
            intro = user_info.intro,
            articleCount = article_count,
            categoryCount = category_count,
            tagCount = tag_count,
            notice = notice,
            viewsCount = views_count
        )
        return blog_homeinfo_dto


    async def getBlogBackInfo(self) -> BlogBackInfoDTO:
        """
            查询博客后端展示信息
        """
        # (1)先进行数据库查询操作
        async with relation_db_cli.pool.acquire() as conn:
            async with conn.transaction():
                sql_template = "select count(1) from {0};"
                # <1> 查询留言量
                message_count = await conn.fetchval(
                    sql_template.format("tb_message") )
                # <2> 查询用户量
                user_count = await conn.fetchval(
                    sql_template.format("tb_user_info") )
                # <3> 查询文章量
                article_count = await conn.fetchval(
                    sql_template.format("tb_article") )
                # <4> 查询一周用户量
                unique_view_list: List[int] = await UniqueViewDao().listUniqueViews(
                    conn = conn,
                    create_transaction = False
                )
                # <5> 查询分类数据
                categorydto_list: List[CategoryDTO] = await CategoryDao.listCategoryDTO(
                    conn = conn,
                    create_transaction = False
                )
        # (2) 接着进行 redis查询操作
        with await cache_db_cli.pool as conn:
            # <1> 查询访问量
            views_count: Optional[str] = await conn.execute(
                "get", "blog_views_count" )
            # <2> 查询redis访问量前5的文章
            article_views_hlist: List[str] = await conn.execute(
                "hgetall", "article_views_count" )
        if views_count is not None:
            views_count: int = int(views_count)
        else:
            views_count: int = 0
        # 处理redis排行前 5
        article_views_hlist = translateHList2Zip(
            article_views_hlist, 
            valuetype_translater = int 
        ).sort(
            key=lambda x: x[1],
            reverse=True 
        )
        article_views_hlist = article_views_hlist[:5]
        article_views_map: Dict[str, int] = {
            key:value for key, value in article_views_hlist
        }
        # 文章排行为空则 直接返回
        if len(article_views_hlist):
            return BlogBackInfoDTO(
                viewsCount = views_count,
                messageCount = message_count,
                userCount = user_count,
                articleCount = article_count,
                categoryDTOList = categorydto_list,
                uniqueViewDTOList = unique_view_list,   
            )
        # 查询文章标题
        article_list: List[Article] = await ArticleDao().listArticleRank(
            [ int(item[0]) for item in article_views_hlist ]
        )

        articlerankdto_list: List[ArticleRankDTO] = []
        for article in article_list:
            articlerankdto_list.append(
                ArticleRankDTO(
                    articleTitle = article.articleTitle,
                    viewsCount = article_views_map[str(article.id)]
                )
            )
        blogbackinfodto = BlogBackInfoDTO(
            viewsCount = views_count,
            messageCount = message_count,
            userCount = user_count,
            articleCount = article_count,
            categoryDTOList = categorydto_list,
            uniqueViewDTOList = unique_view_list,
            articleRankDTOList = articlerankdto_list
        )
        return blogbackinfodto


    async def getAboutMe(self) -> str:
        """
            获取aboutme信息
        """
        with await cache_db_cli.pool as conn:
            about_me: Optional[str] = await conn.execute("get", "about")
        if about_me is None:
            about_me = ""
        
        return about_me


    async def updateAboutMe(
                self, 
                aboutContent: str ) -> None:
        """
            设置 aboutme信息
        """
        with await cache_db_cli.pool as conn:
            is_ok: str = await conn.execute(
                "set", 
                "about", 
                aboutContent )
        if is_ok != "OK":
            raise Exception("aboutme 设置失败")

    
    async def updateNotice(
                self,
                notice: str ) -> None:
        """
            设置公告信息
        """
        with await cache_db_cli.pool as conn:
            is_ok: str = await conn.execute(
                "set", 
                "notice", 
                notice )
        if is_ok != "OK":
            raise Exception("notice 设置失败")
    
    
    async def getNotice(self) -> str:
        """
            获取公告
        """
        with await cache_db_cli.pool as conn:
            notice: Optional[str] = await conn.execute(
                "get", 
                "notice" )
        if notice is None:
            notice = "发布你的第一篇公告吧"
        
        return notice
        

__all__ = [
    "BlogInfoService",
]