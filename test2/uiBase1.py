# 内网登录

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://broker-dev.mklij.com/")
# driver.find_element("class name", "change-login").click()
# driver.implicitly_wait(3)
# driver.find_element_by_xpath("//*[@type='text' and @class='el-input__inner']").send_keys('012682')
# driver.find_element_by_xpath("//*[@type='password' and @class ='el-input__inner']").send_keys('123456')
# driver.find_element_by_xpath("//button[@class='el-button el-button--primary el-button--small']").click()
# driver.implicitly_wait(2)
# driver.find_element("class name", "active").click()

'''
active
elements = driver.find_elements_by_xpath("//div[contains(@class, 'foo')]")
element = driver.find_element_by_xpath('//div/td[1]')
el-button el-button--primary el-button--small
'''

"""
底层逻辑写法
"""

from selenium.webdriver.

driver = webdriver
el = driver.excute("findelement", {"using"})
