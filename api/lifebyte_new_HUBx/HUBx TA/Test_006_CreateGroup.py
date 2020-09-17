# -*- coding: utf-8 -*-
# @Author ：jenny
# @Time   ：2020/9/14 14:43
# @IDE    ：PyCharm
import json
import random
import string

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
_url = read_config('projectname', 'evn_baseurl') + '/api/createGroup'

sql1 = "SELECT leverage FROM `hubx_ta_stag`.`trading_leverage`"
sql2 = "select currency from `hubx_ta_stag`.`trading_currency`"

leverage = mydb.mysql_db(sql1)
currency = mydb.mysql_db(sql2)

_leverage = getdict.getlist(leverage)
_currency = getdict.getlist(currency)

class TestCreateGroups():


    def test_01_Normal(self):
        ''' 正常创建Group'''


        data ={
            "group_name": "py{}".format(''.join(random.sample(string.digits, 2))),
            "leverage": random.choice(_leverage),
            "currency": random.choice(_currency),
            "comment": "jenny{}".format(''.join(random.sample(string.digits, 2))),
            "trading_server": "hub_ta_1"
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

'''
if __name__ == '__main__':
    import os
    pytest.main(["{}".format(os.path.split(__file__)[-1])])

'''


if __name__ == '__main__':
    TB = TestCreateGroups()
    TB.test_01_Normal()












