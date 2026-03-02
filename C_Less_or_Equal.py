import sys

input_data = sys.stdin.read().split()

n = int(input_data[0])
k = int(input_data[1])
a = sorted(int(x) for x in input_data[2:])

if k==0:
    result = a[0]-1
    print(result if result >= 1 else -1)
elif k==n:
    print(a[k-1])
else:
    if a[k-1] == a[k]:
        print("-1")
    else:
        print(a[k-1])