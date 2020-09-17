# -*- coding: utf-8 -*-
# @Author ：jenny
# @Time   ：2020/7/22 10:20
# @IDE    ：PyCharm
import json
import random

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

_url = read_config('projectname', 'evn_baseurl') + '/api/updateBrokerUserInformation'


class TestUpdateBrokerUser():


    def test_01_Normal(self):
        '''更新用户信息'''
        data ={
            "broker_id": 285,
            "updated_at": "2020-09-14 12:53:08",
            "update_fields":
            {

                    "last_name": "gh",
                    "note": "gh",
                    "password": "Lb123456",
                    "user_status": "{}".format(''.join(str(random.randint(0,2)))),         #2-enable,1-readonly,0-disable
                    "send_password_email": "true",
                    "permissions":
                        {
                            "exposure": [],    #[]代表无权限
                            "risk_report": [18],
                            "broker_trading_account_data_visualisation": [35],
                            "broker_mt4_management": [45],
                            "broker_hubx_ta_management": [41],
                            "broker_tmt": [34],
                            "broker_user_management": [20],
                            "broker_admin_portfolio": [38],
                            "broker_all_portfolios": [27],
                            "broker_all_mams": [42],
                            "broker_admin_account_management": [29],
                            "broker_member_management": [36],
                            "broker_action_history": [25],
                            "broker_settings": [32]
                        }
                }
        }


        Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) +"     ***Test Start***")
        try:
            GBU01 = webrequests().post_json(url=_url, data=data, headers=_header)
            assert GBU01[0] == 200

        except BaseException as e:
            Log().error("查询失败，请检查账号")
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
    TB = TestUpdateBrokerUser()
    TB.test_01_Normal()












