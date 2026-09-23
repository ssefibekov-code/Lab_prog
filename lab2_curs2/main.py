n = int(input())
q = list(map(int, input().split()))
k = int(input())

window_sum = sum(q[:k])
result = [window_sum / k]

for i in range(k, n):
    window_sum += q[i] - q[i - k]
    result.append(window_sum / k)

print(*result)