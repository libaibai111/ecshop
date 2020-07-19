# 1、打开并访问网页
# 2、登录
# 3、点击【系统设置】
# 4、点击【商店设置】
#    输入商店名称
#    输入商店标题
#    输入商店描述
#    输入商店关键字
#    选择所在国家
#    选择所在省份
#    选择所在城市
#    输入详细地址
#    输入客服QQ好
#    输入淘宝旺旺
#    输入Skype
#    输入Yahoo Messenger
#    输入MSN Messenger
#    输入客服邮件地址
#    输入客服电话
#    选择是否暂时关闭网店
#    上传网点Logo
#    输入用户中心公告
#    是否显示 Licensed
#    输入商店公告
#    选择是否关闭注册
#    点击【确定】
# 5、退出登录

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

# 4、点击【商店设置】
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]/ul/li[1]/a').click()
time.sleep(1)
#    输入商店名称
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
driver.find_element(By.NAME,'value[101]').clear()  # 清空商店名称
time.sleep(0.5)
driver.find_element(By.NAME,'value[101]').send_keys('chuu旗舰店')  # 输入商店名称
time.sleep(0.5)
#    输入商店标题
driver.find_element(By.NAME,'value[102]').clear()  # 清空商店标题
time.sleep(0.5)
driver.find_element(By.NAME,'value[102]').send_keys('欢迎光临chuu旗舰店')  # 输入商店标题
time.sleep(0.5)
#    输入商店描述
driver.find_element(By.NAME,'value[103]').clear()  # 清空商店描述
time.sleep(0.5)
driver.find_element(By.NAME,'value[103]').send_keys('-5kg')  # 输入商店描述
time.sleep(0.5)
#    输入商店关键字
driver.find_element(By.NAME,'value[104]').clear()  # 清空商店关键字
time.sleep(0.5)
driver.find_element(By.NAME,'value[104]').send_keys('女装')  # 输入商店关键字
time.sleep(0.5)
#    选择所在国家
element = driver.find_element(By.NAME,'value[105]')
element.click()
time.sleep(0.5)
Select(element).select_by_value('1')
time.sleep(0.5)
#    选择所在省份
element = driver.find_element(By.NAME,'value[106]')
element.click()
time.sleep(0.5)
Select(element).select_by_value('2')
time.sleep(0.5)
#    选择所在城市
element = driver.find_element(By.NAME,'value[107]')
element.click()
time.sleep(0.5)
Select(element).select_by_value('52')
time.sleep(0.5)
#    输入详细地址
driver.find_element(By.NAME,'value[108]').clear()  # 清空详细地址
time.sleep(0.5)
driver.find_element(By.NAME,'value[108]').send_keys('天安门')  # 输入详细地址
time.sleep(0.5)
#    输入客服QQ号
driver.find_element(By.NAME,'value[109]').clear()  # 清空客服QQ号
time.sleep(0.5)
driver.find_element(By.NAME,'value[109]').send_keys('535889071')  # 输入客服QQ号
time.sleep(0.5)
#    输入淘宝旺旺
driver.find_element(By.NAME,'value[110]').clear()  # 清空淘宝旺旺
time.sleep(0.5)
driver.find_element(By.NAME,'value[110]').send_keys('535889071')  # 输入淘宝旺旺
time.sleep(0.5)
#    输入Skype
driver.find_element(By.NAME,'value[111]').clear()  # 清空Skype
time.sleep(0.5)
driver.find_element(By.NAME,'value[111]').send_keys('535889071')  # 输入Skype
time.sleep(0.5)
#    输入Yahoo Messenger
driver.find_element(By.NAME,'value[112]').clear()  # 清空Yahoo Messenger
time.sleep(0.5)
driver.find_element(By.NAME,'value[112]').send_keys('535889071')  # 输入Yahoo Messenger
time.sleep(0.5)
#    输入MSN Messenger
driver.find_element(By.NAME,'value[113]').clear()  # 清空MSN Messenger
time.sleep(0.5)
driver.find_element(By.NAME,'value[113]').send_keys('535889071')  # 输入MSN Messenger
time.sleep(0.5)
#    输入客服邮件地址
driver.find_element(By.NAME,'value[114]').clear()  # 清空客服邮件地址
time.sleep(0.5)
driver.find_element(By.NAME,'value[114]').send_keys('535889071')  # 输入客服邮件地址
time.sleep(0.5)
#    输入客服电话
driver.find_element(By.NAME,'value[115]').clear()  # 清空客服电话
time.sleep(0.5)
driver.find_element(By.NAME,'value[115]').send_keys('535889071')  # 输入客服电话
time.sleep(0.5)
#    选择是否暂时关闭网店
driver.find_element(By.ID,'value_116_0').click()  # 选择开启网站
time.sleep(0.5)
#    上传网点Logo
driver.find_element(By.NAME,'shop_logo').send_keys('D:/海德/网络拓扑图.jpg')  # 上传网点Logo
time.sleep(0.5)
#    是否显示Licensed
driver.find_element(By.NAME,'value[119]').click()  # 选择显示Licensed
time.sleep(0.5)
#    输入用户中心公告
driver.find_element(By.NAME,'value[120]').clear()  # 清空用户中心公告
time.sleep(0.5)
driver.find_element(By.NAME,'value[120]').send_keys('这里是chuuu')  # 输入用户中心公告
time.sleep(0.5)
#    输入商店公告
driver.find_element(By.NAME,'value[121]').clear()  # 清空商店公告
time.sleep(0.5)
driver.find_element(By.NAME,'value[121]').send_keys('这里是chuuu')  # 输入商店公告
time.sleep(0.5)
#    选择是否关闭注册
driver.find_element(By.ID,'value_122_1').click()  # 选择开启注册
time.sleep(0.5)
#    点击【确定】
driver.find_element(By.XPATH,'//div[@id="tabbody-div"]/form/div/input[1]').click()  # 点击【确定】
time.sleep(5)
print("商店设置成功")

# 5、退出登录
driver.switch_to.default_content()  # 跳出最外层
driver.switch_to.frame("header-frame")  # 进入顶部的header-frame
driver.find_element(By.XPATH,'//div[@id="submenu-div"]/ul/li[1]/a/img').click()  # 点击退出
time.sleep(3)
print("退出成功")

driver.quit()