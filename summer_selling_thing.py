n, f = map(int, input().split())
days = []
for i in range(n):
    k, l = map(int, input().split())
    days.append((k, l))
 
days.sort(key=lambda x: min(x[0], x[1]), reverse=True)
 
ans = 0
for i in range(n):
    if i < f:
        ans += min(days[i][0]*2, days[i][1])
    else:
        ans += min(days[i][0], days[i][1])
print(ans)
