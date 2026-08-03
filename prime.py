num=int(input("Enter a number"))
count=0
for i in range(2,num-1):
    if(num%i)==0:
        count+=1
if count < 2:
    print("It is a prime")
else:
    print("It is not a prime")