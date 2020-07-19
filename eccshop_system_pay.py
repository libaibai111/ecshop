# 1、打开并访问网页
# 2、登录
# 3、点击【系统设置】
# 4、点击【支付方式】
# 5、安装支付宝
# 6、编辑支付宝
# 7、删除支付宝
# 8、退出

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 1、打开后台页面
driver = webdriver.Chrome()
url = 'http://localhost/upload/admin/privilege.php?act=login'
driver.get(url=url)
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
print("登录成功")

# 3、点击【系统设置】
driver.switch_to.frame("menu-frame")  # 进入左侧的menu-frame
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]').click()
time.sleep(1)

# 4、点击【支付方式】
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]/ul/li[3]/a').click()
time.sleep(1)

# 5、安装支付宝
#    点击安装
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[7]/a').click()  # 点击安装
time.sleep(1)
#    输入支付方式名称
driver.find_element(By.NAME,"pay_name").clear()  # 清空支付方式名称
time.sleep(0.5)
driver.find_element(By.NAME,"pay_name").send_keys('<font color="#FF0000">支付宝</font>')  #输入支付方式名称
time.sleep(0.5)
#    输入支付方式描述
driver.find_element(By.NAME,"pay_desc").clear()  # 清空支付方式描述
time.sleep(0.5)
driver.find_element(By.NAME,"pay_desc").send_keys('支付宝网站(www.alipay.com) 是国内先进的网上支付平台。<br/>支付宝收款'
                                                  '接口：在线即可开通，<font color="red"><b>零预付，免年费</b></font>，'
                                                  '单笔阶梯费率，无流量限制。<br/><a href="http://cloud.ecshop.com/payment'
                                                  '_apply.php?mod=alipay" target="_blank"><font color="red">立即在线申请'
                                                  '</font></a>')  # 输入支付方式描述
time.sleep(0.5)
#    输入支付宝账户
driver.find_element(By.XPATH,"/html/body/form/div/table/tbody/tr[3]/td[2]/input[1]").clear()  # 清空支付宝账户
time.sleep(0.5)
driver.find_element(By.XPATH,"/html/body/form/div/table/tbody/tr[3]/td[2]/input[1]").send_keys('18340808112')  # 输入支付宝账户
time.sleep(0.5)
#    输入交易安全检验码
driver.find_element(By.XPATH,"/html/body/form/div/table/tbody/tr[4]/td[2]/input[1]").clear()  # 清空交易安全检验码
time.sleep(0.5)
driver.find_element(By.XPATH,"/html/body/form/div/table/tbody/tr[4]/td[2]/input[1]").send_keys('333666')  # 输入交易安全检验码
time.sleep(0.5)
#    输入合作者身份id
driver.find_element(By.XPATH,"/html/body/form/div/table/tbody/tr[5]/td[2]/input[1]").clear()  # 清空合作者身份id
time.sleep(0.5)
driver.find_element(By.XPATH,"/html/body/form/div/table/tbody/tr[5]/td[2]/input[1]").send_keys('0001')  # 输入合作者身份id
time.sleep(0.5)
#    选择接口类型
element = driver.find_element(By.XPATH,"/html/body/form/div/table/tbody/tr[6]/td[2]/select")  # 点击下拉框
element.click()
time.sleep(0.5)
Select(element).select_by_index(0)  # 选择使用标准双接口
time.sleep(3)
#    输入支付手续费
driver.find_element(By.XPATH,"/html/body/form/div/table/tbody/tr[7]/td[2]/input").clear()  # 清空支付手续费
time.sleep(0.5)
driver.find_element(By.XPATH,"/html/body/form/div/table/tbody/tr[7]/td[2]/input").send_keys('1')  # 输入支付手续费
time.sleep(0.5)
#    点击【确定】
driver.find_element(By.XPATH,"/html/body/form/div/table/tbody/tr[10]/td/input[5]").click()  # 点击【确定】
time.sleep(5)
print("安装成功")

# 6、编辑支付宝
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[7]/a[2]').click()  # 点击编辑图标
time.sleep(0.5)
driver.find_element(By.XPATH,"/html/body/form/div/table/tbody/tr[1]/td[2]/input").clear()  # 清空支付方式名称
time.sleep(0.5)
driver.find_element(By.XPATH,"/html/body/form/div/table/tbody/tr[1]/td[2]/input").send_keys('支付宝')  # 输入支付方式名称
time.sleep(0.5)
#    点击【确定】
driver.find_element(By.XPATH,"/html/body/form/div/table/tbody/tr[10]/td/input[5]").click()  # 点击【确定】
time.sleep(5)
print("编辑成功")

# 7、卸载支付宝
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[7]/a[1]').click()  # 点击卸载
time.sleep(3)
driver.switch_to.alert.accept()  # 确定删除
time.sleep(5)
print("卸载成功")

# 8、退出
driver.switch_to.default_content()  # 跳出最外层
driver.switch_to.frame("header-frame")  # 进入顶部的header-frame
driver.find_element(By.XPATH,'//div[@id="submenu-div"]/ul/li[1]/a/img').click()
time.sleep(5)
print("退出登录")

driver.quit()