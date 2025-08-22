# num = 20

# factors=[]

# for i in range (1,(num//2)+1):
#     if num%i==0:
#         factors.append(i)
# print (factors)
from math import sqrt
num=36
result = []
for i in range (1,int(sqrt(num))+1):
    if num%i==0:
        result.append(i)
        if num//i !=i:
            result.append(num//i)
print(sorted(result))