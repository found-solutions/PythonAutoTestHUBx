# -*- coding: utf-8 -*-
# @Author ：Mingjie Huang
# @Time   ：2019/7/31 11:39
# @IDE    ：PyCharm

from locust import HttpLocust, TaskSet, task
from comm.readdoc import read_json,read_config
import json
'''性能测试任务类'''
class AdminLoginTasks(TaskSet):

#初始化函数
    def on_start(self):
        try:
            self.request_json = read_json("userinfo.json")
        except Exception as e:
            print(e)

#任务
    @task(1)
    def get_tag_vals(self):

        request_headers = {
            "Accept": read_config('projectname', 'evn_accept'),
            "Content-Type": read_config('projectname', 'evn_content-type')
        }
        request_json = self.request_json
        try:
            response = self.client.post('/api/authorizations/admin', headers=request_headers, data=request_json)
            assert 'access_token' in response.text, u'不存在access_token关键字'
        except Exception as e:
            # print(response.text)
            print ("出错了：%s"%e)
            raise
        else:
            print("恭喜，请求成功")

        # if response.status_code != 200:
        #     print ("返回内容：%s"%(response.text))
        #     print ("返回异常,请求状态码：%s"%(response.status_code))
        # elif response.status_code == 200:
        #     print ("返回成功")


class Withdrawal(TaskSet):

#初始化函数
    def on_start(self):
        try:
            self.request_json = read_json("withdrawal.json")
        except Exception as e:
            print(e)

#任务
    @task(1)
    def get_tag_vals(self):

        request_headers = {
            "Accept": read_config('projectname', 'evn_accept'),
            "Content-Type": read_config('projectname', 'evn_content-type'),
            "Authorization": read_config('projectname','evn_token'),
            "User-Agent": read_config('projectname','evn_user-agent')
        }
        request_json = self.request_json
        # try:
        #     response = self.client.post('/api/front/fundings/withdrawal', headers=request_headers, data=request_json)
        #     assert response.status_code == 200
        # except Exception as e:
        #     # print(response.text)
        #     print ("出错了：%s"%e)
        #     raise
        # else:
        #     print("恭喜，请求成功")
        response = self.client.post('/api/front/fundings/withdrawal', headers=request_headers, data=request_json)
        if response.status_code == 204:
            print("请求成功")
        else:
            print("请求失败",response.text)

#性能测试配置
class WebsiteUser(HttpLocust):
    task_set = Withdrawal
    #请求响应时间
    min_wait = 30
    max_wait = 40
    host = read_config('projectname', 'evn_baseurl')

if __name__ == '__main__':
    import os
    os.system("locust -f locust_test.py")
