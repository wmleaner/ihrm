# 小明爱跑步，体现封装特性
class Person:
    def __init__(self,name,weigh):
        self.name=name
        self.weigh=weigh
        self.runcount=0
        self.eatcount=0
    def __str__(self):
        return '-------------我是%s，体重%0.2f-----------'%(self.name,self.weigh)
    def run(self):
        self.runcount+=1
        self.weigh-=0.5
        print('%s爱跑步，跑了%s次，体重减了%0.2f，目前体重%0.2f' % (self.name, self.runcount,0.5*self.runcount,self.weigh))
    def eat(self):
        self.weigh+=1

        self.eatcount+=1
        print('%s爱吃饭，吃了%s次，体重增加了%0.2f，目前体重%0.2f' % (self.name, self.eatcount,self.eatcount, self.weigh))

xiaoming=Person('小明',70.0)
print(xiaoming)

xiaoming.run()
print(xiaoming)

xiaoming.eat()
print(xiaoming)
