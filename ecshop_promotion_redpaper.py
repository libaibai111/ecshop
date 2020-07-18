# 1、打开页面并访问
# 2、登录
# 3、点击【促销管理】
# 4、点击【红包类型】
# 5、添加红包类型
# 6、发放红包
# 7、查看红包
# 8、编辑红包
# 9、移除红包
# 10、退出登录

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
driver.find_element(By.NAME,"username").clear()
time.sleep(0.5)
driver.find_element(By.NAME,"username").send_keys("李白")
time.sleep(0.5)
#    输入密码
driver.find_element(By.NAME,"password").clear()
time.sleep(0.5)
driver.find_element(By.NAME,"password").send_keys("aaa535889071")
time.sleep(0.5)
#    点击【进入管理中心】
driver.find_element(By.CLASS_NAME,"button").click()
time.sleep(1)

# 3、点击【促销管理】
driver.switch_to.frame("menu-frame")  # 进入左侧的menu-frame
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[2]').click()
time.sleep(1)

# 4、点击【红包类型】
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[2]/ul/li[2]/a').click()
time.sleep(1)

# 5、添加红包类型
#   点击【添加红包类型】
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
driver.find_element(By.XPATH,'/html/body/h1/span[1]/a').click()  # 点击【添加红包类型】
time.sleep(1)
#   输入类型名称
driver.find_element(By.NAME,'type_name').send_keys('普通红包')  # 输入类型名称
time.sleep(0.5)
#   输入红包金额
driver.find_element(By.NAME,'type_money').send_keys('10')  # 输入红包金额
time.sleep(0.5)
#   输入最小订单金额
driver.find_element(By.NAME,'min_goods_amount').send_keys('100')  # 输入最小订单金额
time.sleep(0.5)
#   选择发放红包方式
driver.find_element(By.XPATH,'//table/tbody/tr[4]/td[2]/input[2]').click()  # 选择按商品发放
time.sleep(0.5)
#   输入发放起始日期
js = "document.getElementById('send_start_date').removeAttribute('readonly')"  # 移除元素readonly属性
driver.execute_script(js)
driver.find_element(By.ID,'send_start_date').clear()
time.sleep(0.5)
driver.find_element(By.ID,'send_start_date').send_keys('2020-08-20')
time.sleep(0.5)
#   输入发放结束日期
js = "document.getElementById('send_end_date').removeAttribute('readonly')"  # 移除元素readonly属性
driver.execute_script(js)
driver.find_element(By.ID,'send_end_date').clear()
time.sleep(0.5)
driver.find_element(By.ID,'send_end_date').send_keys('2020-10-20')
time.sleep(0.5)
#   输入使用结束日期
js = "document.getElementById('use_start_date').removeAttribute('readonly')"  # 移除元素readonly属性
driver.execute_script(js)
driver.find_element(By.ID,'use_start_date').clear()
time.sleep(0.5)
driver.find_element(By.ID,'use_start_date').send_keys('2020-08-20')
time.sleep(0.5)
#   输入使用结束日期
js = "document.getElementById('use_end_date').removeAttribute('readonly')"  # 移除元素readonly属性
driver.execute_script(js)
driver.find_element(By.ID,'use_end_date').clear()
time.sleep(0.5)
driver.find_element(By.ID,'use_end_date').send_keys('2020-10-20')
time.sleep(0.5)
#   点击【确定】
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[10]/td[2]/input[1]').click()  # 点击【确定】
time.sleep(5)

# 6、发放红包
# 点击【发放】
driver.switch_to.default_content()  # 跳到最顶层
driver.switch_to.frame("menu-frame")  # 进入左侧的menu-frame
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[2]/ul/li[2]/a').click()  # 点击【红包类型】
time.sleep(1)
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
time.sleep(1)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[7]/a[1]').click()  # 点击【发放】
time.sleep(1)
# 选择商品分类
element = driver.find_element(By.NAME,'cat_id')
element.click()
time.sleep(1)
Select(element).select_by_value('21')
time.sleep(1)
# 选择商品品牌
element = driver.find_element(By.NAME,'brand_id')
element.click()
time.sleep(1)
Select(element).select_by_value('3')
time.sleep(1)
# 输入关键字
driver.find_element(By.XPATH,'/html/body/div[1]/form/input[1]').send_keys('西装')
time.sleep(0.5)
# 点击【搜索】
driver.find_element(By.XPATH,'/html/body/div[1]/form/input[2]').click()
time.sleep(0.5)
# 选择商品
driver.find_element(By.ID,'120.00').click()
time.sleep(1)
# 点击【>>】
driver.find_element(By.XPATH,'/html/body/div[2]/form/table/tbody/tr[2]/td[2]/p[1]/input').click()
time.sleep(1)
# 点击【发放】
driver.find_element(By.XPATH,'/html/body/div[2]/form/table/tbody/tr[3]/td/input').click()
time.sleep(3)

# 7、查看红包
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[7]/a[2]').click()
time.sleep(3)

# 8、编辑红包
driver.back()  # 后退到上一个页面
time.sleep(1)   # 停留1秒
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
time.sleep(1)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[7]/a[3]').click()
time.sleep(1)
# 修改类型名称
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[1]/td[2]/input').clear()
time.sleep(0.5)
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[1]/td[2]/input').send_keys('限量红包')
time.sleep(0.5)
# 点击【确定】
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[10]/td[2]/input[1]').click()  # 点击【确定】
time.sleep(5)

# 9、移除红包
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[7]/a[4]').click()
time.sleep(2)
# 点击【确定】
driver.switch_to.alert.accept()  # 确定删除
time.sleep(3)

# 10、退出登录
driver.switch_to.default_content()  # 跳出最外层
driver.switch_to.frame("header-frame")  # 进入顶部的header-frame
driver.find_element(By.XPATH,'//div[@id="submenu-div"]/ul/li[1]/a/img').click()  # 点击退出
time.sleep(3)

driver.quit()