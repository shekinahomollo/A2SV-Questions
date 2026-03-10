import sys
input_data = sys.stdin.read().strip().split()

n = int(input_data[0])
s = int(input_data[1])

a = list(map(int, input_data[2:2+n]))
l = 0
sum = 0
count = 0

for r in range(n):
    sum += a[r]
    while sum > s:
        sum -= a[l]
        l += 1
    count = max(count, r-l+1)
print (count)