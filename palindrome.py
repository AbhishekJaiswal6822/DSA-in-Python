num= 11
orignal = num
result = 0

while num> 0:
    ld= num%10
    result= (result*10)+ld
    num = num//10
if result == orignal:
    print("palidrome")
else:
    print ("not a plaindrome")