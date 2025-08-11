l = list(map(int, input().split()))
t = int(input())

s = dict()
tmp = None
for x in l:
    if (t - x) in s:
        tmp = [x, t-x]
        break
    s.add(x)

if not tmp:
    print(-1)
for i in range(len(l)):
    if l[i] == tmp[0]:
        tmp[0] = i
    elif l[i] == tmp[1]:
        tmp[1] = i

print(f"tmp[0] tmp[1]")