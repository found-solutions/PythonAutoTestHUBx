# -*- coding: utf-8 -*-


import inspect


def get_current_function_name():
    # 获取当前运行的函数
    return inspect.stack()[1][3]

# class MyClass:
#     def function_one(self):
#         # name = "%s.%s"%(self.__class__.__name__, get_current_function_name())
#         name = "%s" % (self.__class__.__name__)
#         return name


# if __name__ == '__main__':
# myclass = MyClass()
# print(myclass.function_one())