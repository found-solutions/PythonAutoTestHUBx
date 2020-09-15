# -*- coding: utf-8 -*-



import pytest
from comm.logger import Log
from comm.readdoc import read_config, write_config
from comm.getdefname import get_current_function_name
from comm.requestmethod import webrequests
from comm.getmembertoken import CheckAdminToken


CheckAdminToken()
_header = {
    "Accept": read_config('projectname', 'evn_accept'),
    "Content-Type": read_config('projectname', 'evn_content-type'),
    "Authorization":"Bearer " +  read_config('projectname', 'evn_adminacctoken')
}
_url = read_config('projectname', 'evn_baseurl') + '/api/front/tradingAccounts/create'


class TestMemberAddAccount():

    def test_01_AddNew(self):
        data = {
            "user_id": 942,
            "trading_server_id": 1,
            "leverage": 10,
            "group": 'stboz-st-u',
            "password": 'Lb123456',
            "password_confirmation": 'Lb123456'
        }
        Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) + "     ***Test Start***")
        r = webrequests().post(url=_url, data=data, headers=_header)
        try:
            # print(r[1])
            assert r[0] == 200
            # assert 'access_token' in r[1].json()
        except Exception as e:
            Log().error(e)
            raise
        else:
            Log().info("=========》PASSED")
        finally:
            Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) + "     ***Test End***\n")