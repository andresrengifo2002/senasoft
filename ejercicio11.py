i=int(input("digite un numero de i "))
e=int(input("digite un numero de e "))
r=int(input("digite un numero de r "))

if i > 10 or e > 10 or r > 10 :
     print("es mayor ")
if i < 8 and i > 3  or e < 8 and e >3 or r < 8  and r > 3 :
     print("este es el central ")
if i < 3 or e < 3 or r < 3 :
     print(" es menor ")