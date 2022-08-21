d=int(input("digite el dia "))
m=int(input("digite el mes "))
a=int(input("digite el año "))
while a <= 1 :
    
    if d < 28 :
        d = d + 1
        print(d,"/",m,"/",a)
    elif d > 28 and d <31:
        d = d + 1
        print(d,"/",m,"/",a)
    else:
        if d > 30 :
            d=1
            m=m+1
            print(d,"/",m,"/",a)
        else:
            if m > 12:
                m = 1
                a=a+1
                print(d,"/",m,"/",a)
# if d > 30 :
#     d=1
#     m=m+1
#     print(d,"/",m,"/",a)
# else:
#     if m > 12:
#         a=a+1
#         print(d,"/",m,"/",a)
# if m > 12:
#     a=a+1
#     print(d,"/",m,"/",a)