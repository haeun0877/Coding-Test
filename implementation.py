#시각 문제 풀이
h = int(input())

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count+=1

print(count)

#상하좌우 문제 풀이
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_type=['L','R','U','D']

for plan in plans:
  for i in range(len(move_type)):
    if plan == move_type[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx <1 or ny<1 or nx>n or ny>n:
    continue
  x, y = nx, ny

print(x, y)

#문자열 재정렬 문제 풀이
inNum = input()
array = []
sum=0

for i in inNum:
  if i.isalpha():
    array.append(i)
  else:
    sum+=int(i)

array.sort()
array.append(str(sum))

print(''.join(array))
