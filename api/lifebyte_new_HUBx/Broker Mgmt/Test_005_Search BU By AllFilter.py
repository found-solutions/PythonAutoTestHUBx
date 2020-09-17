# -*- coding: utf-8 -*-
# @Author ：Jenny
# @Time   ：2020/7/15 15:20
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

_url = read_config('projectname', 'evn_baseurl') + '/api/showAllBrokerUsers'



class TestSearchBrokerUser():


    @pytest.mark.level_1
    def test_01_Normal(self):
        '''搜索用户'''

        data = {
            "broker_id_filter":"",               #HUB_ID
            "email_filter": "",
            "start_time": "",
            "end_time": "",
            "user_status_filter":"{}".format(''.join(str(random.randint(0,2)))),  #2:Enable  1:Readonly   0:Disable  不传user_status_filter字段代表All
            "role_filter":"{}".format(''.join(str(random.randint(5,6)))),          #5:Admin  6:God   role_filter为空代表All
            "current_page": "1",
            "per_page": "50",
        }



        Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) +"     ***Test Start***")
        try:
            all01 = webrequests().post_json(url=_url, data=data, headers=_header)
            assert all01[0] == 200

        except BaseException as e:
            Log().error(e)
            raise
        else:
            Log().info("=========>>PASSED")
        finally:
            Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) + "     ***Test End***\n")






if __name__ == '__main__':
    TB = TestSearchBrokerUser()
    TB.test_01_Normal()


'''
if __name__ == '__main__':
    import os
    pytest.main(["{}".format(os.path.split(__file__)[-1])])
'''