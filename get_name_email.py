'''
自动生成用户名和email
'''
import connect_mysql as mysql
#调用数据库查询，得到用户名list
#用户名存在，更换用户名
def getUsername():
    usernames,_ = mysql.getUsers()
    username = max(usernames)
    num = username[8:]
    num = int(num)
    num = num+1
    username = username[0:8]+str(num)
    return username

#email
def getEmail():
    _, emails = mysql.getUsers()
    email = max(emails)
    index = email.index('@')
    num = email[0:index]
    num = int(num)
    num = num+1
    email = str(num)+email[index:]
    return email