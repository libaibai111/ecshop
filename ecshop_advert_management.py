# 1、打开后台页面
# 2、登录
# 3、点击【广告管理】
# 4、点击【广告列表】
# 5、点击【添加广告】
# 6、生成并复制js代码
# 7、点击编辑图标
# 8、点击移除图标
# 9、点击退出
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 1、打开后台页面
driver = webdriver.Chrome()
url = 'http://localhost/upload/admin/privilege.php?act=login'
driver.get(url)
time.sleep(1)
driver.maximize_window()
time.sleep(1)

# 2、登录
#    输入用户名
driver.find_element(By.NAME,"username").send_keys("李白")
time.sleep(0.5)
#    输入密码
driver.find_element(By.NAME,"password").send_keys("aaa535889071")
time.sleep(0.5)
#    点击【进入管理中心】
driver.find_element(By.CLASS_NAME,"button").click()
time.sleep(2)

# 3、点击【广告管理】
driver.switch_to.frame("menu-frame")  # 进入左侧的menu-frame
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[4]').click()
time.sleep(1)

# 4、点击【广告列表】
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[4]/ul/li[1]/a').click()
time.sleep(1)

# 5、点击【添加广告】
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
driver.find_element(By.XPATH,'/html/body/h1/span[1]/a').click()
time.sleep(1)
#    输入广告名称
driver.find_element(By.NAME,'ad_name').send_keys("限时促销")
time.sleep(0.5)
#    选择媒介类型
element = driver.find_element(By.NAME,'media_type')
element.click()
time.sleep(0.5)
Select(element).select_by_value('0')
time.sleep(0.5)
#    选择广告位置
element = driver.find_element(By.NAME,'position_id')
element.click()
time.sleep(0.5)
Select(element).select_by_value('0')
time.sleep(0.5)
#    选择开始日期
js = "document.getElementById('start_time').removeAttribute('readonly')"
driver.execute_script(js)
driver.find_element(By.XPATH,'//input[@id="start_time"]').clear()
time.sleep(0.5)
driver.find_element(By.XPATH,'//input[@id="start_time"]').send_keys('2020-07-20')
time.sleep(0.5)
#    选择结束日期
js = "document.getElementById('end_time').removeAttribute('readonly')"
driver.execute_script(js)
driver.find_element(By.XPATH,'//input[@id="end_time"]').clear()
time.sleep(0.5)
driver.find_element(By.XPATH,'//input[@id="end_time"]').send_keys('2020-10-20')
time.sleep(0.5)
#    输入广告链接
driver.find_element(By.XPATH,'//tbody[@id="0"]/tr[1]/td[2]/input').send_keys('http://www.taobao.com')
time.sleep(0.5)
#    点击选择文件
driver.find_element(By.XPATH,'//tbody[@id="0"]/tr[2]/td[2]/input').send_keys('D:\海德\网络拓扑图.jpg')
time.sleep(0.5)
#    选择开启
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody[6]/tr[1]/td[2]/input[1]').click()
time.sleep(0.5)
#    输入广告联系人
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody[6]/tr[2]/td[2]/input').send_keys('花花')
time.sleep(0.5)
#    输入联系人Email
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody[6]/tr[3]/td[2]/input').send_keys('147896@qq.com')
time.sleep(0.5)
#    输入联系电话
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody[6]/tr[4]/td[2]/input').send_keys('12346789')
time.sleep(0.5)
#    点击【确定】
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody[6]/tr[5]/td[2]/input[1]').click()
time.sleep(5)

# 6、生成并复制js代码
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("menu-frame")  # 进入左侧的menu-frame
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[4]/ul/li[1]/a').click()
time.sleep(1)
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[3]/td[8]/span/a[1]/img').click()
time.sleep(1)
#    输入投放广告的站点名称
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[1]/td[2]/input').send_keys('111')
time.sleep(0.5)
#    选择编码
element = driver.find_element(By.ID,'charset')
element.click()
time.sleep(0.5)
Select(element).select_by_index(0)
time.sleep(0.5)
#    点击【生成并复制js代码】
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[3]/td/div/input').send_keys('111')
time.sleep(0.5)
#    回退上一页面
driver.back()
time.sleep(1)

# 7、点击编辑图标
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[3]/td[8]/span/a[2]/img').click()
time.sleep(1)
#    修改广告名称
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody[1]/tr[1]/td[2]/input').clear()
time.sleep(0.5)
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody[1]/tr[1]/td[2]/input').send_keys('聚划算')
time.sleep(0.5)
#    回退上一页面
driver.back()
time.sleep(1)

# 8、点击移除图标
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[3]/td[8]/span/a[3]/img').click()  # 点击移除图标
time.sleep(3)
#    点击【确定】
driver.switch_to.alert.accept()
time.sleep(3)

# 9、点击退出
driver.switch_to.default_content()  # 跳出最外层
driver.switch_to.frame("header-frame")  # 进入顶部的header-frame
driver.find_element(By.XPATH,'//div[@id="submenu-div"]/ul/li[1]/a/img').click()  # 点击退出
time.sleep(3)

driver.quit()

