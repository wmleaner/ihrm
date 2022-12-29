
def print99():
    i = 0
    while i<9:
        i += 1
        j = 1
        while j<=i:#一层控制一层的，定义需要在第一层循环定义
            print("%d * %d= %d\t"%(i,j,i*j),end='')
            j+=1
        print()
def print123():
    print(123)
x=[1,12.3,'啥子',(1,23)]