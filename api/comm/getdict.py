# -*- coding: utf-8 -*-
# @Author ：Mingjie Huang
# @Time   ：2019/7/4 19:01
# @IDE    ：PyCharm

def getdict(dict1, obj, default=None):
    ''' 遍历嵌套字典，得到想要的value
        dict1所需遍历的字典
        obj 所需value的键'''
    for k, v in dict1.items():
        if k == obj:
            return v
        else:
            if type(v) is dict:  # 如果是字典
                re = getdict(v, obj, default)  # 递归
                if re is not default:
                    return re

if __name__ == '__main__':
    response = {'errno': 0, 'msg': 'success',
                'result': {'id': '5b4dc7111c0ab20001c3c481', 'cname': '测试001', 'desc': '测试机器人', 'type': 0,
                           'settings': {'failAction': ['偶母鸡啊', '我不告诉你']},
                           'lastView': '2018-07-17T18:38:09.250849551+08:00', 'nickname': '小可爱', 'age': 0,
                           'gender': 'male', 'hometown': '北京', 'speciality': '打游戏'}}
    failAction = getdict(response, 'failAction')
    print(failAction)