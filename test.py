# # from selenium import webdriver  # 引入webdriver
# # import time  # 引入时间
# #
# # from selenium.webdriver.common.keys import Keys
# #
# # driver = webdriver.Chrome()                  # 启动浏览器
# # driver.maximize_window()                     # 浏览器窗口最大化
# # url = "http://localhost/upload/"      # 浏览器地址
# # driver.get(url=url)                          #访问浏览器
# # time.sleep(2)                                #停留2秒
# #
# # driver.find_element_by_xpath('//div[@id="HandleLI2_1"]/a').click()     #点击类别“衣服”
# # time.sleep(2)                                                          #停留2秒
# # driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[3]/div/form/div/div/a/img').click()    #点击商品
# # time.sleep(2)                                                          #停留2秒
# #
# # driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[1]/div[2]/form/ul[3]/li[2]/a/img').click()        #点击立即购买
# # time.sleep(2)                                        #停留2秒
# #
# # # driver.find_element_by_xpath('//form[@id="formCart"]/table[1]/tbody/tr[2]/td[7]/a').click()
# # # time.sleep(5)
# #
# # # driver.find_element_by_name('goods_number[33]"').click()  #
# #
# # # time.sleep(2)
# # #
# # js = "document.getElementById('goods_number_33').value=3"
# # driver.execute_script(js)
# # #
# # # driver.find_element_by_xpath('//div[@id="goods_number_33"]').send_keys("2")    #增加数量
# # # time.sleep(2)
# # #
# # time.sleep(5)
# # driver.quit()
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait as wdwait
# from selenium.webdriver.common.by import By as by
# from selenium.webdriver.support.select import Select as select
# import time
# '''
# 自动化实现订单列表操作
# '''
#
# #实例化浏览器对象
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)   #设置全局的等待时间5秒，每次页面加载时自动等待
#
# #参数
# user = 'chenkang'
# pwd = 'chenkang123'
#
# url = 'http://localhost/upload/admin/'
#
# #访问后台管理
# driver.get(url = url)
#
# #登录
# driver.find_element(by.NAME, 'username').send_keys(user)#输入用户名
# driver.find_element(by.NAME, 'password').send_keys(pwd)    #输入密码
# driver.find_element(by.CLASS_NAME, 'button').click()   #点击【进入管理中心】
#
# #进入订单管理
# #切换frame
# driver.switch_to.frame('menu-frame')#进入frame
#
# driver.find_element(by.XPATH, '//ul[@id="menu-ul"]/li[3]').click() #点击【订单管理】
# driver.find_element(by.XPATH, '//ul[@id="menu-ul"]/li[3]/ul/li[1]/a').click()  #点击【订单列表】
#
# #进入订单列表
# #切换frame
# driver.switch_to.default_content()  #跳回主文档，最外层
# driver.switch_to.frame('main-frame')#进入frame
# time.sleep(1)
#
# #搜索商品-订单号
# sno = '2020071745835'
# ele_order_sn = driver.find_element(by.ID, 'order_sn')
# ele_order_sn.clear()
# ele_order_sn.send_keys(sno) #通过存在的订单号
# time.sleep(1)
# ele_search = driver.find_element(by.XPATH, '//div[@class="form-div"]/form/input[3]') #定位【搜索】
# ele_search.click()  #点击【搜索】
# time.sleep(2)
# # 搜索商品-收货人
# ele_order_sn.clear()
# ele_consignee = driver.find_element(by.ID, 'consignee')
# ele_consignee.clear()
# ele_consignee.send_keys('陈康')
# ele_search.click()  # 点击【搜索】
# time.sleep(2)
# # 搜索商品-订单状态
# ele_consignee.clear()
# ele_status = driver.find_element(by.ID, 'status')
# ele_status.click()
# sel_status = select(ele_status)
# sel_status.select_by_value("3")   #设置订单状态
# ele_search.click()  # 点击【搜索】
# time.sleep(2)
# # 搜索商品-组合查询1,2020071813521
# sno = '2020071813521'
# ele_order_sn.send_keys(sno)
# ele_consignee.send_keys("陈康")
# ele_search.click()
# time.sleep(2)
# # 搜索商品-组合查询2,2020071745835
# sno = '2020071745835'
# ele_order_sn.clear()
# ele_order_sn.send_keys(sno)
# ele_status.click()
# time.sleep(1)
# sel_status.select_by_value('101')
# time.sleep(1)
# ele_search.click()
# time.sleep(2)
#
# #查看/编辑商品-指定商品 sno ='2020071727628'
# #查询
# sno = '2020071816235'
# ele_order_sn.clear()    #清理数据
# ele_consignee.clear()
# ele_status.click()
# time.sleep(1)
# sel_status.select_by_value('0')
# ele_order_sn.send_keys(sno)
# ele_search.click()
# time.sleep(1)
#
# # 编辑 - 点击【查看】
# driver.find_element(by.XPATH, '//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[7]/a').click()  # 点击【查看】,进入到查看编辑页面
#
# #滚动
# x = 1
# height = 0
# while x:
#     js1 = 'window.scrollTo(0, %s)' % (height)
#     driver.execute_script(js1)
#     # time.sleep(1)
#     try:
#         ele_action_note = driver.find_element(by.NAME, 'action_note')  # 定位操作备注
#         ele_action_note.clear()
#         ele_action_note.send_keys('确认')  # 设置操作备注
#         driver.find_element(by.XPATH,'//form[@name="theForm"]/div[4]/table/tbody/tr[3]/td[2]/input[1]').click()  # 点击【确认】
#     except:
#         height = height + 100
#     else:
#         x = False
#         print('height',height)
#

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wdwait
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.select import Select as select
import time

'''
自动化实现订单列表操作
'''

# 实例化浏览器对象
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)  # 设置全局的等待时间5秒，每次页面加载时自动等待

# 参数
user = 'chenkang'
pwd = 'chenkang123'

url = 'http://localhost/upload/admin/'

# 访问后台管理
driver.get(url=url)

# 登录
driver.find_element(by.NAME, 'username').send_keys(user)  # 输入用户名
driver.find_element(by.NAME, 'password').send_keys(pwd)  # 输入密码
driver.find_element(by.CLASS_NAME, 'button').click()  # 点击【进入管理中心】

# 进入订单管理
# 切换frame
driver.switch_to.frame('menu-frame')  # 进入frame

driver.find_element(by.XPATH, '//ul[@id="menu-ul"]/li[3]').click()  # 点击【订单管理】
driver.find_element(by.XPATH, '//ul[@id="menu-ul"]/li[3]/ul/li[1]/a').click()  # 点击【订单列表】

# 进入订单列表
# 切换frame
driver.switch_to.default_content()  # 跳回主文档，最外层
driver.switch_to.frame('main-frame')  # 进入frame
time.sleep(1)

# 搜索商品-订单号
sno = '2020071764236'
ele_order_sn = driver.find_element(by.ID, 'order_sn')
ele_order_sn.clear()
ele_order_sn.send_keys(sno)  # 通过存在的订单号
time.sleep(1)
ele_search = driver.find_element(by.XPATH, '//div[@class="form-div"]/form/input[3]')  # 定位【搜索】
ele_search.click()  # 点击【搜索】
time.sleep(2)
# 搜索商品-收货人
ele_order_sn.clear()
ele_consignee = driver.find_element(by.ID, 'consignee')
ele_consignee.clear()
ele_consignee.send_keys('陈康')
ele_search.click()  # 点击【搜索】
time.sleep(2)
# 搜索商品-订单状态
ele_consignee.clear()
ele_status = driver.find_element(by.ID, 'status')
ele_status.click()
sel_status = select(ele_status)
sel_status.select_by_value("3")  # 设置订单状态
ele_search.click()  # 点击【搜索】
time.sleep(2)
# 搜索商品-组合查询1,2020071813521
sno = '2020071813521'
ele_order_sn.send_keys(sno)
ele_consignee.send_keys("陈康")
ele_search.click()
time.sleep(2)
# 搜索商品-组合查询2,2020071745835
sno = '2020071745835'
ele_order_sn.clear()
ele_order_sn.send_keys(sno)
ele_status.click()
time.sleep(1)
sel_status.select_by_value('101')
time.sleep(1)
ele_search.click()
time.sleep(2)

# 查看/编辑商品-指定商品 sno ='2020071701628'
# 确认-付款-配货-生成发货单-确认生成发货单-去发货-发货
# 查询
sno = '2020071818459'
ele_order_sn.clear()  # 清理数据
ele_consignee.clear()
ele_status.click()
time.sleep(1)
sel_status.select_by_value('-1')  # 将状态码设置为-1，请选择
ele_order_sn.send_keys(sno)
ele_search.click()
time.sleep(1)
# 编辑 - 点击【查看】
driver.find_element(by.XPATH, '//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[7]/a').click()  # 点击【查看】,进入到查看编辑页面

def scroll(type, url):
    '''
    滚动页面，到达指定位置，为了得到元素对象
    :param type:
    :param url:
    :return:
    '''
    x = 1
    height = 0
    ele_action_note = 0
    while x:
        js1 = 'window.scrollTo(0, %s)' % (height)
        driver.execute_script(js1)
        time.sleep(1)
        try:
            if type == 'name':
                ele_action_note = driver.find_element(by.NAME, url)  # 定位
            elif type == 'id':
                ele_action_note = driver.find_element(by.ID, url)  # 定位
            else:
                ele_action_note = driver.find_element(by.XPATH, url)
        except:
            height = height + 100
        else:
            x = False
    return ele_action_note

#确认 调用页面滚动，得到元素对象
ele_action_note = scroll('name', 'action_note')
ele_action_note.clear()
ele_action_note.send_keys('确认')  # 设置操作备注
driver.find_element(by.XPATH, '//form[@name="theForm"]/div[4]/table/tbody/tr[3]/td[2]/input[1]').click()  # 点击【确认】
print('确认成功')  # 打桩

# 付款
ele_action_note = scroll('name', 'action_note')  # 调用页面滚动，得到元素对象
ele_action_note.clear()
ele_action_note.send_keys('付款')  # 设置操作备注
driver.find_element(by.NAME, 'pay').click()  # 点击【付款】
print('付款成功')  # 打桩

# 配货name="prepare"
ele_action_note = scroll('name', 'action_note')  # 调用页面滚动，得到元素对象
ele_action_note.clear()
ele_action_note.send_keys('配货')  # 设置操作备注
driver.find_element(by.NAME, 'prepare').click()  # 点击【配货】
print('配货成功')  # 打桩

# 生成发货单
ele_action_note = scroll('name', 'action_note')  # 调用页面滚动，得到元素对象
ele_action_note.clear()
ele_action_note.send_keys('生成发货单')  # 设置操作备注
driver.find_element(by.NAME, 'ship').click()  # 点击【生成发货单】
print('生成发货单成功')  # 打桩

# 确认生成发货单name="delivery_confirmed"
ele_action_note = scroll('name', 'action_note')  # 调用页面滚动，得到元素对象
ele_action_note.clear()
ele_action_note.send_keys('确认生成发货单')  # 设置操作备注
driver.find_element(by.NAME, 'delivery_confirmed').click()  # 点击【确认生成发货单】
print('确认生成发货单成功')  # 打桩

# 去发货name="to_delivery"
ele_action_note = scroll('name', 'action_note')  # 调用页面滚动，得到元素对象
ele_action_note.clear()
ele_action_note.send_keys('去发货')  # 设置操作备注
driver.find_element(by.NAME, 'to_delivery').click()  # 点击【去发货】
print('去发货成功')  # 打桩

# #发货name="delivery_confirmed"
# ele_action_note = scroll('name', 'action_note')  # 调用页面滚动，得到元素对象
# ele_action_note.clear()
# ele_action_note.send_keys('发货')  # 设置操作备注
# driver.find_element(by.NAME, 'delivery_confirmed').click()  # 点击【发货】
# print('发货成功')  # 打桩

# 查看发货单列表的指定订单-进行发货 sno='2020071725692'
# sno = '2020071701628'
ele_order_sn = driver.find_element(by.ID, 'order_sn')
ele_order_sn.click()
ele_order_sn.send_keys(sno)
driver.find_element(by.XPATH, '/html/body/div[1]/form/input[4]').click()  # 点击【搜索】
time.sleep(1)
driver.find_element(by.XPATH, '//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[9]/a[1]').click()  # 点击【查看】
time.sleep(1)
print('点击查看')  # 打桩

# 发货name="delivery_confirmed"
ele_action_note = scroll('name', 'action_note')  # 调用页面滚动，得到元素对象
ele_action_note.clear()
ele_action_note.send_keys('发货')  # 设置操作备注
driver.find_element(by.NAME, 'delivery_confirmed').click()  # 点击【发货】
print('发货成功')  # 打桩

    # 移除商品

time.sleep(5)
driver.quit()