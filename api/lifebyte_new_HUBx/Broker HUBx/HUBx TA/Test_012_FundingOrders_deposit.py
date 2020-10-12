# -*- coding: utf-8 -*-
# @Author ：jenny
# @Time   ：2020/9/29 13:43
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

_url = read_config('projectname', 'evn_baseurl') + '/api/quickFunding'


'''查询数据库中所有TA'''
sql1 = "SELECT id,name FROM `hubx_ta_stag`.`trading_account`"

'''执行sql语句，查询出所有TA'''
tradingaccount = mydb.mysql_db(sql1)

'''将查询出来的TA,转化成新的list'''
_tradingaccount = getdict.getlist(tradingaccount)



class TestFundingOders_deposit():


    @pytest.mark.level_1
    def test_01_Normal(self):
        '''随机选出HUBxTA入金 '''
        data ={
            "transaction_type": "deposit",
            "funding_amount": 1500,
            "trading_account":  random.choice(_tradingaccount),
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



if __name__ == '__main__':
    import os
    pytest.main(["{}".format(os.path.split(__file__)[-1])])



'''
if __name__ == '__main__':
    TB = TestCreateHUBxTA()
    TB.test_01_Normal()

'''










