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

#5、进入添加管理员页面

time.sleep(2)
#进入menu frame
driver.switch_to.default_content()
driver.switch_to.frame('menu-frame')
#点击权限管理
driver.find_element_by_css_selector('[class="collapse lis ico_8"]').click()
#点击添加管理员列表
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[8]/ul/li[1]/a').click()
#进入main frame
driver.switch_to.parent_frame()
driver.switch_to.frame('main-frame')
time.sleep(2)
#进入添加管理员页面
driver.find_element(By.XPATH,'//span[@class="action-span"]/a').click()

#6、添加管理员

passwd='admin123'
#输入用户名
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[1]/td[2]/input').clear()
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[1]/td[2]/input').send_keys('admin2')
#输入邮箱
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[2]/td[2]/input').clear()
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[2]/td[2]/input').send_keys('admin2@qq.com')
#输入密码
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[3]/td[2]/input').click()
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[3]/td[2]/input').send_keys(passwd)
#输入确认密码
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[4]/td[2]/input').click()
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[4]/td[2]/input').send_keys(passwd)
#选择角色
element=driver.find_element(By.NAME,'select_role')
select=Select(element)
select.select_by_value('2')
#提交
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[6]/td/input[1]').click()

#7、进入分派权限页

#进入menu frame
driver.switch_to.default_content()
driver.switch_to.frame('menu-frame')
#点击管理员列表
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[8]/ul/li[1]/a').click()
#进入main frame
time.sleep(2)
driver.switch_to.parent_frame()
driver.switch_to.frame('main-frame')
time.sleep(2)
#wait=WebDriverWait(driver,10,0.5)
#wait.until(EC.presence_of_element_located((By.XPATH,'//table[@id="list-table"]/tbody/tr[2]/td[5]/a[1]/img')))
#点击分派权限
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[2]/td[5]/a[1]/img').click()

#8、设置权限

#全选
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[12]/td/input[1]').click()
#提交
driver.find_element(By.XPATH,'//input[@class="button" and @name="Submit"]').click()

#9、进入搜索管理员日志

#进入menu frame
driver.switch_to.default_content()
driver.switch_to.frame('menu-frame')
#点击管理员列表
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[8]/ul/li[1]/a').click()
#进入main frame
time.sleep(2)
driver.switch_to.parent_frame()
driver.switch_to.frame('main-frame')
time.sleep(2)
#点击搜索
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[2]/td[5]/a[2]/img').click()

#10、搜索并删除管理员日志

time.sleep(2)
#搜索ip
sel=driver.find_element(By.NAME,'ip')
select=Select(sel)
select.select_by_value('0.0.0.0')
time.sleep(2)
#点击确定
driver.find_element(By.XPATH,'//input[@type="submit" and @class="button"]').click()
#搜索清除日志
sel2=driver.find_element(By.CSS_SELECTOR,'[name="log_date"]')
select=Select(sel2)
select.select_by_value('1')
#点击确定
time.sleep(2)
driver.find_element(By.XPATH,'//input[@name="drop_type_date" and @class="button"]').click()

#11、进入编辑管理员页面

#进入menu frame
driver.switch_to.default_content()
driver.switch_to.frame('menu-frame')
time.sleep(2)
#点击管理员列表
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[8]/ul/li[1]/a').click()
#进入main frame
time.sleep(2)
driver.switch_to.parent_frame()
driver.switch_to.frame('main-frame')
#点击编辑
time.sleep(2)
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[2]/td[5]/a[3]/img').click()

#12、编辑管理员信息

passwdnew='admin1234'
time.sleep(2)
#修改用户名
driver.find_element(By.XPATH,'//input[@name="user_name" and @type="text"]').clear()
driver.find_element(By.XPATH,'//input[@name="user_name" and @type="text"]').send_keys('admin3')
#修改邮箱
driver.find_element(By.XPATH,'//input[@name="email" and @type="text"]').clear()
driver.find_element(By.XPATH,'//input[@name="email" and @type="text"]').send_keys('admin3@qq.com')
#输入旧密码
driver.find_element(By.XPATH,'//input[@name="old_password" and @type="password"]').clear()
driver.find_element(By.XPATH,'//input[@name="old_password" and @type="password"]').send_keys(passwd)
#输入新密码
driver.find_element(By.XPATH,'//input[@name="new_password" and @type="password"]').clear()
driver.find_element(By.XPATH,'//input[@name="new_password" and @type="password"]').send_keys(passwdnew)
#输入确认密码
driver.find_element(By.XPATH,'//input[@name="pwd_confirm" and @type="password"]').clear()
driver.find_element(By.XPATH,'//input[@name="pwd_confirm" and @type="password"]').send_keys(passwdnew)
#选择角色
role=driver.find_element(By.CSS_SELECTOR,'[name="select_role"]')
select=Select(role)
select.select_by_value('1')
#点击提交
driver.find_element(By.XPATH,'//input[@type="submit" and @class="button"]').click()

#13、移除管理员

time.sleep(2)
#进入menu frame
driver.switch_to.default_content()
driver.switch_to.frame('menu-frame')
#点击管理员列表
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[8]/ul/li[1]/a').click()
#进入main frame
time.sleep(2)
driver.switch_to.parent_frame()
driver.switch_to.frame('main-frame')
time.sleep(2)
#点击移除
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[2]/td[5]/a[4]/img').click()
time.sleep(2)
#点击确定
driver.switch_to.alert.accept()

#14、退出浏览器

time.sleep(3)
driver.quit()

