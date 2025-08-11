l = input().split()
t = input()

s = dict()
t = None
for x in l:
    if (t - x) in s:
        t = [x, t-x]
        break
    s.add(x)

if not t:
    print(-1)
for i in range(len(l)):
    if l[i] == t[0]:
        t[0] = i
    elif l[i] == t[1]:
        t[1] = i

print(f"t[0] t[1]")