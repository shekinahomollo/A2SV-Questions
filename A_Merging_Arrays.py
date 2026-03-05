import sys
input_data = sys.stdin.read().strip().split()

n = int(input_data[0])
m = int(input_data[1])

a = list(map(int, input_data[2:2+n]))
b = list(map(int, input_data[2+n:2+n+m]))

i = 0
j = 0
res = []

while i < n and j < m:
    if a[i] <= b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1  

while i < n:
    res.append(a[i])
    i += 1

while j < m:
    res.append(b[j])
    j += 1
    
print (*(res))