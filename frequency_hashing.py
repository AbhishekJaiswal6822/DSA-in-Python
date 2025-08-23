# n=[5,3,2,2,1,5,5,7,5,10]
# m=[10,111,1,9,5,67,2]

# hash_list=[0]*11

# for num in n:
#     hash_list[num]+=1
# for num in m:
#     if num < 1 or num > 10:
#         print(f"{num} : 0")
#     else:
#         print(f"{num} : {hash_list[num]}")

# Dictionary
# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]

# hash_map = dict()

# for num in n:
#     hash_map[num] = hash_map.get(num, 0) + 1


# for num in m:
#     print(f"{num} : {hash_map.get(num, 0)}")

# character hashing
s="azyxyyzaaaa"
q=["d","a","y","z"]
hash_list=[0]*26

for ch in  s:
    ascii_val=ord(ch)
    index= ascii_val-97
    hash_list[index]+=1
for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(f"{ch} : {hash_list[index]}")


