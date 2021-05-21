
from typing import List, Optional

from asyncpg import Connection

# 导入数据库连接池
from ..databases.relationDatabase.relationDBCli import relation_db_cli

from ..dataModels.dto import (
    CommentDTO,
    ReplyDTO,
    ReplyCountDTO,
    CommentBackDTO,
)

from ..dataModels.vo import (
    ConditionVO
)



class CommentDao:
    
    def __init__(self):
        pass

    async def listComments(
        self,
        articleId: Optional[int], 
        current: int, 
        page_capacity: int = 10,
        *, 
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> List[CommentDTO]:
        """
            查看评论

            @param articleId 文章id
            @param current   当前页码
            @return 评论集合
        """
        sql = "select " \
            "u.nickname, u.avatar, u.web_site, " \
            "c.user_id, c.id, c.comment_content " \
            "c.create_time " \
            "from tb_comment as c " \
            "join tb_user_info as u on c.user_id = u.id " \
            "where c.is_delete = 0 and paren_id is null"
        
        end_sql = " order by create_time desc " \
            "limit ${0} offset ${1};"
        
        where_values = []
        where_value_index = 0
        # 按查询条件组装sql语句
        if articleId is None:
            where_value_index += 1
            where_values.append(None)
            where_str = f" and article_id is ${where_value_index}"
            sql += where_str
        else:
            where_value_index += 1
            where_values.append(articleId)
            where_str = f" and article_id = ${where_value_index}"
            sql += where_str
        
        # 封装end_sql 语句
        end_sql = end_sql.format(
            where_value_index + 1,
            where_value_index + 2
        )
        where_values.extend([page_capacity, current])
        # 生成sql语句
        sql += end_sql
        # 查询数据
        comemntdto_list: List[CommentDTO] = []
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
                    # 生成对应的数据结构    
                    comemntdto_list.append(
                        CommentDTO(
                            id = record.id,
                            userId = record.user_id,
                            nickname = record.nickname,
                            avatar = record.avatar,
                            webSite = record.web_site,
                            commentContent = record.comment_content,
                            createTime = record.create_time
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

        return comemntdto_list


    async def listReplies(
        self,
        commentIdList: List[int],
        *, 
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> List[ReplyDTO]:
        """
            查看评论id集合下的回复
            @param commentIdList 评论id集合
            @return 回复集合
        """
        sql = "select * " \
            "from (select " \
            "c.user_id, u.nickname, u.avatar, " \
            "u.web_site, c.reply_id, r.nickname as reply_nickname, " \
            "r.web_site as reply_web_site, c.id, c.parent_id, " \
            "c.comment_content, c.create_time, " \
            "row_number () over ( PARTITION BY parent_id ORDER BY c.create_time ASC ) row_num " \
            "from tb_comment as c " \
            "join tb_user_info as u on c.user_id = u.id " \
            "join tb_user_info as r on c.reply_id = r.id " \
            "where c.is_delete = 0 and parent_id in ( {0} )) as t " \
            "where 4 > row_num;"
        # 按条件组装sql语句
        where_value_index = 0
        where_values = []
        # 组装参数值位置
        where_value_index += 1
        where_str = ", ".join(
            [ f"${i}" for i in range(where_value_index, where_value_index + len(commentIdList)) ]
        )
        where_values.extend(commentIdList)
        sql = sql.format(where_str)

        # 开始执行sql语句
        replydto_list: List[ReplyDTO] = []
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
                    replydto_list.append(
                        ReplyDTO(
                            id = record.id,
                            parentId = record.parent_id,
                            userId = record.user_id,
                            nickname = record.nickname,
                            avatar = record.avatar,
                            webSite = record.web_site,
                            replyId = record.reply_id,
                            replayNickname = record.reply_nickname,
                            replyWebSite = record.reply_web_site,
                            commentContent = record.comment_content,
                            createTime = record.create_time
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

        return replydto_list
 
    
    async def listRepliesByCommentId(
        self,
        commentId: int,
        current: int, 
        capacity: int = 5,
        *, 
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> List[ReplyDTO]:
        """
            查看当条评论下的回复
            @param commentId 评论id
            @param current   当前页码
            @return 回复集合
        """
        sql = "select " \
            "c.user_id, u.nickname, u.avatar, " \
            "u.web_site, c.reply_id, r.nickname as reply_nickname, " \
            "r.web_site as reply_web_site, c.id, c.parent_id, " \
            "c.comment_content, c.create_time " \
            "from tb_comment as c " \
            "join tb_user_info as u on c.user_id = u.id " \
            "join tb_user_info as r on c.reply_id = r.id " \
            "where c.is_delete = 0 " \
            "and parent_id = $1 " \
            "order by create_time asc " \
            "limit $2 offset $3;"
        
        # 执行sql语句
        replydto_list: List[ReplyDTO] = []
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
                        commentId,
                        capacity,
                        current ):
                    replydto_list.append(
                        ReplyDTO(
                            id = record.id,
                            parentId = record.parent_id,
                            userId = record.user_id,
                            nickname = record.nickname,
                            avatar = record.avatar,
                            webSite = record.web_site,
                            replyId = record.reply_id,
                            replayNickname = record.reply_nickname,
                            replyWebSite = record.reply_web_site,
                            commentContent = record.comment_content,
                            createTime = record.create_time
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

        return replydto_list


    async def listReplyCountByCommentId(
        self,
        commentIdList: List[int],
        *, 
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> List[ReplyCountDTO]:
        """
            根据评论id查询回复总量
            @param commentIdList 评论id集合
            @return 回复数量
        """
        sql = "select " \
            "parent_id as comment_id, " \
            "count(1) as reply_count " \
            "from tb_comment " \
            "where is_delete = 0 " \
            "and parent_id in ( {0} ) " \
            "group by parent_id;"
        
        # 组装 sql语句
        where_value_index = 0
        where_values = []
        # 组装参数值位置 
        where_value_index += 1
        where_str = ", ".join(
            [ f"${i}" for i in range(where_value_index, where_value_index + len(commentIdList)) ]
        )
        where_values.extend(commentIdList)
        sql = sql.format(where_str)
        
        # 开始执行sql语句
        replycountdto_list: List[ReplyCountDTO] = []
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
                    replycountdto_list.append(
                        ReplyCountDTO(
                            commentId = record.comment_id,
                            replyCount = record.reply_count
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

        return replycountdto_list


    async def listCommentBackDTO(
        self,
        condition: ConditionVO,
        *, 
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> List[CommentBackDTO]:
        """
            查询后台评论
            @param condition 条件
            @return 评论集合
        """
        sql = "select " \
            "c.id, u.avatar, u.nickname, " \
            "r.nickname as reply_nickname, a.article_title, " \
            "c.comment_content, c.create_time, c.is_delete " \
            "from tb_comment as c " \
            "left join tb_article as a on c.article_id = a.id " \
            "left join tb_user_info as u on c.user_id = u.id " \
            "left join tb_user_info as r on c.reply_id = r.id " \
            "where c.is_delete = $1" \
        
        end_sql = " order by create_time desc " \
            "limit ${0} offset ${1};"
        
        # 开始组装 sql语句
        where_value_index = 1
        where_values = [condition.isDelete]
        if condition.keywords is not None:
            where_value_index += 1
            where_str = f" and u.nickname like ${where_value_index}"
            where_values.append( f"%{condition.keywords}%" )
            sql += where_str
        # 组装end_sql
        end_sql = end_sql.format(
            where_value_index + 1,
            where_value_index + 2 )
        where_values.extend(
            [
                condition.size, 
                condition.current
            ]
        )
        # 最终拼接sql 语句
        sql += end_sql
        # 开始执行sql语句
        commentbackdto_list: List[CommentBackDTO] = []
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
                    commentbackdto_list.append(
                        CommentBackDTO(
                            id = record.id,
                            avatar = record.avatar,
                            nickname = record.nickname,
                            replyNickName = record.reply_nickname,
                            articleTitle = record.article_title,
                            commentContent = record.comment_content,
                            createTime = record.create_time,
                            is_delete = record.is_delete
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

        return commentbackdto_list
        
    
    async def countCommentDTO(
        self,
        condition: ConditionVO,
        *, 
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> int:
        """
            统计后台评论数量
            @param condition 条件
            @return 评论数量
        """
        sql = "select count(1) " \
            "from tb_comment as c " \
            "left join tb_user_info as u on c.user_id = u.id " \
            "where c.is_delete = $1"
        
        end_sql = ";"
        
        # 开始组装sql语句
        where_value_index = 1
        where_values = [condition.isDelete]
        # 组装查询条件
        if condition.keywords is not None:
            where_value_index += 1
            where_str = f" and u.nickname like ${where_value_index}"
            where_values.append(
                f"%{condition.keywords}%"
            )
            sql += where_str
        # 拼接 sql 语句
        sql += end_sql
        
        # 开始执行SQL语句
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
                comment_count = await conn.fetchval(
                    sql, *where_values, colomn=0 )
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
        
        if not comment_count:
                    comment_count = 0

        return comment_count



__all__ = [
    "CommentDao"
]