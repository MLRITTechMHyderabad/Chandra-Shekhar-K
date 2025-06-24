'''# Read input
m = int(input())
M = set(map(int, input().split()))

n = int(input())
N = set(map(int, input().split()))

# Symmetric difference
result = M.symmetric_difference(N)

# Print in ascending order
for num in sorted(result):
    print(num)
'''

m = int(input())
M = set(map(int, input().split()))

n = int(input())
N = set(map(int, input().split()))

# Symmetric difference = (M union N) - (M intersection N)
result = (M | N) - (M & N)


for num in sorted(result):
    print(num)