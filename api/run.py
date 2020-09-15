# -*- coding: utf-8 -*-
# @Author ：Mingjie Huang
# @Time   ：2019/7/5 19:31
# @IDE    ：PyCharm

if __name__ == '__main__':
    import pytest
    import time
    from comm.function import send_mail
    '''
    -m:只运行相应标识的用例(如：-m test.py::class::test)
    -v:详细结果
    -s:打印print信息
    '''
    testcase_dir='./lifebyte_new_crm'
    testreport_dir='./test_report'

    now=time.strftime('%Y-%m-%d %H_%M_%S')
    reportname=testreport_dir+'/'+now+' test_report.html'
    # pytest.main(["-s", "{}".format(testcase_dir),"-m=level_2","--reruns=3","-n=2", "--dist=loadscope","--html={}".format(reportname),"--self-contained-html"])
    pytest.main(["{}".format(testcase_dir),"--reruns=2", "-n=2", "--dist=loadscope","--html={}".format(reportname), "--self-contained-html"])
    # pytest.main(['-v', 'lifebyte_new_crm/'])
