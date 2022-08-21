a = int (input("digite el valor de a "))
b = int (input("digite el valor de b "))
v=0
while v <= 100:
    if a % 2 == 0 and a < 100:
        print(a,"es par")
        a = a + 2 
    else:
        if a % 2 == 1 and a < 100 : 
            print(a,"es impar")
            a = a + 2
    if b % 2 == 0 and b < 100 :
        print(b,"es par")
        b = b + 2 
    else:
        if b % 2 == 1 and b < 100 :
            print(b,"es par")
            b = b + 2 
                        
        
        