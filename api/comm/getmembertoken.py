# -*- coding: utf-8 -*-

import pytest
from comm.logger import Log
from comm.readdoc import read_config, write_config
from comm.requestmethod import webrequests
import json
from comm.getdict import getdict


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
    a = json.dumps(data)
    try:
        r = webrequests().post(url=_url, data=a, headers=_header)
        if r[0] == 200:
            token = getdict(r[1].json(),"user_with_token")
            write_config("projectname","evn_brokeracctoken",token)
        else:
            pass
    except BaseException as e:
        Log().error(e)
        raise
    else:
        Log().info("成功获取用户token")

def GetSocialToken():
    '''获取Social token'''
    _header = {
        "Accept": read_config('projectname', 'evn_accept'),
        "Content-Type": read_config('projectname', 'evn_content-type')
    }
    _url = read_config('projectname', 'evn_baseurl') + '/api/validateUser'
    data = {
        "username": read_config('token','social_user'),
        "password": read_config('token','social_user_pw'),
        "url": "https://stag-hubx.tm-nonprod.com/"
    }
    a = json.dumps(data)
    try:
        r = webrequests().post(url=_url, data=a, headers=_header)
        if r[0] == 200:
            token = getdict(r[1].json(), "user_with_token")
            write_config("projectname","evn_socialacctoken",token)
        else:
            pass
    except BaseException as e:
        Log().error(e)
        raise
    else:
        Log().info("成功获取social用户token")

def CheckBrokerToken():
    header = GetBrokerHeader()
    url = read_config('projectname', 'evn_baseurl') + '/api/showAllBrokerUsers'
    date ={"current_page":1,
           "per_page":50
           }
    try:
        r = webrequests().post(url = url,data=date,headers=header)
        if r[0] == 401:
            GetBrokerToken()
    except BaseException as e:
        Log().error(e)

def CheckSocialToken():
    header = GetSocialHeader()
    url = read_config('projectname', 'evn_baseurl') + '/api/countries'
    date = {"platform": "web"}
    a = json.dumps(date)
    try:
        r = webrequests().get(url = url,headers=header,params=a)
        if r[0] == 401:
            GetSocialToken()
    except BaseException as e:
        Log().error(e)

def GetBrokerHeader(accept = 'evn_accept',content_type = 'evn_content-type',Authorization = 'true'):
    if accept == 'false':
        header = {
            "Content-Type": read_config('projectname', content_type),
            "Authorization": "Bearer " + read_config('projectname', 'evn_brokeracctoken')
        }

    elif content_type == 'false':
        header = {
            "Accept": read_config('projectname', accept),
            "Authorization": "Bearer " + read_config('projectname', 'evn_brokeracctoken')
        }
    elif Authorization == 'flase':
        header = {
            "Accept": read_config('projectname', accept),
            "Content-Type": read_config('projectname', content_type),
        }

    else:
        header = {
            "Accept": read_config('projectname', accept),
            "Content-Type": read_config('projectname', content_type),
            "Authorization": "Bearer " + read_config('projectname', 'evn_brokeracctoken')
        }
    return header

def GetSocialHeader(accept = 'evn_accept',content_type = 'evn_content-type',Authorization = 'true'):
    if accept== 'false':
        header = {
            "Content-Type": read_config('projectname', content_type),
            "Authorization": "Bearer " + read_config('projectname', 'evn_socialacctoken')
        }

    elif  content_type == 'false':
        header = {
            "Accept": read_config('projectname', accept),
            "Authorization": "Bearer " + read_config('projectname', 'evn_socialacctoken')
        }
    elif Authorization == 'false':
        header = {
            "Accept": read_config('projectname', accept),
            "Content-Type": read_config('projectname', content_type),
        }

    else:
        header = {
            "Accept": read_config('projectname', accept),
            "Content-Type": read_config('projectname', content_type),
            "Authorization": "Bearer " + read_config('projectname', 'evn_socialacctoken')
        }
    return header




if __name__ == '__main__':
    CheckBrokerToken()
