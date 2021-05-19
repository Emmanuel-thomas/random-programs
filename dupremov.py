# 1. write a program to remove duplicate items from a list
ls = [5, 5, 5, 3, 4, 6, 5]
ms = []
print(len(ls) - 1)
for i in ls:
    if i not in ms:
        ms.append(i)
print(ms)
