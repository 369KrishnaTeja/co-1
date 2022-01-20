class TimeTable:
    count=0
    def __init__(self,fname,sub,day,hour):
        self.fname=fname
        self.sub=sub
        self.day=day
        self.hour=hour
    def search(self,sub):
        if(self.sub==sub):
            return self.sub,self.hour,self.day,self.fname
    def search2(self,hour):
        if(self.hour==hour):
            return self.sub,self.hour,self.day,self.fname
    def search3(self,day):
        if(self.day==day):
            return self.sub,self.hour,self.day,self.fname
    def print1(self):
        print("{}".format(self.fname))
        print("{}".format(self.day))
        print("{}".format(self.hour))
        print("{}".format(self.sub))
    @classmethod
    def obj1(cls,abc):
        fname,sub,day,hour=abc.split('-')
        return cls(fname,sub,day,hour)
    @classmethod
    def count1(cls):
            cls.count=cls.count+1
x=TimeTable("Krishna","OSD","Monday","2")
x.print1()
x.count1()
print(x.search("OSD"))
y=TimeTable.obj1('krishna-DBMS-Tuesday-3')
y.print1()
y.count1()
print(y.count)
print(y.search2("3"))
print(y.search3("Monday"))