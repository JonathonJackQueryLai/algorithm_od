from random import randint
li = [randint(1,10) for i in range(10)]
l = len(li)
for i in range(l):
    temp = li[i]
    temp_index = i
    if i <  l:
        for j in range(i+1,l):
            if temp > li[j]:
                temp_index = j
                temp = li[j]
        li[i],li[temp_index] = li[temp_index],li[i]
print(li)
