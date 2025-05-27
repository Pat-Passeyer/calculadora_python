import calculadora

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo número: "))
def menu():
    while True:
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print(calculadora.sumar(a,b))
        elif opcion == "2":
            print(calculadora.restar(a,b))
        elif opcion == "3":
            print(calculadora.multiplicar(a,b))
        elif opcion == "4":
            print(calculadora.dividir(a,b))
        elif opcion == "5":
            break
        else: 
            print("Ingrese una opción válida.")

menu()          