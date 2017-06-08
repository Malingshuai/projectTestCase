# -*- coding: utf-8 -*-
"""测试目的：iwebshop后台登录场景测试用例
编写时间：2016-10-15
"""
import sys
import unittest
# 将文件路径添加到运行环境变量，方便程序查找
sys.path.append("../models")
sys.path.append("../page_obj")
from iwebshop.iwebshop.test_case.models import myunit, function, driver
from iwebshop.iwebshop.test_case.page_obj.backSystem.backLoginPage import backlogin
from iwebshop.iwebshop.test_case.page_obj.backSystem.backSystemPage import JiBenSheZhi, BackSystem, ShouYeHuanDengSheZhi, DaoHangSheZhi, ZhanDianDiBuXinXi, GouWuSheZhi

class backLoginTest(myunit.MyTest):
    """iwebshop后台登录功能测试"""
    def setUp(self):
        self.driver = driver.browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        backlogin(self.driver, 'http://localhost/iwebshop/index.php?controller=systemadmin&action=index').adminLogin()

    def test_JiBenSheZhi(self,shangpinname="iwebshops", url="http://www.baidus.com"):
        """"验证网站基本设置"""
        cd = BackSystem(self.driver)
        cd.click_wangzhanguanli()
        jd = JiBenSheZhi(cd.driver)
        jd.input_shangdianName(shangpinname)
        jd.input_shangdiandizhi(url)
        jd.input_lianxiren('')
        jd.click_submit()
        self.assertEqual(jd.get_prompt(), u"保存成功", msg="测试不通过！")
        function.insert_img(self.driver, u"登录名不能为空.jpg")


if __name__ == '__main__':
    try:
        suite = unittest.TestSuite()
        suite.addTest(backLoginTest("test_JiBenSheZhi"))
        runner = unittest.TextTestRunner()
        runner.run(suite)
    except:
        print "元素无法定位"
