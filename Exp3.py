class Account:
    def __init__(self,branch,no,name):
        self.branch=branch
        self.no=no
        self.name=name

    def details(self):
        print("Account Name : {} , Account No : {} , Account Branch : {}".format(self.name,self.no,self.branch))
    def abc(self,no):
        if(self.no==no):
            print("Found")

class mobile_Banking(Account):
    def __init__(self,mobnum,branch,no,name):
        self.mobnum=mobnum
        Account.__init__(branch,no,name)