# -*- coding: utf-8 -*-

import pymysql
from comm.readdoc import read_config
from sshtunnel import SSHTunnelForwarder
from comm.logger import Log
import paramiko
import os

logs = Log()


def mysql_db(sql):
    # 直接连接MySQL数据库，无SSH隧道
    # 获取数据库信息
    host = read_config('projectname', 'mysql_host')
    user = read_config('projectname', 'mysql_user')
    passwd = read_config('projectname', 'mysql_passwd')
    port = read_config('projectname', 'mysql_port')
    db = read_config('projectname', 'mysql_db')
    charset = read_config('projectname', 'mysql_charset')

    # 创建连接
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            passwd=passwd,
            port=port,
            db=db,
            charset=charset)
        cur = conn.cursor()  # 建立游标
    except BaseException:
        res = "数据库连接失败！"
        logs.error(res)
    else:
        if sql.strip()[:6].upper() == 'SELECT':
            # res = cur.fetchall()
            cur.execute(sql)  # 执行sql
            res = cur.fetchall()  # 显示查询结果
            cur.close()
            conn.close()
        else:
            try:
                cur.execute(sql)  # 执行sql
            except BaseException as e:
                logs.error(e)
                conn.rollback()  # SQL异常，回滚
                res = e
            else:
                # 无异常时执行
                conn.commit()  # 提交
                res = 'SQL 执行 ok！'
                logs.info(res)
            finally:
                # 总是执行
                cur.close()
                conn.close()
    return res


def ssh_server():

    # 获取当前文件的路径
    file_path = os.path.dirname(__file__)
    # 获取配置文件config.ini的路径
    #config_path = os.path.join(file_path, 'private_key')

    # 创建ssh连接
    ssh_host = read_config('projectname', 'ssh_address')
    ssh_port = read_config('projectname', 'ssh_port')
    ssh_user = read_config('projectname', 'ssh_user')
    #用密码访问
    ssh_password = read_config('projectname', 'ssh_password')
    #用密钥访问
    ssh_password = paramiko.RSAKey.from_private_key_file(config_path)
    mydb_host = read_config('projectname', 'mysql_host')
    mydb_port = read_config('projectname', 'mysql_port')
    server = SSHTunnelForwarder(
        ssh_address_or_host=(ssh_host, int(ssh_port)),  # 端口转为int类型
        ssh_username=ssh_user,
        ssh_password=ssh_password,
        ssh_pkey=ssh_password,
        remote_bind_address=(mydb_host, int(mydb_port))  # 端口转为int类型

    )
    return server


def ssh_mysql(sql):
    # 通过ssh隧道连接MySQL

    ssh = ssh_server()
    ssh.start()

    host = "127.0.0.1"
    user = read_config('projectname', 'mysql_user')
    passwd = read_config('projectname', 'mysql_passwd')
    port = ssh.local_bind_port
    db = read_config('projectname', 'mysql_db')
    charset = read_config('projectname', 'mysql_charset')

    # 创建连接
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            passwd=passwd,
            port=port,
            db=db,
            charset=charset)
    except BaseException:
        res = "数据库连接失败！！"
        logs.error(res)
        ssh.stop()

    else:
        # j建立游标
        # cur = conn.cursor()#元组形式
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)#字典形式

        if sql.strip()[:6].upper() == 'SELECT':
            # res = cur.fetchall()
            cur.execute(sql)  # 执行sql
            res = cur.fetchall()  # 显示查询结果
            cur.close()
            conn.close()
            ssh.stop()
        else:
            try:
                cur.execute(sql)  # 执行sql
            except BaseException as e:
                logs.error(e)
                conn.rollback()  # SQL异常，回滚
                res = e
            else:
                # 无异常时执行
                conn.commit()  # 提交
                res = 'SQL 执行 ok！'
                logs.info(res)
            finally:
                # 总是执行
                cur.close()
                conn.close()
                ssh.stop()
    return res


if __name__ == '__main__':
    # import requests
    # # salecode = 'test_code11'
    # # insetsql = "INSERT INTO `staging-portal`.`sale_codes`(`code`, `display_name`, `email`,  `TO`, `CC`, `BCC`, `created_by`, `updated_by`, `created_at`, `updated_at`) VALUES ('{code}', '{display_name}', '{email}', '{TO}', '{CC}', '{BCC}','test1','test1', NOW(), NOW())".format(
    # #     code=salecode, display_name=salecode, email=salecode + '@lifebyte.io', TO=salecode + '@lifebyte.io', CC=salecode + '@lifebyte.io', BCC=salecode + '@lifebyte.io')
    # # deletesql = "DELETE FROM `staging-portal`.`sale_codes` WHERE `code` = '{}'".format(
    # #     salecode)
    # #
    # # res1 = ssh_mysql(insetsql)
    # # res2 = ssh_mysql(deletesql)
    # login = []
    # # sql1 = "SELECT LOGIN FROM tm_demo_1.mt4_users WHERE LOGIN not in (SELECT external_id FROM tm_staging_crm.trading_accounts)"
    # sql1 = "SELECT external_id FROM trading_accounts WHERE id >= 10063 and id <= 10412"
    # res1 = ssh_mysql(sql1)
    # # print(res1)
    # c = []
    # for i in res1:
    #     a = list(i.values())
    #     for b in a:
    #         print(b)
    #         c.append(b)
    # print(c)
    # for j in c:
    #     # sql2 = "INSERT INTO tm_staging_crm.trading_accounts (`type`,`external_id`,`user_id`,`is_ib`,`salescode`,`note`,`created_at`,`updated_at`) VALUES ('1','{external_id}','3','0','yali_test','test',NOW(),NOW())".format(external_id=j)
    #     # res2 = ssh_mysql(sql2)
    #     # print(j,res2)
    #     print(j)
    #     parameters = {
    #             "url" : "https://staging-portal-api.trademax.global/api/tradingAccounts/modify",
    #             "header" : {
    #             "Accept": "application/prs.CRM-Back-End.v2+json",
    #             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    #             "Content-Type": "application/x-www-form-urlencoded",
    #             "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImI3OTJiMWUwMjA3Mzg1NjU3NTk1ZTM0YmU2MjI0ZDg0MmQ4NTMyNTczZGEwZGYxMzg1NGNkMDU2ZjM5Y2FkMzRkOTQ0ZTYyOTM1NzlkNWIxIn0.eyJhdWQiOiIxIiwianRpIjoiYjc5MmIxZTAyMDczODU2NTc1OTVlMzRiZTYyMjRkODQyZDg1MzI1NzNkYTBkZjEzODU0Y2QwNTZmMzljYWQzNGQ5NDRlNjI5MzU3OWQ1YjEiLCJpYXQiOjE1NzEwMTcwMDIsIm5iZiI6MTU3MTAxNzAwMiwiZXhwIjoxNTcxNjIxODAyLCJzdWIiOiIyNjMiLCJzY29wZXMiOlsiKiJdfQ.linHklod2-iOGpOftGhIJsq0fxL5R14r7jh-RzOSAfdEDC1jHKOMEko1UTiNO-C7hTmpU7WuW3I39zCfpZignnQqO5ohkcUKjQMEMlvey3rQk2zqxf-2-z8jbF_Wk7UXrDfR8t9xYibSQm-VXLmBrGLmOrL-07lvz_dgM8HGUlcyiwNVptXrYF3moDpmZYVZNfQ5cyqgDxqHB9m5kpMid9Kx0StjsPPbelsoVdrcCzRdrJWCiCjngO5q7Odaj46lZBpryrYgHBQpu3O0a5M0iGtO1mkZ0hl_I5PFwdXJy1qpaVhmp7Xm-Z3aJMILz3wA5E0QU0N_UulQalXWzi-accU_dqjg0rNNrUm_FTJYJ9XzG-SahmD00kPgO3SgdyPBhiI6LJfWhozDiuvFg_KBA5hSYNtAJ91f_mgLxvhHb_MnsnY89aMW3P5dOn13jjJR6dF0kB6BXPbcBWVzhCRZWjmCGBk0JpwPYfbjaycSLOJcz_czBQaXQyhKk2aCugPgbtQiLd14krWJ9l_XqMTNQS4WYp3mgkM6jeIuSpeK1CbP_SFWjFXat0q4lVlVFDVqcHx9OGt9O9VGIUdEXohnMktMIP4sgYpVPk0lxyOw85he_A3Qo0BQQtuxlKdxPjx7i43D4x08VzipGBoDl9e7i04lUq7RW6yBCVPAsPkxZr4"}
    #         }
    #     data = {
    #         "user_id": 762,
    #         "trading_server_id": 1,
    #         "external_id": j,
    #         "parent_external_id": 600133,
    #         "is_ib": 0,
    #         "salescode": "yali_test",
    #         "parent_trading_server_id": 3
    #     }
    #     response = requests.patch(
    #                 url=parameters["url"],
    #                 data=data,
    #                 headers=parameters["header"])
    #     if response.status_code == 200:
    #         result = response.content.decode('utf-8')
    #     else:
    #         result = "访问失败"

    sql1 = "SELECT external_id FROM trading_accounts"
    res1 = ssh_mysql(sql1)
    print(res1)