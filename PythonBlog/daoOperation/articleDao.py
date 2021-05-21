from typing import List, Optional

from asyncpg import Connection

# 导入数据库连接池
from ..databases.relationDatabase.relationDBCli import relation_db_cli

from ..dataModels.dto import (
    ArticleDTO,
    ArticleHomeDTO,
    ArticlePreviewDTO,
    ArticleBackDTO,
    TagDTO,

)
from ..dataModels.vo import (
    ConditionVO
)

from ..dataModels.entity import(
    Article, NewArticle,
)


class ArticleDao:
    
    def __init__(self):
        pass
    

    async def listArticles(
        self,
        current: int, 
        page_capacity: int = 10,
        *, 
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> List[ArticleHomeDTO]:
        """
            查询首页文章
            @param current 当前页码
            @param conn 如果 不为空代表自建connection连接
            @param create_transaction：
                    代表 是否函数自建create_transaction, 
                    如果conn == None, create_transaction 强制设为 True
            @return 首页文章集合
            @
        """
        sql = "select " \
            "a.id, article_cover, article_title, " \
            "article_content, a.create_time, a.is_top, " \
            "a.category_id, category_name, " \
            "t.id as tag_id, t.tag_name " \
            "from (" \
            "select " \
            "id, article_cover, article_title, article_content, " \
            "is_top, create_time, category_id " \
            "from tb_article " \
            "where is_delete = 0 " \
            "and is_draft = 0 " \
            "order by is_top desc, id desc " \
            "limit $1 offset $2) as a " \
            "join tb_category as c on a.category_id = c.id " \
            "join tb_article_tag as atg on a.id = atg.article_id " \
            "join tb_tag as t on t.id = atg.tag_id " \
            "order by a.is_top desc, a.id desc;"

        ret_data = {}
        # async with relation_db_cli.pool.acquire() as conn:
        release_signal = False
        if conn is None:
            conn: Connection = await relation_db_cli.pool.acquire()
            release_signal = True
            create_transaction = True
        try:
            if create_transaction:
                tr = conn.transaction()
                await tr.start()
            try:
                async for record in conn.cursor(
                        sql,
                        page_capacity,
                        current):
                    data_item = ret_data.get(record.id)
                    if not data_item:
                        data_item: ArticleHomeDTO = ArticleHomeDTO(
                            id = record.id,
                            articleCover = record.article_cover,
                            articleTitle = record.article_title,
                            articleContent = record.article_content,
                            createTime = record.create_time,
                            isTop = record.is_top,
                            categoryId = record.category_id,
                            categoryName = record.category_name)
                    ret_data[record.id] = data_item
                    # 将DTO数据放入对应数组中
                    data_item.tagDTOList.append(
                        TagDTO(
                            id = record.tag_id,
                            tagName = record.tag_name 
                        ) 
                    )
            except:
                if create_transaction:
                    await tr.rollback()
                raise
            else:
                if create_transaction:
                    await tr.commit()
        finally:
            if release_signal:
                await relation_db_cli.pool.release(conn)
            
        return list(ret_data.values())


    async def getArticleById(
        self,
        articleId: int,
        *, 
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> Optional[ArticleDTO]:
        """
            根据id查询文章
            @param articleId 文章id
            @return 文章
        """
        sql = "select a.id, article_cover, article_title, " \
            "article_content, a.create_time, a.update_time, " \
            "a.category_id, t.id as tag_id, t.tag_name " \
            "from tb_article as a " \
            "join tb_category as c on a.category_id = c.id " \
            "join tb_article_tag as atg on a.id = atg.article_id " \
            "join tb_tag as t on t.id = atg.tag_id " \
            "where a.id = $1;"
        ret_data = {}
        # async with relation_db_cli.pool.acquire() as conn:
        release_signal = False
        if conn is None:
            conn: Connection = await relation_db_cli.pool.acquire()
            release_signal = True
            create_transaction = True
        try:
            if create_transaction:
                tr = conn.transaction()
                await tr.start()
            try:
                async for record in conn.cursor(
                    sql,
                    articleId ):
                    data_item = ret_data.get(record.id)
                    if not data_item:
                        data_item: ArticleDTO = ArticleDTO(
                            id = record.id,
                            articleCover = record.article_cover,
                            articleTitle = record.article_title,
                            articleContent = record.article_content,
                            createTime = record.create_time,
                            updateTime = record.update_time,
                            categoryId = record.category_id,
                            categoryName = record.category_name
                        )
                        ret_data[record.id] = data_item
                     # 将DTO数据放入对应数组中
                    data_item.tagDTOList.append(
                        TagDTO(
                            id = record.tag_id,
                            tagName = record.tag_name 
                        ) 
                    )
            except:
                if create_transaction:
                    await tr.rollback()
                raise
            else:
                if create_transaction:
                    await tr.commit()
        finally:
            if release_signal:
                await relation_db_cli.pool.release(conn)

        if len(ret_data) > 0:
            _, articledto = ret_data.popitem()
        else:
            articledto = None
        
        return articledto
                        
    
    async def listArticlesByCondition(
        self,
        condition: ConditionVO,
        *, 
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> List[ArticlePreviewDTO]:
        """
            根据条件查询文章
            @param condition 条件
            @return 文章集合
        """
        sql = "select a.id, article_cover, article_title, " \
            "a.create_time, a.category_id, category_name, " \
            "t.id as tag_id, t.tag_name " \
            "from (select " \
            "id, article_cover, article_titile, " \
            "article_content, create_time, category_id " \
            "from tb_article " \
            "where is_delete = 0 and is_draft = 0" \

        end_sql = " order by id desc " \
            "limit ${0} offset ${1} ) as a " \
            "join tb_category as c on a.category_id = c.id " \
            "join tb_article_tag as atg on a.id = atg.article_id " \
            "join tb_tag as t on t.id = atg.tag_id;"
        where_values = []
        where_value_index = 0
        # 按查询条件组装sql语句
        if condition.categoryId is not None:
            where_value_index += 1
            where_values.append(condition.categoryId)
            where_str = f" and category_id = ${where_value_index}"
            sql += where_str
        if condition.tagId is not None:
            where_value_index += 1
            where_values.append(condition.tagId)
            where_str = f" and id in (select article_id from tb_article_tag where tag_id = ${where_value_index})"
            sql += where_str
        # 封装 end_sql 语句
        end_sql = end_sql.format(
            where_value_index + 1,
            where_value_index + 2 )
        where_values.extend([condition.size, condition.current])
        # 生成 sql语句
        sql += end_sql
        # 执行查询语句逻辑
        ret_data = {}
        release_signal = False
        if conn is None:
            conn: Connection = await relation_db_cli.pool.acquire()
            release_signal = True
            create_transaction = True
        try:
            if create_transaction:
                tr = conn.transaction()
                await tr.start()
            try:
                async for record in conn.cursor(
                        sql, *where_values ):
                    data_item = ret_data.get(record.id)
                    if not data_item:
                        data_item: ArticlePreviewDTO = ArticlePreviewDTO(
                            id = record.id,
                            articleCover = record.article_cover,
                            articleTitle = record.article_title,
                            createTime = record.create_time,
                            categoryId = record.category_id,
                            categoryName = record.category_name
                        )
                        ret_data[record.id] = data_item
                    # 将DTO数据放入对应数组中
                    data_item.tagDTOList.append(
                        TagDTO(
                            id = record.tag_id,
                            tagName = record.tag_name 
                        )
                    )
            except:
                if create_transaction:
                    await tr.rollback()
                raise
            else:
                if create_transaction:
                    await tr.commit()
        finally:
            if release_signal:
                await relation_db_cli.pool.release(conn)

        return list(ret_data.values())
                    

    async def listArtilceBacks(
        self,
        condition: ConditionVO,
        *, 
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> List[ArticleBackDTO]:
        """
            查询后台文章
            @param condition 条件
            @return 后台文章集合
        """
        sql = "select " \
            "a.id, article_title, is_top, " \
            "is_draft, a.is_delete, a.create_time, " \
            "a.update_time, category_name, " \
            "t.id as tag_id, t.tag_name " \
            "from (select " \
            "id, article_title, is_top, " \
            "is_draft, is_delete, create_time, " \
            "update_time, category_id " \
            "from tb_article " \
            "where is_delete = $1"
        end_sql = " order by is_top desc " \
            "limit ${0} offset = ${1}) as a " \
            "left join tb_category as c on a.category_id = c.id " \
            "left join tb_article_tag as atg on a.id = atg.article_id " \
            "left join tb_tag as t on t.id = atg.tag_id " \
            "order by is_top desc;"
        where_values = [condition.isDelete]
        where_value_index = 1
        # 按查询条件组装sql语句
        if condition.isDraft is not None:
            where_value_index += 1
            where_values.append(condition.isDraft)
            where_str = f" and is_draft = ${where_value_index}"
            sql += where_str
        if condition.keywords:
            where_value_index += 1
            where_values.append("%{}%".format(condition.keywords))
            where_str = f" and article_title like ${where_value_index}"
            sql += where_str
        
        # 封装 end_sql语句
        end_sql = end_sql.format(
            where_value_index + 1, 
            where_value_index + 2)
        where_values.extend([condition.size, condition.current])
        # 生成 sql语句
        sql += end_sql
        # 查询数据
        ret_data = {}
        # async with relation_db_cli.pool.acquire() as conn:
        release_signal = False
        if conn is None:
            conn: Connection = await relation_db_cli.pool.acquire()
            release_signal = True
            create_transaction = True
        try:
            if create_transaction:
                tr = conn.transaction()
                await tr.start()
            try:
                async for record in conn.cursor(
                        sql, *where_values ):
                    data_item = ret_data.get(record.id)
                    if not data_item:
                        data_item: ArticleBackDTO = ArticleBackDTO(
                            id = record.id,
                            articleTitle = record.article_title,
                            createTime = record.create_time,
                            updateTime = record.update_time,
                            categoryName = record.category_name,
                            isTop = record.is_top,
                            isDraft = record.is_draft,
                            isDelete = record.is_delete 
                        )
                        ret_data[record.id] = data_item
                    # 将DTO数据放入对应数组中
                    data_item.tagDTOList.append(
                        TagDTO(
                            id = record.tag_id,
                            tagName = record.tag_name 
                        )
                    )
            except:
                if create_transaction:
                    await tr.rollback()
                raise
            else:
                if create_transaction:
                    await tr.commit()
        finally:
            if release_signal:
                await relation_db_cli.pool.release(conn)

        return list(ret_data.values())

    
    async def countArticleBacks(
        self,
        condition: ConditionVO,
        *, 
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> int :
        """
            查询后台文章总量
            @param condition 条件
            @return 文章总量
        """
        sql = "select count(1) " \
            "from tb_article " \
            "where is_delete = $1"
        end_sql = ";"
        where_values = [condition.isDelete]
        where_value_index = 1
        # 按查询条件组装sql语句
        if condition.isDraft is not None:
            where_value_index += 1
            where_values.append(condition.isDraft)
            where_str = f" and is_draft = ${where_value_index}"
            sql += where_str
        if condition.keywords:
            where_value_index += 1
            where_values.append("%{}%".format(condition.keywords))
            where_str = f" and article_title like ${where_value_index}"
            sql += where_str
        sql += end_sql
        # 执行 sql 语句
        release_signal = False
        if conn is None:
            conn: Connection = await relation_db_cli.pool.acquire()
            release_signal = True
            create_transaction = True
        try:
            if create_transaction:
                tr = conn.transaction()
                await tr.start()
            try:
                count_num = await conn.fetchval(sql, *where_values, column=0)
                if not count_num:
                    count_num = 0
            except:
                if create_transaction:
                    await tr.rollback()
                raise
            else:
                if create_transaction:
                    await tr.commit()
        finally:
            if release_signal:
                await relation_db_cli.pool.release(conn)
        
        return count_num
            

    async def listArticleRank(
        self,
        articleIdList: List[int], 
        *, 
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> List[Article]:
        """
            查询文章排行
            @param articleIdList
            @return
        """
        sql = "select id, article_title " \
            "from tb_article " \
            "where id in ({0}) " \
            "order by " \
            "array_positions(array[{1}]::integer[], id);"
        # 完善sql语句
        id_list_length = len(articleIdList)
        where_idx = 1
        in_str = ",".join(
            [f"${idx}" for idx in range(where_idx, where_idx + id_list_length)]
        )
        order_str = ",".join(
            [f"${idx}" for idx in range(where_idx + id_list_length, where_idx + 2 * id_list_length)]
        )
        sql = sql.format(in_str, order_str)

        # 执行 sql 语句
        article_list: List[Article] = []
        release_signal = False
        if conn is None:
            conn: Connection = await relation_db_cli.pool.acquire()
            release_signal = True
            create_transaction = True
        try:
            if create_transaction:
                tr = conn.transaction()
                await tr.start()
            try:
                async for record in conn.cursor(
                    sql, *articleIdList, *articleIdList ):
                    
                    article_list.append(
                        Article(
                            id = record.id,
                            articleTitle = record.article_title
                        )
                    )
            except:
                if create_transaction:
                    await tr.rollback()
                raise
            else:
                if create_transaction:
                    await tr.commit()
        finally:
            if release_signal:
                await relation_db_cli.pool.release(conn)
        
        return article_list


__all__ = [
    "ArticleDao"
]