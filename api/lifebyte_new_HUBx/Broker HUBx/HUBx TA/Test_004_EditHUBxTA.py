# -*- coding: utf-8 -*-
# @Author ：jenny
# @Time   ：2020/9/16 10:54
# @IDE    ：PyCharm
import json

import random,string
from comm import mydb, getdict

import pytest

from comm.getdefname import get_current_function_name
from comm.getmembertoken import CheckBrokerToken
from comm.logger import Log
from comm.readdoc import read_config
from comm.requestmethod import webrequests

CheckBrokerToken()
_header = {
    "Accept": read_config('projectname', 'evn_accept'),
    "Content-Type": read_config('projectname', 'evn_content-type'),
    "Authorization":"Bearer " +  read_config('projectname', 'evn_brokeracctoken')
}

_url = read_config('projectname', 'evn_baseurl') + '/api/editHUBxTA'

'''设置某些字段参数为全局变量'''
sql1 = "SELECT leverage FROM `hubx_ta_stag`.`trading_leverage`"
sql2 = "SELECT NAME FROM `hubx_ta_stag`.`trading_group`"
sql3 = "select id from  `hubx_ta_stag`.`trading_tag`"
sql4 = "SELECT id,name FROM `hubx_ta_stag`.`trading_account`"


leverage = mydb.mysql_db(sql1)
groupname = mydb.mysql_db(sql2)
tag = mydb.mysql_db(sql3)
tradingaccount = mydb.mysql_db(sql4)

_leverage = getdict.getlist(leverage)
_groupname = getdict.getlist(groupname)
_tag = getdict.getlist(tag)
_tradingaccount = getdict.getlist(tradingaccount)

class TestEditHUBxTA():

    @pytest.mark.level_1
    def test_01_Normal(self):
        '''编辑HUB TA'''


        data = {
         "platform":"web",
         "trading_server":"hub_ta_1",
         "ta_name":"jenny{}".format(''.join(random.sample(string.digits, 2))),
         "status":"{}".format(''.join(str(random.randint(1,3)))),
         "leverage":random.choice(_leverage),
         "group_name": random.choice(_groupname),
         "tags":[random.choice(_tag)],
         "comment":"1234",
         "trading_account": random.choice(_tradingaccount),
         "pin":"1234",
         "password":"Lb123456"
        }


        Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) +"     ***Test Start***")
        try:
            TA01 = webrequests().put_json(url=_url, data=data, headers=_header)
            assert TA01[0] == 200

        except BaseException as e:
            Log().error("编辑失败，请重试")
            raise
        else:
            Log().info("=========>>PASSED")
        finally:
            Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) + "     ***Test End***\n")


if __name__ == '__main__':
    import os
    pytest.main(["{}".format(os.path.split(__file__)[-1])])



'''
if __name__ == '__main__':
    TB = TestCreateHUBxTA()
    TB.test_ApplyHUBxTa_Normal()

'''










