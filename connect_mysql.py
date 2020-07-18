#mysql连接，数据操作
#pip install PyMySQL #下载pymysql库
import pymysql  #引入mysql包
def getUsers():
    config = {  #组装一个数据库连接的字典
        'host' : 'localhost',   #数据库服务器地址
        'port' : 3306,  #端口，mysql一般默认3306，修改过的查询后连接
        'user' : 'root',    #数据库用户名
        'db' : 'ecshop',  #数据库名称
        'charset' : 'utf8', #数据库编码，不设置可能中文乱码
        'cursorclass' : pymysql.cursors.DictCursor #以字典的方式返回结果
    }
    db = pymysql.connect(**config)  #传入组装的字典
    cur = db.cursor()   #创建一个游标对象
    sql = "select * from ecs_users where user_name != 'chenkangkang'"    #组装sql语句
    cur.execute(sql)    #执行sql
    data = cur.fetchall()   #fetchall()获取所有数据
    names = []
    emails = []
    for var in data:
        names.append(var['user_name'])
        emails.append(var['email'])
    db.close()    #关闭数据库连
    return names,emails