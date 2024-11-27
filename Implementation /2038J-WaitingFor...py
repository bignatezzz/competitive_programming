t = int(input())
current_p = 0
while t>0:
    t-=1
    a = input()
    if a[0] == 'P':
        current_p = current_p + int(a[2:])
        
    else:
        seats = int(a[2:])
        if seats>current_p:
            current_p = 0
            print("YES")
        else:
            current_p = current_p - seats
            print("NO")
