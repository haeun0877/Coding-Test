DFS : 깊이 웃선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
---
###   DFS는 스택사용
BFS : 너비 우선 탐색이라고도 부르며, 가까운 노드부터 탐색하는 알고리즘
---
###   BFS는 큐사용
>스택 : 선입후출 구조 또는 후입선출 구조
  삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
  ```
  stack.append(5)
  stack.append(2)
  stack.append(3)
  stack.append(7)
  stack.pop()
  stack.append(1)
  stack.append(4)
  stack.pop()
  
  print(stack)
  ```
  출력결과 : [5, 2, 3, 1]
>큐 : 선입선출 구조
  삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
  ```
  from collections import deque
  
  queue = deque()
  
  queue.append(5)
  queue.append(2)
  queue.append(3)
  queue.append(7)
  queue.popleft()
  queue.append(1)
  queue.append(4)
  queue.popleft()
  
  print(queue)
  ```
  출력결과 : deque([3, 7, 1, 4])
  

#DFS 소스코드 예제
```
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

graph=[
  [],
  [2, 3, 8],
  [1, 7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9

dfs(graph, 1, visited)
```

#BFS 소스코드 예제
```
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)
```

#음료수 얼려 먹기 문제 풀이
######(DFS혹은 BFS로 풀이 가능)
```
def dfs(x, y):
  if x <=-1 or x>=n or y<=-1 or y>=m:
      return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x-1, y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

n, m = map(int, input().split())

graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result +=1

print(result)
```

#미로 탈출 문제 풀이
######(bfs에서는 list를 사용하면 시간초과판정가능성있음, 보통 deque를 씀)
```
from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x,y))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))
  return graph[n-1][m-1]

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))
```
