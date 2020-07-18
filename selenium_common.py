'''
初始化Chrome浏览器公共方法
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.action_chains import ActionChains as actionchains
#实例化话浏览器Chrome
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)

#打开页面 进入京东首页
url = 'http://www.jd.com'
driver.get(url = url)

#页面向下走一点点
# js = 'window.scrollTo(0, 900)'
# driver.execute_script(js)
# time.sleep(5)
#
# # #到页面的底部
# # #获取html页面的大小
# wh = driver.find_element(by.TAG_NAME, 'html').size
# print(wh)
# js = 'window.scrollTo(0,%s)' % (wh['height'])
# driver.execute_script(js)
#
# # #到页面的头部
# js = 'window.scrollTo(0, 0)'
# driver.execute_script(js)
# time.sleep(5)

#实现鼠标悬停
loc = driver.find_element(by.LINK_TEXT, '手机') #定位元素位置
#实例化一个actionChains对象,传入参数浏览器驱动对象
action = actionchains(driver)
action.move_to_element(loc).perform()   #实现鼠标悬停
time.sleep(3)
#选择分类下分类
driver.find_element(by.LINK_TEXT, '5G手机').click()
time.sleep(3)

#按下鼠标左键
# action.click_and_hold(loc).perform()
# time.sleep(2)

#实现鼠标拖动
# loc1 = driver.find_element(by.ID, 'key')  #定位目标路径的位置
# action.drag_and_drop(loc, loc1).perform()
# time.sleep(5)

#切换分页2

#切换到窗口
handles = driver.window_handles
driver.switch_to.window(handles[0])

#自动滚动
x = 1
height = 0
while x:
    js1 = 'window.scrollTo(0, %s)' % (height)
    driver.execute_script(js1)
    # time.sleep(1)
    try:
        ele = driver.find_element(by.XPATH, '//div[@id="J_feeds"]/div/div[1]/div/h3')
        #elelj = driver.find_element(by.XPATH, '//div[@id="J_footer"]/div[3]/div/p[2]/a[2]')
        # elelj = driver.find_element(by.XPATH, '//div[@id="J_coupon"]/div[1]/a/h3')
    except:
        height = height + 100
    else:
        x = False
        print(ele.text)
        print('height',height)

#切换到窗口
driver.switch_to.window(handles[-1])
time.sleep(1)
print(driver.title)

#实现回车搜索
searchEle = driver.find_element(by.ID, 'key')
searchEle.clear()   #清理原数据
searchEle.send_keys('牛肉干')   #设置值
searchEle.send_keys(Keys.ENTER) #按下回车
time.sleep(5)

new_window = 'window.open("http://localhost/upload/");'
driver.execute_script(new_window)
time.sleep(3)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
time.sleep(2)
driver.find_element(by.LINK_TEXT, '收藏本站').click()
time.sleep(2)
driver.switch_to.alert.dismiss()

time.sleep(5)
#退出并关闭驱动
driver.quit()