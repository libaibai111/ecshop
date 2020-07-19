'''
批量生成订单-新用户
'''
import business.ecshop_shop as order

amount = input('请输入要生成的订单数：')
amount = int(amount)
for batch in range(1,amount):
    order.shop()
print('生成完了')