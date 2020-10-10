from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

class Graph:
    def __init__(self, V):
        self.V = V
        self.edges = defaultdict(list)
    def addEdge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)
    def dfs(self, A, visited):
        visited[A] = True
        count = 1
        for v in self.edges[A]:
            if visited[v] == False:
                count += self.dfs(v, visited)
        return count
    def solve(self, A):
        if len(self.edges[A]) == 1:
            return ("Hitland")
        visited = [False for i in range(self.V + 1)]
        nodes = [0 for i in range(self.V + 1)]
        visited[0] = True
        ans = self.dfs(A, visited)
        if (ans - 1)% 2 == 1:
            return("Hitland")
        return("Stalind")
        
        
        
T = int(input())
for t in range(T):
    N, V = list(map(int, input().split()))
    g = Graph(N)
    for n in range(N - 1):
        u, v = list(map(int, input().split()))
        g.addEdge(u, v)
    ans = g.solve(V)
    print(ans)
    
        
