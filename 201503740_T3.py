from ast import Return
from cmath import sqrt   
    

opcion = 0
while True:
    try:
        print("""
        Elige la operacion que quieras realizar
        
        1) Sumar 
        2) Restar 
        3) Multiplicar
        4) Dividir
        5) potencia
        6) Raiz
        7) Apagar calculadora
        """)

        opcion = int(input("Elige una opción: ") )     

        if opcion == 1:
            print(" ")
            try:
                n1 = float(input("Introduce tu primer número: "))
                n2 = float(input("Introduce tu segundo número: "))

                print("""********************************************************************
                RESULTADO: La suma de""",n1,"+",n2,"es igual a",n1+n2)
                print("********************************************************************")

            except ValueError as ERROR:
                    print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero<<<<<<<< \n ")
                    print (ERROR)
                    print ("\n --------INTENTE DE NUEVO--------")
                    Return

                
        elif opcion == 2:
            print(" ")
            try:
                n1 = float(input("Introduce tu primer número: "))
                n2 = float(input("Introduce tu segundo número: "))

                print("""********************************************************************
                RESULTADO: La resta de""",n1,"-",n2,"es igual a",n1-n2)
                print("********************************************************************")

            except ValueError as ERROR:
                    print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero<<<<<<<< \n ")
                    print (ERROR)
                    print ("\n --------INTENTE DE NUEVO--------")
                    Return


        elif opcion == 3:
            print(" ")
            try:
                n1 = float(input("Introduce tu primer número: "))
                n2 = float(input("Introduce tu segundo número: "))

                print("""********************************************************************
                RESULTADO: El producto de""",n1,"*",n2,"es igual a",n1*n2)
                print("********************************************************************")

            except ValueError as ERROR:
                    print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero<<<<<<<< \n ")
                    print (ERROR)
                    print ("\n --------INTENTE DE NUEVO--------")
                    Return


        elif opcion == 4:
            print(" ")
            try:
                n1 = float(input("Introduce tu primer número: "))
                n2 = float(input("Introduce tu segundo número: "))

                print("""********************************************************************
                RESULTADO: El producto de""",n1,"/",n2,"es igual a",n1/n2)
                print("********************************************************************")

            except ValueError as ERROR:
                    print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero<<<<<<<< \n ")
                    print (ERROR)
                    print ("\n --------INTENTE DE NUEVO--------")
                    Return
    
            except ZeroDivisionError as ERROR:
                    print ("\n >>>>>>>>>toda division de un numero entre cero (0) su resultado sera indefinido<<<<<<<< \n ")
                    print (ERROR)
                    print ("\n --------INTENTE DE NUEVO--------")
                    Return


        elif opcion == 5:
            print("\n----- X^n-----\n")
            try:
                n1 = float(input("Introduce el valor de X: "))
                n2 = float(input("Introduce el valor de n: "))

                print("""********************************************************************
                RESULTADO: La potencia de""",n1,"^",n2,"es igual a",n1**n2)
                print("********************************************************************")

            except ValueError as ERROR:
                    print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero<<<<<<<< \n ")
                    print (ERROR)
                    print ("\n --------INTENTE DE NUEVO--------")
                    Return


        elif opcion == 6:
            print("\n ----- x √ (y) -----\n")
            try:
                n1 = float(input("Introduce el valor de indice X : "))
                n2 = float(input("Introduce el valor del radicando Y: "))

                print("""********************************************************************
                RESULTADO: La raiz""",n1,"√",n2,"es igual a",n2**(1/n1))
                print("********************************************************************")  

            except ValueError as ERROR:
                    print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero<<<<<<<< \n ")
                    print (ERROR)
                    print ("\n --------INTENTE DE NUEVO--------")
                    Return


        elif opcion == 7:
            break
        else:
            try:
                print("Opción incorrecta")
                
            except ValueError as ERROR:
                    print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero<<<<<<<< \n ")
                    print (ERROR)
                    print ("\n --------INTENTE DE NUEVO--------")
                    Return

    except ValueError as ERROR:
                print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero del menu<<<<<<<< \n ")
                print (ERROR)
                print ("\n --------INTENTE DE NUEVO--------")
                Return
        