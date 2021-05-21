
from typing import List, Optional
from asyncpg import Connection

#导入数据库连接池
from ..databases.relationDatabase.relationDBCli import relation_db_cli

# 导入需要使用的 dto 数据模型
from ..dataModels.dto import (
    UserBackDTO,
)

# 导入需要使用的 vo 数据模型
from ..dataModels.vo import (
    ConditionVO,
)



class UserAuthDao:
    
    def __init__(self):
        pass
    
    async def listUsers(
        self,
        condition: ConditionVO,
        *, 
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> List[UserBackDTO]:
        """
            查询后台用户列表
            @param condition 条件
            @return 用户集合

        """
        sql = "select " \
            "ua.id, user_info_id, avatar, " \
            "nickname, login_type, user_role, " \
            "ip_addr, ip_source, ua.create_time, " \
            "last_login_time, is_silence " \
            "from tb_user_auth as ua " \
            "left join tb_user_info as ui on ua.user_info_id = ui.id"
        
        end_sql = "limit ${0} offset ${1}"
        # 开始组装sql 语句 
        where_value_index = 0
        where_values = []
        if condition.keywords is not None:
            where_value_index += 1
            where_str = f" where nickname like ${where_value_index}"
            where_values.append(f"%{condition.keywords}%")
            sql += where_str
        # 组装 end_sql
        end_sql = end_sql.format(
            where_value_index + 1, where_value_index + 2 )
        where_values.extend([condition.size, condition.current])
        # 合并sql语句 
        sql += end_sql
        
        # 开始执行sql语句
        userbackdto_list: List[UserBackDTO] = []
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
                    userbackdto_list.append(
                        UserBackDTO(
                            id = record.id,
                            userInfoId = record.user_info_id,
                            avatar = record.avatar,
                            nickname = record.nickname,
                            userRole = record.user_role,
                            loginType = record.login_type,
                            ipAddr = record.ip_addr,
                            ipSource = record.ip_source,
                            createTime = record.create_time,
                            lastLoginTime = record.last_login_time,
                            isSilence = record.is_silence
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
        
        return userbackdto_list
        

    async def countUser(
        self,
        condition: ConditionVO,
        *, 
        conn: Optional[Connection] = None,
        create_transaction: bool = True ) -> int:

        """
            查询后台用户数量
            @param condition 条件
            @return 用户数量
        
        """
        sql =  "select count(1) " \
            "from tb_user_auth as ua " \
            "left join tb_user_info as ui on ua.user_info_id = ui.id"
        
        end_sql = ";"
        # 开始组装 sql语句
        where_value_index = 0
        where_values = []
        if condition.keywords is not None:
            where_value_index += 1
            where_str = f" where nickname like ${where_value_index}"
            where_values.append(f"%{condition.keywords}%")
            sql += where_str
        # 组合 sql语句 
        sql += end_sql
        # 开始执行sql语句
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
        
        if not count_num:
                    count_num = 0

        return count_num


__all__ = [
    "UserAuthDao",

]
