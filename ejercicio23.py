a = int (input("digite el valor de a "))
b = int (input("digite el valor de b "))
opcion = input("seleccione la operacion ")
def division(a , b ):
    resultado = a / b
    return resultado      

if (opcion == "1") :
    print(division(a , b),"division")
    


def multiplicacion(a ,b):
    resultado = a * b
    return resultado      

if (opcion == "2"): 
    print(multiplicacion(a , b),"multiplicacion")
    

def suma (a, b):
    resultado = a + b
    return resultado    

if (opcion == "3"): 
    print(suma (a , b),"suma")
    


def resta (a , b):
  
     resultado= a - b
     return resultado     
 
if (opcion == "4"): 
    print(resta(a ,b), "resta")