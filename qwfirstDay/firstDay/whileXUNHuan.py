'''
i=1
while i<=5:
    j=1
    while j<=5:
        print('*  ',end='')
        j+=1
    print()
    i+=1
打印正方形
'''

#打印三角形

i=1  #控制行数
while i<=9:
    j=1  #控制列数
    while j<=i:
        print('%d * %d= %d\t'%(i,j,i*j),end='')
        '''制表符，协助在输出文本时，垂直方向保持对齐'''
        j+=1
    print()
    i+=1