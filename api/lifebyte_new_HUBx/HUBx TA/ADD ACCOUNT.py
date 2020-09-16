# -*- coding: utf-8 -*-
# @Author ：
# @Time   ：2020/9/11 15:40
# @IDE    ：PyCharm

import pytest
from comm.logger import Log
from comm.readdoc import read_config, write_config
from comm.getdefname import get_current_function_name
from comm.requestmethod import webrequests
import json
import random, string

_header = {
    "Accept": read_config('projectname', 'evn_accept'),
    "Content-Type": read_config('projectname', 'evn_content-type'),
    "Authorization":"Bearer " +  read_config('projectname', 'evn_brokeracctoken')
}
_url = read_config('projectname', 'evn_baseurl') + '/api/createHUBxTA'


class TestGetToken():
    '''获取token测试'''

    @pytest.mark.level_1
    def test_01_Normal(self):
        '''用户名，密码正确'''
        data = {
            "confirm_pwd": "Lb123456",
            "group_name":"AutoTest Group12",
            "password": "Lb123456",
            "pin": "1234",
            "ta_name": "test{}".format(''.join(random.sample(string.digits, 2))),
            "trading_server": "hub_ta_1"
        }
        a=json.dumps(data)
        Log().info("%s.%s" %(self.__class__.__name__,get_current_function_name()) +"     ***Test Start***")

        try:
            r = webrequests().post(url=_url, data=a, headers=_header)
            assert r[0] == 200
            assert 'AutoTest Group12' in r[1].text
        except BaseException as e:
            Log().error(e)
            raise
        else:
            Log().info("=========>>PASSED")
        finally:
            Log().info("%s.%s" %(self.__class__.__name__,get_current_function_name()) +"     ***Test End***\n")



if __name__ == '__main__':
    import os
    pytest.main(["{}".format(os.path.split(__file__)[-1])])

