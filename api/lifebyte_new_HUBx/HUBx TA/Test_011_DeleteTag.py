# -*- coding: utf-8 -*-
# @Author ：jenny
# @Time   ：2020/9/14 14:43
# @IDE    ：PyCharm
import json
import random
import string

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

_url = read_config('projectname', 'evn_baseurl') + '/api/deleteTag'

'''设置某些字段为全局变量'''
sql1 = "select id from  `hubx_ta_stag`.`trading_tag`"
tag = mydb.mysql_db(sql1)
_tag = getdict.getlist(tag)


class TestDeleteTags():

    @pytest.mark.level_1
    def test_01_Normal(self):
        '''正常删除已存在Tag '''


        data ={
            "trading_server": "hub_ta_1",
            "tag_id": random.choice(_tag)
        }


        Log().info("%s.%s" % (self.__class__.__name__, get_current_function_name()) +"     ***Test Start***")
        try:
            TA01 = webrequests().delete(url=_url, data=data, headers=_header)
            assert TA01[0] == 200


        except BaseException as e:
            Log().error("删除失败，请重试")
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
    TB = TestDeleteTags()
    TB.test_01_Normal()
'''











