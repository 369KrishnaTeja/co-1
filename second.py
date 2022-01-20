#Task 4 : Create a train list with following keys train ID, train name,
# train type, source, destination, create 5 train objects and apply
# following operations: search based on train type and display all
# the trains, search source and train type, update a specific Train
# for a specific key, create a new key for the trains as number of
# passengers, delete a specific key from the trains, Hint : use if
# and for loops and methods of dictionary

train={
"t_id":{"6754","4567","8901","8921","8971"},
"name":["LL","GG","TT","BB","OO"],
"ttype":["Fast","SuperFast","Luxary","Fast","Slow"],
"Source":["Tirupati","Madhurai","Mumbai","Hyd","chennai"],
"Destination":["Vizag","Hyd","Karnataka","Mumbai","delhi"]
}

for k,v in train.items():
    for j in range(len(train)):
        if(k=="name"):
            v=train.get(k)
            print(v[j])
        if (k == "ttype"):
            v = train.get(k)
            print(v[j])
        if (k == "Source"):
            v = train.get(k)
            print(v[j])
        if (k == "Destination"):
            v = train.get(k)
            print(v[j])