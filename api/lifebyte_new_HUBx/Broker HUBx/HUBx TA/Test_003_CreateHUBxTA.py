# -*- coding: utf-8 -*-
# @Author ：jenny
# @Time   ：2020/9/14 13:43
# @IDE    ：PyCharm
import json

import random,string



import pytest

from comm import mydb, getdict
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

_url = read_config('projectname', 'evn_baseurl') + '/api/createHUBxTA'

'''设置某些字段参数为全局变量'''
sql1 = "SELECT leverage FROM `hubx_ta_stag`.`trading_leverage`"
sql2 = "SELECT NAME FROM `hubx_ta_stag`.`trading_group`"

leverage = mydb.mysql_db(sql1)
groupname = mydb.mysql_db(sql2)

_leverage = getdict.getlist(leverage)
_groupname = getdict.getlist(groupname)


class TestCreateHUBxTA():


    @pytest.mark.level_1
    def test_01_Normal(self):
        '''正常创建HUBxTA '''
        data ={
            "trading_server": "hub_ta_1",
            "leverage": random.choice(_leverage),
            "group_name": random.choice(_groupname),
            "ta_name": "jenny{}".format(''.join(random.sample(string.digits, 2))),
            "password": "Lb123456",
            "confirm_pwd": "Lb123456",
            "pin": "123456"
        }


        Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) +"     ***Test Start***")
        try:
            TA01 = webrequests().post_json(url=_url, data=data, headers=_header)
            assert TA01[0] == 200

        except BaseException as e:
            Log().error("创建失败，请重试")
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
    TB.test_01_Normal()

'''










