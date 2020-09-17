# -*- coding: utf-8 -*-
# @Author ：
# @Time   ：2020/6/28 15:20
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

_url = read_config('projectname', 'evn_baseurl') + '/api/showAllBrokerUsers'


class TestResetBrokerUser():


    @pytest.mark.level_1
    def test_01_Normal(self):
        '''重置信息'''

        data = {
            "current_page": "1",
            "per_page": "50",

        }


        Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) +"     ***Test Start***")
        try:
            Res01 = webrequests().post_json(url=_url, data=data, headers=_header)
            assert Res01[0] == 200

        except BaseException as e:
            Log().error(e)
            raise
        else:
            Log().info("=========>>PASSED")
        finally:
            Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) + "     ***Test End***\n")






if __name__ == '__main__':
    TB = TestResetBrokerUser()
    TB.test_01_Normal()

'''
if __name__ == '__main__':
    import os
    pytest.main(["{}".format(os.path.split(__file__)[-1])])
'''