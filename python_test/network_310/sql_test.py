import openpyxl
import pymysql


def sql_insert():
    no = int(input('部门编号: '))

    name = input('部门名称: ')
    location = input('部门所在地: ')

    # 1. 创建连接（Connection）
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                           user='guest', password='Guest.618',
                           database='hrs', charset='utf8mb4')
    try:
        # 2. 获取游标对象（Cursor）
        with conn.cursor() as cursor:
            # 3. 通过游标对象向数据库服务器发出SQL语句
            affected_rows = cursor.execute(
                'insert into `tb_dept` values (%s, %s, %s)',
                (no, name, location)
            )
            if affected_rows == 1:
                print('新增部门成功!!!')
        # 4. 提交事务（transaction）
        conn.commit()
    except pymysql.MySQLError as err:
        # 4. 回滚事务
        conn.rollback()
        print(type(err), err)
    finally:
        # 5. 关闭连接释放资源
        conn.close()


def sql_delete():
    no = int(input('部门编号: '))

    # 1. 创建连接（Connection）
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                           user='guest', password='Guest.618',
                           database='hrs', charset='utf8mb4',
                           autocommit=True)
    try:
        # 2. 获取游标对象（Cursor）
        with conn.cursor() as cursor:
            # 3. 通过游标对象向数据库服务器发出SQL语句
            affected_rows = cursor.execute(
                'delete from `tb_dept` where `dno`=%s',
                (no,)
            )
            if affected_rows == 1:
                print('删除部门成功!!!')
    finally:
        # 5. 关闭连接释放资源
        conn.close()


def sql_update():
    no = int(input('部门编号: '))
    name = input('部门名称: ')
    location = input('部门所在地: ')

    # 1. 创建连接（Connection）
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                           user='guest', password='Guest.618',
                           database='hrs', charset='utf8mb4')
    try:
        # 2. 获取游标对象（Cursor）
        with conn.cursor() as cursor:
            # 3. 通过游标对象向数据库服务器发出SQL语句
            affected_rows = cursor.execute(
                'update `tb_dept` set `dname`=%s, `dloc`=%s where `dno`=%s',
                (name, location, no)
            )
            if affected_rows == 1:
                print('更新部门信息成功!!!')
        # 4. 提交事务
        conn.commit()
    except pymysql.MySQLError as err:
        # 4. 回滚事务
        conn.rollback()
        print(type(err), err)
    finally:
        # 5. 关闭连接释放资源
        conn.close()


def sql_select():
    # 1. 创建连接（Connection）
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                           user='guest', password='Guest.618',
                           database='hrs', charset='utf8mb4')
    try:
        # 2. 获取游标对象（Cursor）
        with conn.cursor() as cursor:
            # 3. 通过游标对象向数据库服务器发出SQL语句
            cursor.execute('select `dno`, `dname`, `dloc` from `tb_dept`')
            # 4. 通过游标对象抓取数据
            row = cursor.fetchone()
            while row:
                print(row)
                row = cursor.fetchone()
    except pymysql.MySQLError as err:
        print(type(err), err)
    finally:
        # 5. 关闭连接释放资源
        conn.close()


def sql_export_excel():
    # 创建工作簿对象
    workbook = openpyxl.Workbook()
    # 获得默认的工作表
    sheet = workbook.active
    # 修改工作表的标题
    sheet.title = '员工基本信息'
    # 给工作表添加表头
    sheet.append(('工号', '姓名', '职位', '月薪', '补贴', '部门'))
    # 创建连接（Connection）
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                           user='guest', password='Guest.618',
                           database='hrs', charset='utf8mb4')
    try:
        # 获取游标对象（Cursor）
        with conn.cursor() as cursor:
            # 通过游标对象执行SQL语句
            cursor.execute(
                'select `eno`, `ename`, `job`, `sal`, coalesce(`comm`, 0), `dname` '
                'from `tb_emp` natural join `tb_dept`'
            )
            # 通过游标抓取数据
            row = cursor.fetchone()
            while row:
                # 将数据逐行写入工作表中
                sheet.append(row)
                row = cursor.fetchone()
        # 保存工作簿
        workbook.save('out/hrs.xlsx')
    except pymysql.MySQLError as err:
        print(err)
    finally:
        # 关闭连接释放资源
        conn.close()


def main():
    # sql_insert()
    # sql_delete()
    # sql_update()
    # sql_select()
    sql_export_excel()


if __name__ == '__main__':
    main()
