# -*- coding: utf-8 -*-

import os
import configparser
import json


def read_config(section, option):
    # 读取配置文件节点内容

    # 获取当前文件的路径
    file_path = os.path.dirname(__file__)
    # 获取配置文件config.ini的路径
    config_path = os.path.join(file_path, 'config.ini')
    # print(config_path)

    conf = configparser.ConfigParser()
    conf.read(config_path, encoding='UTF-8')
    parment = conf.get(section, option)
    return parment


def write_config(section, option, value):
    # 添加节点/修改节点的值

    # 获取当前文件的路径
    file_path = os.path.dirname(__file__)
    # 获取配置文件config.ini的路径
    config_path = os.path.join(file_path, 'config.ini')
    # print(config_path)

    conf = configparser.ConfigParser()
    conf.read(config_path, encoding='UTF-8')

    if not conf.has_section(section):
        # 检查节点是否存在，不存在就创建并添加option键值对
        conf.add_section(section)
        conf.set(section, option, value)
    else:
        conf.set(section, option, value)

    with open(config_path, 'w') as f:
        conf.write(f)

    f.close()


def read_json(filename):
    # 读取json文件内容
    func_path = os.path.dirname(__file__)
    base_dir = os.path.dirname(func_path)

    # 将路径转化为字符串
    base_dir = str(base_dir)

    # 对路径的字符串进行替换
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/model')[0]

    json_file = base + '/Templates/' + filename

    f = open(json_file, encoding='utf-8')

    json_info = json.load(f)
    f.close()
    return json_info


def read_txt():
    '''
    读取SMTP配置文件内容
    :return: 遍历输出到file_msg
    '''
    dir_path = os.path.dirname(__file__)
    filename = 'myemail.txt'
    file = dir_path + '/' + filename
    file_msg = []

    f = open(file)
    lines = f.readlines()

    for line in lines:
        line = line.strip('\n')
        file_msg.append(line)

    f.close()
    return file_msg


if __name__ == '__main__':
    r = read_json('userinfo.json')
    print(r)
