n=int(input("enter the no: "))
n_str=str()
sum=0

for digit in n_str:
    sum=pow (int(digit,n))+sum
    print(sum)

if sum==n:
    print("{} is armsno".format(n))
else:
    print("{} is not armsno".format(n))