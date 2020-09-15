import pytest
from comm.logger import Log
from comm.readdoc import read_config, write_config
from comm.requestmethod import webrequests


def GetBrokerToken():
    '''获取Broker token'''
    _header = {
        "Accept": read_config('projectname', 'evn_accept'),
        "Content-Type": read_config('projectname', 'evn_content-type')
    }
    _url = read_config('projectname', 'evn_baseurl') + '/api/validateBrokerUser'
    data = {
        "username": read_config('token','broker_user'),
        "password": read_config('token','broker_user_pw'),
        "is_remembered": "false",
        "validate_cmd": 1
    }
    try:
        r = webrequests().post(url=_url, data=data, headers=_header)
        if r[0] == 200:
            token = r[1].json()["user_with_token"]
            write_config("projectname","evn_brokeracctoken",token)
        else:
            pass
    except BaseException as e:
        Log().error(e)
        raise
    else:
        Log().info("成功获取用户token")