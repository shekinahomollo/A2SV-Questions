#User function Template for python3
from collections import Counter

class Solution:
    #Function to check if a is a subset of b.

    
    def isSubset(self, a, b):
        count_a = Counter(a)
        count_b = Counter(b)
    
        for elem in count_b:
            if count_b[elem] > count_a[elem]:
                return False
        return True
        # Your code here
 