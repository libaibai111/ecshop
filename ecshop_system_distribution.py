'''
权限模块
'''
#1、引入驱动

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#2、打开ecshop

driver=webdriver.Chrome()
url='http://192.168.1.39/upload/admin/index.php'
driver.get(url=url)
driver.maximize_window()
driver.implicitly_wait(10)

#3、输入用户名密码

driver.find_element(By.NAME,'username').send_keys('admin')
driver.find_element(By.NAME,'password').send_keys('Pml19950101')

#4、登录并保存

driver.find_element(By.ID,'remember').click()
driver.find_element(By.XPATH,'//input[@type="submit" and @class="button"]').click()

#5、进入配送方式页面

time.sleep(2)
#进入menu frame
driver.switch_to.default_content()
driver.switch_to.frame('menu-frame')
#点击系统设置
driver.find_element_by_css_selector('[class="collapse lis ico_9"]').click()
#点击配送方式
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]/ul/li[4]/a').click()

#6、安装城际快递

#进入main frame
time.sleep(2)
driver.switch_to.parent_frame()
driver.switch_to.frame('main-frame')
time.sleep(2)
#点击安装
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[3]/td[8]/a').click()

#7、新增配送区域

time.sleep(4)
#输入配送区域名称
driver.find_element(By.CSS_SELECTOR,'[name="shipping_area_name"]').clear()
driver.find_element(By.CSS_SELECTOR,'[name="shipping_area_name"]').send_keys("锦江区")
#输入基本费用
driver.find_element(By.XPATH,'//input[@type="text" and @name="base_fee"]').clear()
driver.find_element(By.XPATH,'//input[@type="text" and @name="base_fee"]').send_keys('10')
#输入免费额度
driver.find_element(By.XPATH,'//input[@type="text" and @name="free_money"]').clear()
driver.find_element(By.XPATH,'//input[@type="text" and @name="free_money"]').send_keys('0')
#输入货到付款支付费用
driver.find_element(By.XPATH,'//input[@type="text" and @name="pay_fee"]').clear()
driver.find_element(By.XPATH,'//input[@type="text" and @name="pay_fee"]').send_keys('20')
#选择国家
sel3=driver.find_element(By.ID,'selCountries')
select=Select(sel3)
select.select_by_value('1')
#选择省份
sel4=driver.find_element(By.ID,'selProvinces')
select=Select(sel4)
select.select_by_value('26')
#选择城市
sel5=driver.find_element(By.ID,'selCities')
select=Select(sel5)
select.select_by_value('322')
#选择区/县
sel6=driver.find_element(By.ID,'selDistricts')
select=Select(sel6)
select.select_by_value('2723')
#点击新增
driver.find_element(By.XPATH,'//input[@type="button" and @class="button"]').click()
#点击确定
driver.find_element(By.XPATH,'//input[@type="submit" and @class="button"]').click()
time.sleep(5)

#8、编辑配送区域

#点击编辑
driver.find_element(By.XPATH,'//table[@id="listTable"]/tbody/tr[2]/td[4]/a[1]').click()
time.sleep(4)
#编辑配送区域名称
driver.find_element(By.CSS_SELECTOR,'[name="shipping_area_name"]').clear()
driver.find_element(By.CSS_SELECTOR,'[name="shipping_area_name"]').send_keys("西城区")
#编辑基本费用
driver.find_element(By.XPATH,'//input[@type="text" and @name="base_fee"]').clear()
driver.find_element(By.XPATH,'//input[@type="text" and @name="base_fee"]').send_keys('15')
#编辑免费额度
driver.find_element(By.XPATH,'//input[@type="text" and @name="free_money"]').clear()
driver.find_element(By.XPATH,'//input[@type="text" and @name="free_money"]').send_keys('1')
#编辑货到付款支付费用
driver.find_element(By.XPATH,'//input[@type="text" and @name="pay_fee"]').clear()
driver.find_element(By.XPATH,'//input[@type="text" and @name="pay_fee"]').send_keys('25')
#选择国家
sel3=driver.find_element(By.ID,'selCountries')
select=Select(sel3)
select.select_by_value('1')
#选择省份
sel4=driver.find_element(By.ID,'selProvinces')
select=Select(sel4)
select.select_by_value('2')
#选择城市
sel5=driver.find_element(By.ID,'selCities')
select=Select(sel5)
select.select_by_value('52')
#选择区/县
sel6=driver.find_element(By.ID,'selDistricts')
select=Select(sel6)
select.select_by_value('501')
#点击新增
driver.find_element(By.XPATH,'//input[@type="button" and @class="button"]').click()
#取消勾选锦江区
driver.find_element(By.XPATH,'//td[@id="regionCell"]/input[1]').click()
#点击确定
driver.find_element(By.XPATH,'//input[@type="submit" and @class="button"]').click()
time.sleep(5)

#9、移除配送区域

#勾选配送区域
driver.find_element(By.XPATH,'//table[@id="listTable"]/tbody/tr[2]/td[1]/input').click()
#点击移除选定的配送区域
driver.find_element(By.ID,'btnSubmit').click()
#点击确定
time.sleep(2)
driver.switch_to.alert.accept()

#10、卸载城际快递

#进入配送方式页面
time.sleep(2)
#进入menu frame
driver.switch_to.default_content()
driver.switch_to.frame('menu-frame')
#点击配送方式
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]/ul/li[4]/a').click()
#进入main frame
driver.switch_to.parent_frame()
driver.switch_to.frame('main-frame')
time.sleep(2)
#点击卸载
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[3]/td[8]/a[1]').click()
time.sleep(1)
driver.switch_to.alert.accept()

#11、退出浏览器

time.sleep(4)
driver.quit()