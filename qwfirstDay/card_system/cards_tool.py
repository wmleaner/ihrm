#负责各个功能函数的定义和实现
#目标功能：显示菜单 新建名片 显示全部名片 查询名片 修改名片 删除名片
card_list=[
    {'姓名':'小红','电话':'18328683122','QQ号':'2863463318','邮箱':'2863463318@qq.com'},
    {'姓名':'小红帽','电话':'1832868','QQ号':'10086','邮箱':'1832868@sina.cn'},
    {'姓名':'小红','电话':'18328683122','QQ号':'2863463318','邮箱':'2863463318@qq.com'}
]
def showmenu():
    print()
    print()
    print('*'*50)
    print('欢迎使用 [名片管理】 v1.0')
    print()
    print('1. 新建名片')
    print('2. 显示全部')
    print('3. 查询名片')
    print()
    print('0. 退出系统')
    print('*' * 50)
#新建名片     ，涉及到查询等等，最好是列表里存字典，为了方便所有函数，最好定义全局变量
def new_card():
    print('[功能]新建名片')
    username=input('请输入姓名：')
    mobileohone=input('请输入电话：')
    qq=input('请输入QQ号码：')
    email=input('请输入邮箱：')
    card={'姓名':username,'电话':mobileohone,'QQ号':qq,'邮箱':email}
    card_list.append(card)#使用append把字典作为一个整体加入列表
    print('新建姓名是：{}'.format(username)+' 名片成功')  #get取key值时一定记得''成对引号
#显示全部
def see_all():
    print('[功能]显示全部')
    '''本来已经可以了，但是当搜索不出结果时不展示表头提示没有数据更规范，所以添加判断：当不存在数据时提示'''
    if card_list==[]:
        print('这里空空的，请去新建名片哦')
    else:
        print('-'*130)
        #     n=1 本来是遍历字典的key值得，但是发现不能这么写。不然当没有名片时，表头就获取不到数据变成空了
        #     for n in i:
        #         print(' {}\t\t'.format(n),end='')
        #     print()
        print('姓名'.ljust(10),'电话'.ljust(10),'QQ号'.ljust(15),'邮箱'.center(15))#sep是打印时不同输出间的间隔符，end是想要使用的结束符
        print('-' * 130)
        #遍历card_list得到多个字典
        for m in card_list:
            print(m.get('姓名').ljust(9),m.get('电话').ljust(12),m.get('QQ号').ljust(12),m.get('邮箱').ljust(10),end='')
             # for key,vals in m.items():无法
             # print('{}'.ljust(10).format(vals),end='')
            print()

#查询名片
def search():
    print('[功能]查询名片')
    sendname=input('请输入您要查询的姓名:')
    for i in card_list:
        if i.get('姓名')==sendname:
            print('已经找到姓名是{}的人了'.format(sendname))
            print('-' * 130)
            print('姓名'.ljust(10), '电话'.ljust(10), 'QQ号'.ljust(15), '邮箱'.center(10))  # sep是打印时不同输出间的间隔符，end是想要使用的结束符
            print('-' * 130)
            print(i.get('姓名').ljust(9),i.get('电话').ljust(12),i.get('QQ号').ljust(9),i.get('邮箱').ljust(15))
            print('-' * 130)
            return
    else:
            print("没有找到该名字的信息")


#退出系统
def exit():
    print('退出系统')