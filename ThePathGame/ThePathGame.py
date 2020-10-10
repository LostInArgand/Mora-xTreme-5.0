from collections import defaultdict
import sys
sys.setrecursionlimit(100000000)

def dfs(u):
    global minPath
    if u > len(arr):
        return False
    if u == len(arr):
        return True
    if arr[u] == '1':
        return False
    if u == len(arr) - 1:
        return True
    try:
        return mem[u]
    except:
        val = False
        for i in range(k, 0, -1):
            # if u + i >= len(arr):
            #     return val
            val = dfs(u + i)
            if val == True:
                minPath.append(i)
                mem[u] = val
                return val
        if arr[u] == '0':
            mem[u] = val
            return val
        mem[u] = False
        return False

def solve(arr):
    global minPath
    if arr[0] == 1 or arr[-1] == 1:
        return None
    arr.reverse()
    dfs(0)
    if len(minPath) == 0:
        return None
    minPath[0] = N - (sum(minPath) - minPath[0])
    if minPath[0] == 0:
        del minPath[0]
    minPath = [str(ele) for ele in minPath]
    

N, k = list(map(int, input().split()))

arr = list(input().rstrip())
if k == 1 and ('1' not in arr):
    temp = ['1' for i in range(N)]
    print(' '.join(temp))
    exit()
mem = defaultdict()
minPath = []
solve(arr)
if len(minPath) == 0:
    print(-1)
else:
    print(' '.join(minPath))
