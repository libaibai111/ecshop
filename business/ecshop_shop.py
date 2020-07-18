'''
自动化-ecshop购物流程验证
'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.select import Select as select
import business.ecshop_common_get as gne

def shop():
    #实例化浏览器对象
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(3)

    #参数
    username = gne.getUsername() #自动生成用户名和email
    email = gne.getEmail()

    pwd = 'chenkang123'
    cpwd = 'chenkang123'
    msn = '123456@hotmail.com'
    qq = '411052590'
    call1 = '2558888888'
    call2 = '255999999'
    phone = '15885537820'
    wt = '我的座右铭是？'
    da = '哈哈哈'
    xy = ''
    search = '毛'
    country = '中国'
    province = '四川'
    city = '成都'
    district = '锦江区'
    shname = '陈康'
    address = '东方广场C座'

    url = 'http://localhost/upload/user.php?act=register'
    #进入注册页面
    driver.get(url = url)
    time.sleep(2)

    #开始注册
    driver.find_element(by.ID, 'username').send_keys(username)  #用户名
    driver.find_element(by.ID, 'email').send_keys(email) #email
    driver.find_element(by.ID, 'password1').send_keys(pwd)  #密码
    driver.find_element(by.ID, 'conform_password').send_keys(cpwd)  #确认密码
    driver.find_element(by.NAME, 'extend_field1').send_keys(msn)   #MSN
    driver.find_element(by.NAME, 'extend_field2').send_keys(qq) #qq
    driver.find_element(by.NAME, 'extend_field3').send_keys(call1) #办公电话
    driver.find_element(by.NAME, 'extend_field4').send_keys(call2) #家庭电话
    driver.find_element(by.NAME, 'extend_field5').send_keys(phone) #家庭电话
    elem = driver.find_element(by.NAME, 'sel_question') #定位下拉框
    sel = select(elem)  #实例化下拉框对象
    sel.select_by_visible_text(wt)  #设置问题
    driver.find_element(by.NAME, 'passwd_answer').send_keys(da) #密码问题答案
    # driver.find_element(by.NAME, 'agreement').send_keys('1')    #勾选协议？？？
    driver.find_element(by.CLASS_NAME, 'us_Submit_reg').click() #点击会员注册按钮
    time.sleep(5)

    #退出//*[@id="ECS_MEMBERZONE"]/a[2]
    driver.find_element(by.XPATH, '//font[@id="ECS_MEMBERZONE"]/a[2]').click()  #点击退出按钮
    time.sleep(5)

    #登录
    driver.find_element(by.XPATH, '//font[@id="ECS_MEMBERZONE"]/a[1]').click() #点击右上角登录按钮
    time.sleep(3)
    driver.find_element(by.NAME, 'username').send_keys(username)    #输入登录用户名
    driver.find_element(by.NAME, 'password').send_keys(pwd)    #输入登录密码
    driver.find_element(by.CLASS_NAME, 'us_Submit').click() #点击立即登陆按钮
    time.sleep(5)

    #搜索商品
    driver.find_element(by.ID, 'keyword').send_keys(search) #设置搜索条件
    driver.find_element(by.CLASS_NAME, 'fm_hd_btm_shbx_bttn').click()   #点击搜索按钮
    time.sleep(3)

    #选择商品
    driver.find_element(by.XPATH, '//form[@id="compareForm"]/div/div[2]').click()   #选择并点击商品
    time.sleep(3)

    #加入购物车
    driver.find_element(by.XPATH, '//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img').click() #点击立即购买
    time.sleep(2)

    #进入结算中心
    driver.find_element(by.XPATH, '/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img').click() #进入结算中心
    time.sleep(2)

    try:
        #填写收货地址
        ctr = driver.find_element(by.NAME, 'country')
    except:
        print('已经设置了收货地址')
    else:
        selc = select(ctr)
        selc.select_by_visible_text(country)    #设置国家
        prc = driver.find_element(by.NAME, 'province')
        selp = select(prc)
        selp.select_by_visible_text(province)    #设置省份
        ct = driver.find_element(by.NAME, 'city')
        selct = select(ct)
        selct.select_by_visible_text(city)    #设置城市
        dist = driver.find_element(by.NAME, 'district')
        seldst = select(dist)
        seldst.select_by_visible_text(district)    #设置区
        driver.find_element(by.NAME, 'consignee').send_keys(shname) #设置收货人
        driver.find_element(by.NAME, 'address').send_keys(address) #设置详细地址
        driver.find_element(by.NAME, 'tel').send_keys(phone) #设置电话
        driver.find_element(by.NAME, 'Submit').click()  #保存配送地址，点击【配送至这个地址】
    time.sleep(3)

    #确认订单
    driver.find_element(by.NAME, 'shipping').click()    #选择配送方式
    driver.find_element(by.NAME, 'payment').click()    #选择支付方式
    driver.find_element(by.XPATH, '//form[@id="theForm"]/div[11]/div[2]/input[1]').click()   #提交订单
    time.sleep(3)

    #结算/html/body/div[7]/div/table/tbody/tr[3]/td/div/input
    driver.find_element(by.XPATH, '/html/body/div[7]/div/table/tbody/tr[3]/td/div/input').click()   #点击【立即使用支付宝支付】
    time.sleep(2)

    #切换窗口
    handles = driver.window_handles
    driver.switch_to.window(handles[0])
    time.sleep(2)

    #退出系统
    driver.find_element(by.XPATH, '//font[@id="ECS_MEMBERZONE"]/a[2]').click()  #点击退出按钮
    time.sleep(5)

    #关闭页面并退出驱动
    time.sleep(3)
    driver.quit()
