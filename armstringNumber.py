num= 153
original = num

nod = (len(str(num)))
total =0

while num > 0:
    ld = num % 10
    total = total + (ld ** nod)
    num = num // 10
if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

