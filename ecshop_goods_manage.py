# 1、打开页面并访问
# 2、登录
# 3、点击【商品管理】
# 4、点击【添加新商品】
# 5、点击查看图标
# 6、点击编辑图标
# 7、点击复制图标
# 8、点击回收站图标
# 9、退出登录

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

# 3、点击【商品管理】
driver.switch_to.frame("menu-frame")  # 进入左侧的menu-frame
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[1]').click()
time.sleep(1)

# 4、点击【添加新商品】
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[1]/ul/li[2]/a').click()
time.sleep(1)
#     输入商品名称
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[1]/td[2]/input[1]').send_keys("运动鞋")
time.sleep(0.5)
#    选择字体颜色
driver.find_element(By.XPATH,'//div[@id="font_color"]/img').click()  # 定位字体颜色选择框并点击
time.sleep(0.5)
js = 'document.getElementById("goods_name_color").removeAttribute("type")'  # 删除隐藏元素type=hidden属性
driver.execute_script(js)
time.sleep(0.5)
driver.find_element(By.ID,'goods_name_color').send_keys('#FE0000')  # 输入字体颜色value
time.sleep(0.5)
#    选择字体样式
element = driver.find_element(By.NAME,'goods_name_style')
element.click()
time.sleep(0.5)
Select(element).select_by_value('strong')
time.sleep(0.5)
#    选择商品分类
element = driver.find_element(By.NAME,'cat_id')
element.click()
time.sleep(0.5)
Select(element).select_by_value('172')
time.sleep(0.5)
#    添加分类
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[3]/td[2]/a').click()  # 定位添加分类按钮并点击
time.sleep(0.5)
driver.find_element(By.XPATH,'//span[@id="category_add"]/input').send_keys('辣条7')  # 定位输入框并输入‘辣条’
time.sleep(0.5)
driver.find_element(By.XPATH,'//span[@id="category_add"]/a[1]').click()  # 定位确定按钮并点击
time.sleep(0.5)
#    添加扩展分类
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[4]/td[2]/input').click()  # 定位添加按钮并点击
time.sleep(0.5)
element = driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[4]/td[2]/select')  # 定位选择框
element.click()
time.sleep(0.5)
Select(element).select_by_value('188')  # 选择分类选项
time.sleep(0.5)
#    选择商品品牌
element = driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[5]/td[2]/select')  # 定位商品品牌选择框
element.click()
time.sleep(0.5)
Select(element).select_by_value('30')  # 选择品牌选项
time.sleep(0.5)
#    添加品牌
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[5]/td[2]/a').click()  # 点击添加品牌按钮
time.sleep(0.5)
driver.find_element(By.XPATH,'//span[@id="brand_add"]/input').send_keys('chuu4')  # 定位输入框输入‘chuu’
time.sleep(1)
driver.find_element(By.XPATH,'//span[@id="brand_add"]/a[1]').click()  # 定位确定按钮并点击
time.sleep(0.5)
#    选择供货商
element = driver.find_element(By.XPATH,'//select[@id="suppliers_id"]')  # 定位供货商选择框
element.click()
time.sleep(0.5)
Select(element).select_by_value('2')  # 选择供货商选项
time.sleep(0.5)
#    输入本店售价，按市场价计算
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[7]/td[2]/input[1]').clear()  # 清空本店售价
time.sleep(0.5)
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[7]/td[2]/input[1]').send_keys('100')  # 本店售价输入’100‘
time.sleep(0.5)
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[7]/td[2]/input[2]').click()  # 点击按市场价格计算按钮
time.sleep(0.5)
#    输入注册用户会员价格
driver.find_element(By.XPATH,'//input[@id="rank_1"]').clear()  # 清空输入框
time.sleep(0.5)
driver.find_element(By.XPATH,'//input[@id="rank_1"]').send_keys('100')  # 输入注册用户价格
time.sleep(0.5)
driver.find_element(By.XPATH,'//input[@id="rank_3"]').clear()  # 清空输入框
time.sleep(0.5)
driver.find_element(By.XPATH,'//input[@id="rank_3"]').send_keys('90')  # 输入代销用户价格
time.sleep(0.5)
driver.find_element(By.XPATH,'//input[@id="rank_2"]').clear()  # 清空输入框
time.sleep(0.5)
driver.find_element(By.XPATH,'//input[@id="rank_2"]').send_keys('90')  # 输入vip用户价格
time.sleep(0.5)
#    输入商品优惠数量、优惠价格
driver.find_element(By.XPATH,'//table[@id="tbody-volume"]/tbody/tr/td/input[1]').clear()  # 清空商品优惠数量
time.sleep(0.5)
driver.find_element(By.XPATH,'//table[@id="tbody-volume"]/tbody/tr/td/input[1]').send_keys('2')  # 输入商品优惠数量
time.sleep(0.5)
driver.find_element(By.XPATH,'//table[@id="tbody-volume"]/tbody/tr[1]/td/input[2]').clear()  # 清空商品优惠价格
time.sleep(0.5)
driver.find_element(By.XPATH,'//table[@id="tbody-volume"]/tbody/tr[1]/td/input[2]').send_keys('10')  # 输入商品优惠价格
time.sleep(0.5)
driver.find_element(By.XPATH,'//table[@id="tbody-volume"]/tbody/tr/td/a').click()  # 点击+按钮
time.sleep(0.5)
driver.find_element(By.XPATH,'//table[@id="tbody-volume"]/tbody/tr[2]/td/input[1]').send_keys('3')  # 输入商品优惠数量
time.sleep(0.5)
driver.find_element(By.XPATH,'//table[@id="tbody-volume"]/tbody/tr[2]/td/input[2]').send_keys('20')  # 输入商品优惠价格
time.sleep(0.5)
#    输入市场售价，取整数
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[10]/td[2]/input[1]').clear()  # 清空市场售价
time.sleep(0.5)
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[10]/td[2]/input[1]').send_keys('129.9')  # 输入市场售价
time.sleep(0.5)
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[10]/td[2]/input[2]').click()  # 点击取整数按钮
time.sleep(0.5)
#    输入赠送消费积分数
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[11]/td[2]/input').clear()  # 清空赠送积分数
time.sleep(0.5)
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[11]/td[2]/input').send_keys('10')  # 输入赠送积分数
time.sleep(0.5)
#    输入赠送等级积分数
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[12]/td[2]/input').clear()  # 清空赠送等级积分数
time.sleep(0.5)
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[12]/td[2]/input').send_keys('-1')  # 输入赠送等级积分数
time.sleep(0.5)
#    输入积分购买金额
js = 'document.getElementsByName("integral")[0].removeAttribute("onblur")'  # 移除元素onblur属性
driver.execute_script(js)
time.sleep(0.5)
eleje = driver.find_element(By.NAME,'integral')  # 定位元素
eleje.clear()  # 清空积分购买金额
time.sleep(0.5)
eleje.send_keys('10')  # 输入积分购买金额
time.sleep(0.5)

#    勾选促销价
driver.find_element(By.XPATH,'//input[@id="is_promote"]').click()  # 勾选促销价
time.sleep(0.5)
#    输入促销价
js = 'document.getElementById("promote_1").value=90'
driver.execute_script(js)
time.sleep(0.5)
#    输入促销日期-起始日期
js = "document.getElementById('promote_start_date').removeAttribute('readonly')"  # 移除元素readonly属性
driver.execute_script(js)
driver.find_element(By.XPATH,'//input[@id="promote_start_date"]').clear()  # 清除输入框内容
time.sleep(0.5)
driver.find_element(By.XPATH,'//input[@id="promote_start_date"]').send_keys("2020-10-10")  # 输入日期
time.sleep(0.5)
#    输入促销日期-结束日期
js = "document.getElementById('promote_end_date').removeAttribute('readonly')"  # 移除元素readonly属性
driver.execute_script(js)
driver.find_element(By.XPATH,'//input[@id="promote_end_date"]').clear()  # 清除输入框内容
time.sleep(1)
driver.find_element(By.XPATH,'//input[@id="promote_end_date"]').send_keys("2020-10-10")  # 输入日期
time.sleep(2)
#    上传商品图片
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[16]/td[2]/input[1]').send_keys('D:/海德/网络拓扑图.jpg')
time.sleep(0.5)
#    勾选自动生成商品缩略图
driver.find_element(By.XPATH,'//input[@id="auto_thumb"]').click()
time.sleep(0.5)
#    点击【确定】
driver.find_element(By.XPATH,'//div[@id="tabbody-div"]/form/div/input[2]').click()
time.sleep(5)

# 5、点击查看图标
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[11]/a[1]/img').click()  # 点击查看图标
time.sleep(3)

# 6、点击编辑图标
handles = driver.window_handles
driver.switch_to.window(handles[0])  # 切换至上一个窗口
time.sleep(3)
driver.switch_to.frame("main-frame")  # 进入"main-frame
time.sleep(1)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[11]/a[2]/img').click()  # 点击编辑图标
time.sleep(1)
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[1]/td[2]/input[1]').clear()  # 清空商品名称
time.sleep(0.5)
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[1]/td[2]/input[1]').send_keys("运动鞋-男鞋")  # 输入值
time.sleep(0.5)

# 7、点击复制图标
driver.back()  # 后退到上一个页面
time.sleep(1)   # 停留3秒
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[11]/a[3]/img').click()  # 点击复制图标
time.sleep(1)

# 8、点击回收站图标
driver.back()  # 后退到上一个页面
time.sleep(1)   # 停留3秒
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[11]/a[4]/img').click()  # 点击回收站图标
time.sleep(1)
driver.switch_to.alert.accept()  # 确定删除
time.sleep(1)

# 9、退出登录
driver.switch_to.default_content()  # 跳出最外层
driver.switch_to.frame("header-frame")  # 进入顶部的header-frame
driver.find_element(By.XPATH,'//div[@id="submenu-div"]/ul/li[1]/a/img').click()  # 点击退出
time.sleep(3)

driver.quit()
