import os

# allure配置
# 获取项目根目录
base_dir = os.path.abspath(os.path.dirname(__file__))

# 设置相关目录
lib_dir = os.path.join(base_dir, 'lib')
report_dir = os.path.join(base_dir, 'report')
tests_dir = os.path.join(base_dir, 'lifebyte_new_HUBx/')