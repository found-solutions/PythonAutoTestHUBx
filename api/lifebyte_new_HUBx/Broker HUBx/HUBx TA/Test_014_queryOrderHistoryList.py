# -*- coding: utf-8 -*-
# @Author ：jenny
# @Time   ：2020/10/12 11:43
# @IDE    ：PyCharm
import json
import random
import datetime as dt

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

_url = read_config('projectname', 'evn_baseurl') + '/api/queryHUBxTAOrderList'



sql1 = "SELECT name FROM `hubx_ta_stag`.`mam_master`"
sql2 = "SELECT id FROM `hubx_ta_stag`.`mam_slave_txn` where account_id = 571"
sql3 = "SELECT mt.transaction_key FROM mam_master_txn mt,mam_slave_txn st WHERE st.master_txn_id = mt.id AND st.account_id = 571"



'''执行sql语句，查询数据'''
Mname = mydb.mysql_db(sql1)
Mid = mydb.mysql_db(sql2)
interaction_id = mydb.mysql_db(sql3)


'''将查询出来的数据,转化成新的list'''
_Mname = getdict.getlist(Mname)
_Mid = getdict.getlist(Mid)
_interaction_id = getdict.getlist(interaction_id)
_orderType = [0,1,6,98,99]   #0-buy,1-sell,6-balance,98-empty,99-reconciliation



class TestqueryOrderHistory():

    @pytest.mark.level_1
    def test_01_Normal(self):
        '''通过存在的MAM name查询orders'''
        data = {
            "per_page":10,
            "current_page": 1,
            "mam_name": "_Mname",
            "trading_account": "571",
            "trading_server": "hub_ta_1"
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



    @pytest.mark.level_2
    def test_02_Normal(self):
        '''通过存在的OrderID查询orders'''
        data = {
                "per_page": 10,
                "current_page": 1,
                "order_id": random.choice(_Mid),
                "trading_account": "571",
                "trading_server": "hub_ta_1"
            }

        Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) + "     ***Test Start***")
        try:
           TA02 = webrequests().get(url=_url, params=data, headers=_header)
           assert TA02[0] == 200

        except BaseException as e:
          Log().error("查询失败，请重试")
          raise
        else:
             Log().info("=========>>PASSED")
        finally:
             Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) + "     ***Test End***\n")




    @pytest.mark.level_3
    def test_03_Normal(self):
        '''通过存在的Interaction ID查询orders'''
        data = {
                "per_page": 10,
                "current_page": 1,
                "interaction_id": random.choice(_interaction_id),
                "trading_account": "571",
                "trading_server": "hub_ta_1"
            }

        Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) + "     ***Test Start***")
        try:
           TA02 = webrequests().get(url=_url, params=data, headers=_header)
           assert TA02[0] == 200

        except BaseException as e:
          Log().error("查询失败，请重试")
          raise
        else:
             Log().info("=========>>PASSED")
        finally:
             Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) + "     ***Test End***\n")



    @pytest.mark.level_4
    def test_04_Normal(self):
        '''通过存在的Order Time查询orders'''
        data = {
                "per_page": 10,
                "current_page": 1,
                "open_time_start": dt.datetime.now().strftime('%F %T'),
                "open_time_end" : dt.datetime.now().strftime('%F %T'),
                "trading_account": "571",
                "trading_server": "hub_ta_1"
            }

        Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) + "     ***Test Start***")
        try:
           TA02 = webrequests().get(url=_url, params=data, headers=_header)
           assert TA02[0] == 200

        except BaseException as e:
          Log().error("查询失败，请重试")
          raise
        else:
             Log().info("=========>>PASSED")
        finally:
             Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) + "     ***Test End***\n")


    @pytest.mark.level_5
    def test_05_Normal(self):
        '''通过存在的Order Type查询orders'''
        data = {
                "per_page": 10,
                "current_page": 1,
                "order_type[]": random.choice(_orderType),
                "trading_account": "571",
                "trading_server": "hub_ta_1"
            }

        Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) + "     ***Test Start***")
        try:
           TA02 = webrequests().get(url=_url, params=data, headers=_header)
           assert TA02[0] == 200

        except BaseException as e:
          Log().error("查询失败，请重试")
          raise
        else:
             Log().info("=========>>PASSED")
        finally:
             Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) + "     ***Test End***\n")


    @pytest.mark.level_6
    def test_06_Normal(self):
        '''通过存在的Comment查询orders'''
        data = {
                "per_page": 10,
                "current_page": 1,
                "order_type[]": random.choice(_orderType),
                "trading_account": "571",
                "trading_server": "hub_ta_1"
            }

        Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) + "     ***Test Start***")
        try:
           TA02 = webrequests().get(url=_url, params=data, headers=_header)
           assert TA02[0] == 200

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


'''
if __name__ == '__main__':
    TB = TestqueryOrderHistory()
    TB.test_01_Normal()
    TB.test_02_Normal()
    TB.test_03_Normal()
    TB.test_04_Normal()
    TB.test_05_Normal()
'''

if __name__ == '__main__':
    TB = TestqueryOrderHistory()
    TB.test_05_Normal()













