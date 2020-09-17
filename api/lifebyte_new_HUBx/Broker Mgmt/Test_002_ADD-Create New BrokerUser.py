# -*- coding: utf-8 -*-
# @Author ：
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

_url = read_config('projectname', 'evn_baseurl') + '/api/createNewBrokerUserManually'

_email = "13611@good.com"
class TestADDBrokerUser():
    #global _email
    @pytest.mark.level_1
    def test_01_Normal(self):
        '''正常新增用户'''
        data = {
            "email": _email,
            "role": "5",
            "locked": "1"
        }


        Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) +"     ***Test Start***")
        try:
            CNBU01 = webrequests().post_json(url=_url, data=data, headers=_header)
            assert CNBU01[0] == 200

        except BaseException as e:
            Log().error("添加失败，请检查账号")
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
    TB = TestADDBrokerUser()
    TB.test_01_Normal()












