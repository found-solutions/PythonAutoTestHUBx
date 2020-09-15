# -*- coding: utf-8 -*-


import logging
import time
import os


# log_path是存放日志的路径
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs')

# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):
    os.mkdir(log_path)


class Log():

    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(
            log_path, '%s.log' %
            time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        # self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
        self.formatter = logging.Formatter(
            '[%(asctime)s] - %(levelname)s: %(message)s')

    def printconsole(self, level, message):

        # 创建一个FileHandler，用于写到本地
        f = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        f.setLevel(logging.DEBUG)
        f.setFormatter(self.formatter)
        self.logger.addHandler(f)

        # 创建一个StreamHandler,用于输出到控制台
        s = logging.StreamHandler()
        s.setLevel(logging.DEBUG)
        s.setFormatter(self.formatter)
        self.logger.addHandler(s)

        # 区分日志级别
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 避免日志输出重复问题
        self.logger.removeHandler(s)
        self.logger.removeHandler(f)

        # 关闭打开的文件
        f.close()

    def debug(self, message):
        self.printconsole('debug', message)

    def info(self, message):
        self.printconsole('info', message)

    def warning(self, message):
        self.printconsole('warning', message)

    def error(self, message):
        self.printconsole('error', message)


if __name__ == '__main__':
    log = Log()
    log.info("----------自动化测试开始----------")
    log.info("测试...")
    log.warning("-----------自动化测试结束----------")
