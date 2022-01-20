list1={
    "Krishna":["Ravi","Gopi"],
    "Teja":["Surya","Mohan"],
    "Rohit":["Upendra","Ram","Nandhu"]
}
n=input("Enter faculty name to know no of students routed : ")
c=0
for i in list1:
    if(i==n):
        print("No of students routed are : {0}".format(len(list1.get(i))))
        break
    c=c+1
if(c==len(list1)):
    print("Not Found")