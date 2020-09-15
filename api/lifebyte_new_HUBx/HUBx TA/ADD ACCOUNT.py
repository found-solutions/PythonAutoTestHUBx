# -*- coding: utf-8 -*-
# @Author ：
# @Time   ：2020/9/11 15:40
# @IDE    ：PyCharm

import pytest
from comm.logger import Log
from comm.readdoc import read_config, write_config
from comm.getdefname import get_current_function_name
from comm.requestmethod import webrequests


_header = {
    "Accept": read_config('projectname', 'evn_accept'),
    "Content-Type": read_config('projectname', 'evn_content-type')
}
_url = read_config('projectname', 'evn_baseurl') + '/api/validateBrokerUser'


class TestGetToken():
    '''获取token测试'''

    @pytest.mark.level_1
    def test_01_Normal(self):
        '''用户名，密码正确'''
        data = {
            "username": "mary00@qq.com",
            "password": "Lb123456",
            "is_remembered": "false",
            "validate_cmd": 1
        }
        Log().info("%s.%s" %(self.__class__.__name__,get_current_function_name()) +"     ***Test Start***")

        try:
            r = webrequests().post(url=_url, data=data, headers=_header)
            assert r[0] == 200
            assert 'user_with_token' in r[1].text
        except BaseException as e:
            Log().error(e)
            raise
        else:
            Log().info("=========>>PASSED")
        finally:
            Log().info("%s.%s" %(self.__class__.__name__,get_current_function_name()) +"     ***Test End***\n")

    @pytest.mark.level_2
    def test_02_UsernameNotExit(self):
        '''用户名错误'''
        data = {
            "username": "testtest",
            "password": "Lb123456",
            "is_remembered": "false",
            "validate_cmd": 2
        }
        Log().info("%s.%s" %(self.__class__.__name__,get_current_function_name()) +"     ***Test Start***")

        try:
            r = webrequests().post(url=_url, data=data, headers=_header)
            assert r[0] == 403
            assert 'user_with_token' not in r[1].text
        except BaseException as e:
            Log().error(e)
            raise
        else:
            Log().info("=========>>PASSED")
        finally:
            Log().info("%s.%s" %(self.__class__.__name__,get_current_function_name()) +"     ***Test End***\n")

    @pytest.mark.level_3
    def test_03_PasswdError(self):
        '''密码错误'''
        data = {
            "username": "mary@lifebyte.io",
            "password": "Lb123456789",
            "is_remembered": "false",
            "validate_cmd": 1
        }
        Log().info(
            "%s.%s" %(self.__class__.__name__,get_current_function_name()) +"     ***Test Start***")

        try:
            r = webrequests().post(url=_url, data=data, headers=_header)
            assert r[0] == 403
            assert 'user_with_token' not in r[1].text
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

