
from typing import List, Dict

from ..dataModels.vo import (
    ArticleVO,
    ConditionVO,
    DeleteVO
)

from ..dataModels.dto import (
    PageDTO,
    ArchiveDTO,
    ArticleHomeDTO,
    ArticleBackDTO,
    ArticlePreviewListDTO,
    ArticleSearchDTO,
    ArticleDTO,
    ArticleOptionDTO,
    ArticlePreviewDTO,
    CategoryBackDTO,
    TagDTO,
)

# 导入常量值
from ..configs.constant import (
    DeleteConst,
    ArticleConst,
)

# 导入 数据库连接池对象
from ..databases.relationDatabase.relationDBCli import relation_db_cli
from ..databases.cacheDatabase.cacheDBCli import cache_db_cli

# 导入 Dao层逻辑操作
from ..daoOperation import (
    ArticleDao,
)

# 导入工具包
from ..utils.htmlUtil import HTMLUtil
from ..utils.translateUtil import translateHList2Dict



class ArticleService:
    """
        @description:
            文章相关操作具体实现
    """

    def __init__(self):
        pass


    async def listArchives(
                    self, 
                    current: int,
                    *,
                    capacity: int = 10
                ) -> PageDTO[ArchiveDTO]:
        """
            @description:
                查询文章归档
            @params:
                current 当前页码
                capacity 每页多少个数 默认为 10个
            @return:
                文章
        """
        # 查询的SQL语句
        sql = "select " \
            "id, " \
            "article_title as articleTitle, " \
            "create_time as createTime " \
            "from tb_article " \
            "where is_delete =$1 and is_draft=$2 " \
            "order by create_time desc;" 
            # "limit $3 offset $4;"
        
        # 计算起始向以及偏移段
        start_offset = (current - 1) * capacity -1 if current > 1 else 0
        
        # 声明 放置查询结果的数组
        archivedto_list: List[ArchiveDTO] = []
        
        async with relation_db_cli.pool.acquire() as conn:
            async with conn.transaction():
                await conn.cursor()
                async for record in conn.cursor(
                        sql,
                        DeleteConst.NORMAL,
                        ArticleConst.PUBLISH,
                        capacity,
                        start_offset):
                    archivedto_list.append(
                        ArchiveDTO.parse_obj(record)
                    )
        # 组装数据
        # :TODO 这里的count应该代表总数, 所以需要查询再查询一次表总数 
        ret_data = PageDTO[ArchiveDTO](
            recordList = archivedto_list,
            count = len(archivedto_list)
        )

        return ret_data


    async def listArticleBackDTO(
                    self,
                    condition: ConditionVO
                ) -> PageDTO[ArticleBackDTO]:
        """
            @description:
                查询后台文章
            @params:
                condition 条件
            @return:
                文章列表
        """
        # 转换页码
        condition.current = (condition.current - 1) * condition.size
        # sql语句 ==> 查询满足条件的文章数目
        article_dao = ArticleDao()
        async with relation_db_cli.pool.acquire() as conn:
            async with conn.transaction():
                # 查询文章总量
                article_counts = await article_dao.countArticleBacks(
                    condition, 
                    conn = conn, 
                    create_transaction = False )
                
                if article_counts == 0:
                    return PageDTO[ArticleBackDTO](count = 0)
                # 查询后台文章
                articlebackdto_list = await article_dao.listArtilceBacks(
                    condition,
                    conn = conn,
                    create_transaction = False )
        
        # 查询文章点赞量和浏览量
        with await cache_db_cli.pool as conn:
            # translateHList2Dict 
            # 是将 redis hgetall 命令返回的 list转为 dict/map
            views_count_map: List[str] = await conn.execute("hgetall", "article_views_count")
            like_count_map: List[str] = await conn.execute("hgetall", "article_like_count")
    
        # 转换数据格式 (从查询语句中单独拿出来的目的为了尽快释放连接池)
        views_count_map: Dict[str, int] = translateHList2Dict(
            views_count_map,
            valuetype_translater = int )
        like_count_map: Dict[str, int] = translateHList2Dict(
            like_count_map,
            valuetype_translater = int
        )

        # 封装点赞量和浏览量
        for articlebackdto in articlebackdto_list:
            articlebackdto.viewsCount = views_count_map.get(
                str(articlebackdto.id), 0 )
            articlebackdto.likeCount = like_count_map.get(
                str(articlebackdto.id), 0)

        ret_data = PageDTO[ArticleBackDTO](
            recordList = articlebackdto_list,
            count = article_counts
        )
        return ret_data


    async def listArticles(
                    self, 
                    current: int,
                    capacity: int = 10
                ) -> List[ArticleHomeDTO]:
        """
            @description:
                查询首页文章
            @params:
                current 当前页码
            @return:
                文章
        """
        # 转换页码查询  1 => 0, > 1 => (current - 1) * capacity
        current = (current - 1) * capacity if current > 1 else 0
        articlehomedto_list = await ArticleDao().listArticles(current)
        for articlehomedto in articlehomedto_list:
            articlehomedto.articleContent = HTMLUtil.deleteArticleTag(
                articlehomedto.articleContent )
                    
        return articlehomedto_list


    async def listArticlesByCondition(
                    self,
                    condition: ConditionVO
                ) -> ArticlePreviewListDTO:
        """
            @description:
                根据条件查询文章列表
            @params:
                condition 条件
            @return:
                文章
        """
        # 强制设置每页展示条数
        condition.size = 9
        # 转换页码
        condition.current = (condition.current - 1) * condition.size 

        async with relation_db_cli.pool.acquire() as conn:
            # 搜索条件对应数据
            articlePreviewdto_list: List[ArticlePreviewDTO] = await ArticleDao().listArticlesByCondition(
                condition,
                conn = conn, 
                create_transaction = True )
            # 搜索条件对应名(标签或分类名)
            search_condition_name: str = None
            if condition.categoryId is not None:
                # 搜索条件为类别
                sql = "select category_name from tb_category where id = $1;"
                async with conn.transaction():
                    search_condition_name = await conn.fetchval(sql, condition.categoryId, column=0)
            else:
                # 搜索条件为标签
                sql = "select tag_name from tb_tag where id = $1;"
                async with conn.transaction():
                    search_condition_name = await conn.fetchval(sql, condition.tagId, column=0)
        
        # 返回结果
        return ArticlePreviewListDTO(
            articlePreviewDTOList = articlePreviewdto_list,
            name = search_condition_name
        )


    # 暂时跳过
    async def listArticlesBySearch(
                    self,
                    condition: ConditionVO
                ) -> List[ArticleSearchDTO]:
        """
            @description:
                搜索文章
            @params:
                condition 条件
            @return:
                文章
        """
        raise NotImplementedError("NotImplemented !!!")
        
    # 暂时跳过
    async def getArticleBackById(
                    self,
                    articleId: int
                ) -> ArticleVO:
        """
            @description:
                根据id查看后台文章
            @parmas:
                articleId 文章id
            @return:
                文章
        """
        raise NotImplementedError("NotImplement !!!")


    # 涉及到 session统计访问数量 暂时跳过
    async def getArticleById(
                    self,
                    articleId: int
                ) -> ArticleDTO:
        """
            @description:
                根据id查看文章
            @params:
                articleId 文章id
            @return:
                文章
        """
        raise NotImplementedError("NotImplement !!!")
        


    async def listArticleOptionDTO() -> ArticleOptionDTO:
        """
            @description:
                查看文章分类标签选项
            @return:
                文章分类标签选项
        """

        categorydto_list: List[CategoryBackDTO] = []
        tagdto_list: List[TagDTO] = []
        async with relation_db_cli.pool.acquire() as conn:
            async with conn.transaction():
                # 查询文章分类选项
                category_sql = "select id, " \
                    "category_name as categoryName " \
                    "from tb_category;"
                async for record in conn.cursor(category_sql):
                    categorydto_list.append(
                        CategoryBackDTO.parse_obj(record))
                # 查询文章标签选项
                tag_sql = "select id, " \
                    "tag_name as tagName " \
                    "from tb_tag;"
                async for record in conn.cursor(tag_sql):
                    tagdto_list.append(
                        TagDTO.parse_obj(record))
        ret_data: ArticleOptionDTO = ArticleOptionDTO(
            tagDTOList = tagdto_list,
            categoryDTOList = categorydto_list
        )
        return ret_data
        
    # 保存操作 暂时跳过
    async def saveArticleLike(
                    self,
                    articleId: int
                ) -> None:
        """
            @description:
                点赞文章
            @params:
                articleId 文章id
        """
        
        raise NotImplementedError("NotImplement !!!")

    # 保存操作 暂时跳过
    async def saveOrUpdateArticle(
                    self,
                    articleVO: ArticleVO  
                ) -> None:
        """
            @description:
                添加或修改文章
            @params:
                文章对象
        """

        raise NotImplementedError("NotImplement !!!")

    # 保存操作 暂时跳过
    async def updateArticleTop(
                    self,
                    articleId: int,
                    isTop: int
                ) -> None:
        """
            @description:
                修改文章置顶
            @params:
                isTop 置顶状态值
                articleId 文章id
        """

        raise NotImplementedError("NotImplement !!!")

    # 保存操作 暂时跳过
    async def updateArticleDelete(
                    self,
                    deleteVO: DeleteVO
                ) -> None:
        """
            @description:
                删除或恢复文章
            @params:
                deleteVO 逻辑删除对象
        """
        
        raise NotImplementedError("NotImplement !!!")

    # 保存操作 暂时跳过
    async def deleteArticles(
                    self,
                    articleIdList: List[int]
                ) -> None:
        """
            @description:
                物理删除文章
            @oarams:
                articleIdList 文章id集合
        """
        
        raise NotImplementedError("NotImplement !!!")



__all__ = [
    "ArticleService",

]