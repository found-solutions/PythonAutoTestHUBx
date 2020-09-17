# -*- coding: utf-8 -*-
# @Author ：jenny
# @Time   ：2020/9/14 13:43
# @IDE    ：PyCharm
import json
import random

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

_url = read_config('projectname', 'evn_baseurl') + '/api/queryHUBxTAList'

'''设置某些字段参数为全局变量'''
sql4 = "SELECT id,name FROM `hubx_ta_stag`.`trading_account`"

tradingaccount = mydb.mysql_db(sql4)

_tradingaccount = getdict.getlist(tradingaccount)



class TestSearchHUBxTA():

    @pytest.mark.level_1
    def test_01_Normal(self):
        '''搜索某条特定的数据 '''
        data = {
                "platform":"web",
                "trading_server":"hub_ta_1",
                "trading_account":_tradingaccount[0],
                "ta_name" : _tradingaccount[1],
                "status":"{}".format(''.join(str(random.randint(1,3)))),    #enable-1,readonly-2,disable-3
                # "group_name":"AutoTest Group1",
                "per_page":"50",
                "current_page":"1"
                }


        Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) +"     ***Test Start***")
        try:
            TA01 = webrequests().get(url=_url, params=data, headers=_header)
            assert TA01[0] == 200

        except BaseException as e:
            Log().error("查询失败，请重试")
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
    TB = TestSearchHUBxTA()
    TB.test_SearchHUBxTa_Normal()












