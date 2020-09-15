# -*- coding: utf-8 -*-


import requests
from comm.logger import Log
import json


class webrequests():

    def get(self, url, params=None, headers=None, files=None, timeout=8):
        '''封装get方法，return响应码和响应内容'''
        # 忽略ssl证书警告
        requests.packages.urllib3.disable_warnings()
        try:
            r = requests.get(
                url,
                params=params,
                headers=headers,
                files=files,
                verify=False,
                timeout=timeout)
            Log().info("请求的内容：%s" % params)
            # 获取返回的状态码
            status_code = r.status_code
            Log().info("获取返回的状态码：%d" % status_code)
            # 响应内容，json类型转化成python数据类型
            # response_json = r.json()
            # Log().info("响应内容：%s" % response_json)
            # 返回响应码，响应内容
            return status_code, r
        except BaseException as e:
            Log().error("请求失败！")

    def post(self, url, data=None, headers=None, files=None, timeout=8):
        '''封装post请求，return响应码和响应内容'''
        # 忽略ssl证书警告
        requests.packages.urllib3.disable_warnings()
        try:
            r = requests.post(
                url,
                data=data,
                headers=headers,
                files=files,
                verify=False,
                timeout=timeout)
            Log().info("请求的内容：%s" % data)
            # 获取返回的状态码
            status_code = r.status_code
            Log().info("获取返回的状态码：%d" % status_code)
            # 响应内容，json类型转化成python数据类型
            # response_json = r.json()
            # Log().info("响应内容：%s" % response_json)
            # 返回响应码，响应内容
            # Log().debug(r.request.headers)
            return status_code, r
        except BaseException as e:
            Log().error("请求失败！")

    def post_json(self, url, data=None, headers=None, timeout=8):
        '''封装post方法，并用json格式传值，return响应码和响应内容'''
        # 忽略ssl证书警告
        requests.packages.urllib3.disable_warnings()
        try:
            # python数据类型转化为json数据类型
            data = json.dumps(data).encode('utf-8')
            r = requests.post(
                url,
                data=data,
                headers=headers,
                verify=False,
                timeout=timeout)
            Log().info("请求的内容：%s" % data)
            # 获取返回的状态码
            status_code = r.status_code
            Log().info("获取返回的状态码：%d" % status_code)
            # 响应内容，json类型转化成python数据类型
            # response = r.json()
            # Log().info("响应内容：%s" % response)
            # 返回响应码，响应内容
            return status_code, r
        except BaseException as e:
            Log().error("请求失败！")

    def put(self, url, data=None, headers=None, files=None, timeout=8):
        '''封装put请求，return响应码和响应内容'''
        # 忽略ssl证书警告
        requests.packages.urllib3.disable_warnings()
        try:
            r = requests.put(
                url,
                data=data,
                headers=headers,
                files=files,
                verify=False,
                timeout=timeout)
            Log().info("请求的内容：%s" % data)
            # 获取返回的状态码
            status_code = r.status_code
            Log().info(u"获取返回的状态码：%d" % status_code)
            # 响应内容，json类型转化成python数据类型
            # response_json = r.json()
            # Log().info("响应内容：%s" % response_json)
            # 返回响应码，响应内容
            return status_code, r
        except BaseException as e:
            Log().error("请求失败！")

    def put_json(self, url, data=None, headers=None, timeout=8):
        '''封装put方法，并用json格式传值，return响应码和响应内容'''
        # 忽略ssl证书警告
        requests.packages.urllib3.disable_warnings()
        try:
            # python数据类型转化为json数据类型
            data = json.dumps(data).encode('utf-8')
            r = requests.put(
                url,
                data=data,
                headers=headers,
                verify=False,
                timeout=timeout)
            Log().info("请求的内容：%s" % data)
            # 获取返回的状态码
            status_code = r.status_code
            Log().info("获取返回的状态码：%d" % status_code)
            # 响应内容，json类型转化成python数据类型
            # response = r.json()
            # Log().info("响应内容：%s" % response)
            # 返回响应码，响应内容
            return status_code, r
        except BaseException as e:
            Log().error("请求失败！")

    def delete(self, url, data=None, headers=None, files=None, timeout=8):
        '''封装delete请求，return响应码和响应内容'''
        # 忽略ssl证书警告
        requests.packages.urllib3.disable_warnings()
        try:
            r = requests.delete(
                url,
                data=data,
                headers=headers,
                files=files,
                verify=False,
                timeout=timeout)
            Log().info("请求的内容：%s" % data)
            # 获取返回的状态码
            status_code = r.status_code
            Log().info(u"获取返回的状态码：%d" % status_code)
            # 响应内容，json类型转化成python数据类型
            # response_json = r.json()
            # Log().info("响应内容：%s" % response_json)
            # 返回响应码，响应内容
            return status_code, r
        except BaseException as e:
            Log().error("请求失败！")

    def patch(self, url, data=None, headers=None, files=None, timeout=8):
        '''封装patch请求，return响应码和响应内容'''
        # 忽略ssl证书警告
        requests.packages.urllib3.disable_warnings()
        try:
            r = requests.patch(
                url,
                data=data,
                headers=headers,
                files=files,
                verify=False,
                timeout=timeout)
            Log().info("请求的内容：%s" % data)
            # 获取返回的状态码
            status_code = r.status_code
            Log().info(u"获取返回的状态码：%d" % status_code)
            # 响应内容，json类型转化成python数据类型
            # response_json = r.json()
            # Log().info("响应内容：%s" % response_json)
            # 返回响应码，响应内容
            return status_code, r
        except BaseException as e:
            Log().error("请求失败！")


if __name__ == '__main__':
    url = 'https://www.sojson.com/open/api/weather/json.shtml'
    payloda = {'city': '上海'}
    s = webrequests()
    s.get(url, payloda)