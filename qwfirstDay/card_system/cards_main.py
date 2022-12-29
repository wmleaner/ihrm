#当前文件cards_main负责调用，不负责功能----------总控中心
import cards_tool
#添加死循环让其重复显示
while True:
    cards_tool.showmenu()
    op=input('请输入你的选择:')#不能int，因为万一用户手贱输入字符串，就运行不了崩溃了
    cd=['1','2','3']
    if op in cd:
        if op=='1':
           cards_tool.new_card()
        elif op=='2':
            cards_tool.see_all()
        else:
            cards_tool.search()
    elif op=='0':
        print('即将退出系统')
        break
    else:
        print('输入的参数有误，请重新输入')