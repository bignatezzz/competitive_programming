
 t = int(input())
while t>0:
    t-=1
    a = input()
    x = int(a[0])
    y=int(a[2])
    print(x, end ="")
    if x == y:
        print('=', end = "")
    elif x>y:
        print('>', end = "")
    else:
        print('<', end ="")
        
    print(y)
