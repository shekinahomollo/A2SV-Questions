import sys

input_data = sys.stdin.read().split()

ptr = 0
t = int(input_data[ptr])
ptr += 1
for _ in range(t):
    n = int(input_data[ptr])
    ptr += 1
    a = sorted(int(input_data[ptr + i]) for i in range(n))
    ptr += n

    if all(a[i + 1] - a[i] <= 1 for i in range(n - 1)):
        print("YES")
    else:
        print("NO")