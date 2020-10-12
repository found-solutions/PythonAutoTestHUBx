# -*- coding: utf-8 -*-
# @Author ：jenny
# @Time   ：2020/6/28 15:20
# @IDE    ：PyCharm
import json

import pytest


from comm.getmembertoken import CheckBrokerToken
from comm.logger import Log
from comm.readdoc import read_config
from comm.requestmethod import webrequests
from comm.getdefname import get_current_function_name


CheckBrokerToken()
_header = {
    "Accept": read_config('projectname', 'evn_accept'),
    "Content-Type": read_config('projectname', 'evn_content-type'),
    "Authorization":"Bearer " +  read_config('projectname', 'evn_brokeracctoken')
}

_url = read_config('projectname', 'evn_baseurl') + '/api/checkBrokerEmailExist'

_email = "1361@good.com"
class TestCheckBrokerEmaillExist():
    #global _email
    @pytest.mark.level_1
    def test_01_Normal(self):
        '''检查新增账号是否已存在'''
        data = {
          "email" : _email
        }



        Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) +"     ***Test Start***")
        try:
            BEE01 = webrequests().post_json(url=_url, data=data, headers=_header)

            assert BEE01[0] == 200
            assert False == BEE01[1]['data']['is_exist']

        except BaseException as e:
            Log().error("该账号已存在")
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
    TB = TestADDBrokerUser()
    TB.test_BrokerEmailExist_Normal()

'''










