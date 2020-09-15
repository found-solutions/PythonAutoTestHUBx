import os
import sys
import subprocess
import shutil

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

import config as cfg

# 构造allure报告所需要的路径
allure_raw_path = os.path.join(cfg.report_dir, 'allure_raw')
allure_cmd_path = os.path.join(cfg.lib_dir, 'allure-2.12.1', 'bin', 'allure')
allure_report_path = os.path.join(cfg.report_dir, 'allure_report')


# 执行 pytest 命令
# 需要先安装
# pip install pytest
# pip install pytest-rerunfailures 用于当用例失败时，指定重试次数。用法：--reruns 3
# pip install pytest-xdist 用于并发执行。用法：-n 并发数， 如果并发数为auto表示会自动根据CPU的数量设定并发数量。--dist=loadscope以用例类
# 为一个在分组并发执行，避免用例中有先后顺序导致运行失败
# pip install allure-pytest  用于生成 allure 报告，用法：--alluredir 结果存放路径。 注意这里allure保存的结果还不是报告，而是一堆json和文本文件
def run_test_by_pytest(test_path, rerun=2, xdist='auto', **allure):
    # 检查路径
    if allure.get('allure_raw_path') or allure.get('allure_cmd_path') or allure.get('allure_report_path'):
        raw_path = allure.get('allure_raw_path')
        cmd_path = allure.get('allure_cmd_path')
        report_path = allure.get('allure_report_path')
    else:
        try:
            raw_path = allure_raw_path
            cmd_path = allure_cmd_path
            report_path = allure_report_path
        except NameError:
            raise NameError('请先定义 allure 相关路径！')

    # 处理历史报告数据，不处理，报告中始终看不到趋势，项目第一次使用，请删除report下的所有文件
    old_results = os.path.join(report_path, 'history')
    old_results_raw = os.path.join(allure_raw_path, 'history')
    if os.path.exists(old_results):
        # 检查测试结果中有没有 history 文件夹，有则删除
        if os.path.exists(old_results_raw):
            shutil.rmtree(old_results_raw)
        # 将报告中的历史数据 history 文件夹，拷贝到测试结果中
        shutil.copytree(old_results, old_results_raw)

    # 运行 pytest 命令
    # pytest_cmd = f'pytest -s {test_path} -m=level_2 --alluredir {raw_path} --reruns {rerun} -n {xdist} --dist=loadscope'
    pytest_cmd = 'pytest -s {test_path} --alluredir {raw_path} --reruns {rerun} -n {xdist} --dist=loadscope'.format(test_path=test_path,raw_path=raw_path,rerun=rerun,xdist=xdist)
    p1 = subprocess.Popen(pytest_cmd, shell=True, stdout=subprocess.PIPE)
    if not p1.communicate()[0]:
        raise ModuleNotFoundError('请确保已安装 pytest, 可通过 pip list 查看。')

    # 运行 allure 报告生成命令
    allure_cmd = '{cmd_path} generate {raw_path} -o {report_path} --clean'.format(cmd_path=cmd_path,raw_path=raw_path,report_path=report_path)
    p2 = subprocess.Popen(allure_cmd, shell=True, stdout=subprocess.PIPE)
    out = p2.communicate()[0]
    if not out:
        raise ModuleNotFoundError('请确保 allure 命令路径是否正确，可通过参数 allure_cmd_path 指定 allure 所在的目录！')
    out = str(out, 'utf-8')
    if 'successfully' in out:
        print('报告已生成成功，请到{report_path}中查看 index.html'.format(report_path=report_path))


if __name__ == "__main__":
    test_path = cfg.tests_dir
    run_test_by_pytest(test_path)
