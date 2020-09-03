#거스름돈 문제풀이
print("거스름돈 문제풀이")
n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin
    n %= coin

print(count)

#1이 될 때까지 문제풀이
N, K = map(int, input().split())
count = 0

while True:
    if N % K == 0:
        N /= K
    else:
        N -= 1
    count += 1

    if N == 1:
        break

print(count)

#곱하기 혹은 더하기 문제풀이
data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)