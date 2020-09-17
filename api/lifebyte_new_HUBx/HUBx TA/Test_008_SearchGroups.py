# -*- coding: utf-8 -*-
# @Author ：jenny
# @Time   ：2020/9/14 13:43
# @IDE    ：PyCharm
import json

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

_url = read_config('projectname', 'evn_baseurl') + '/api/queryGroupList'

class TestSearchGroups():

    @pytest.mark.level_1
    def test_01_Normal(self):
        '''正常搜索group'''
        data = {
            "group_name": "py02",
            "leverage": 1,
            "currency": "AUD",
            "comment": "erect",
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

'''
if __name__ == '__main__':
    import os
    pytest.main(["{}".format(os.path.split(__file__)[-1])])

'''


if __name__ == '__main__':
    TB = TestSearchGroups()
    TB.test_01_Normal()












