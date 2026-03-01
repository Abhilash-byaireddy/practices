#
n=[1,4,2,2,2]
k=2
for i in n:
    if i == k:
        n.remove(i)
print(len(n)-1)
