dict1={"Codingal":3,"is":2,"best":2,"for":2,"Coding":1}
l1=list(dict1.values())
count=0
num=int(input("Enter the number that needs to be checked for its frequency : "))
for i in l1:
    if i==num:
        count=count+1
print(num,"is repeated",count,"times")       