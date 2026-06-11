n = int(input(""))
l = [n]
while n != 1:
    if (n%2 == 0):
        n = int(n/2)
    else:
        n = int((n*3)+1)
    l.append(n)
for x in l:
    print(x, end=' ')