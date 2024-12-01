import os
import time
import math


def cambiar_color(texto, fondo):
    """
    Cambia los colores de texto y fondo de la consola.
    Solo funciona en Windows.
    """
    os.system(f'color {fondo:X}{texto:X}')


def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')


def imprimir_titulo(titulo):
    """Imprime un título con formato."""
    print("*******************************************")
    print(f"             {titulo}")
    print("*******************************************")


def validar_contrasena():
    """Valida una contraseña con un máximo de 3 intentos."""
    contrasena_correcta = "170522"
    intentos = 3

    while intentos > 0:
        limpiar_pantalla()
        cambiar_color(15, 4)
        imprimir_titulo("SISTEMA PROTEGIDO POR CLAVE")
        print("\t\nALEXIS VILLEGAS ALVARADO\n\n")
        entrada = input("Ingrese la CLAVE: ")

        if entrada == contrasena_correcta:
            return True
        else:
            intentos -= 1
            print(f"\nContraseña incorrecta. Intentos restantes: {intentos}")
            time.sleep(1.5)

    return False


def conversion_angulos():
    """Realiza conversiones entre ángulos."""
    limpiar_pantalla()
    cambiar_color(15, 3)
    imprimir_titulo("\n\n\tCONVERSIONES DE ANGULOS")
    print("1. Centesimal a Radian")
    print("2. Centesimal a Sexagesimal")
    print("3. Sexagesimal a Centesimal")
    print("4. Sexagesimal a Radian")
    print("5. Radian a Centesimal")
    print("6. Radian a Sexagesimal")
    print("\n\n\t7. Volver al menú principal")

    opcion = int(input("\nSeleccione una opción: "))
    if opcion == 7:
        return

    angulo = float(input("\nIngrese el ángulo: "))
    resultado = 0

    if opcion == 1:
        resultado = angulo * math.pi / 200
    elif opcion == 2:
        resultado = angulo * 9 / 10
    elif opcion == 3:
        resultado = angulo * 10 / 9
    elif opcion == 4:
        resultado = angulo * math.pi / 180
    elif opcion == 5:
        resultado = angulo * 200 / math.pi
    elif opcion == 6:
        resultado = angulo * 180 / math.pi
    else:
        print("Opción no válida.")
        time.sleep(1)
        return

    print(f"Resultado: {resultado:.6f}")
    input("Presione Enter para continuar...")


def elegir_operacion():
    """Permite elegir entre calcular área o perímetro."""
    print("\n¿Qué desea calcular?")
    print("1. Área")
    print("2. Perímetro")
    return int(input("Seleccione una opción: "))


def area_perimetro_cuadrado():
    """Calcula el área o perímetro de un cuadrado."""
    limpiar_pantalla()
    cambiar_color(15, 2)
    imprimir_titulo("CUADRADO")
    lado = float(input("Ingrese el lado del cuadrado: "))

    if lado > 0:
        opcion = elegir_operacion()
        if opcion == 1:
            print(f"\nÁrea: {lado * lado:.2f} unidades cuadradas")
        elif opcion == 2:
            print(f"\nPerímetro: {lado * 4:.2f} unidades")
        else:
            print("Opción no válida.")
    else:
        print("Entrada inválida. El lado debe ser mayor a 0.")
    input("Presione Enter para continuar...")


def area_perimetro_triangulo():
    """Calcula el área o perímetro de un triángulo."""
    limpiar_pantalla()
    cambiar_color(15, 5)
    imprimir_titulo("TRIÁNGULO")
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    lado1 = float(input("Ingrese el primer lado del triángulo: "))
    lado2 = float(input("Ingrese el segundo lado del triángulo: "))

    if base > 0 and altura > 0 and lado1 > 0 and lado2 > 0:
        opcion = elegir_operacion()
        if opcion == 1:
            print(f"\nÁrea: {(base * altura) / 2:.2f} unidades cuadradas")
        elif opcion == 2:
            print(f"\nPerímetro: {base + lado1 + lado2:.2f} unidades")
        else:
            print("Opción no válida.")
    else:
        print("Entrada inválida. Todos los valores deben ser mayores a 0.")
    input("Presione Enter para continuar...")


def area_perimetro_trapecio():
    """Calcula el área o perímetro de un trapecio."""
    limpiar_pantalla()
    cambiar_color(15, 6)
    imprimir_titulo("TRAPECIO")
    base_mayor = float(input("Ingrese la base mayor del trapecio: "))
    base_menor = float(input("Ingrese la base menor del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    lado1 = float(input("Ingrese el primer lado del trapecio: "))
    lado2 = float(input("Ingrese el segundo lado del trapecio: "))

    if base_mayor > 0 and base_menor > 0 and altura > 0 and lado1 > 0 and lado2 > 0:
        opcion = elegir_operacion()
        if opcion == 1:
            print(f"\nÁrea: {((base_mayor + base_menor) * altura) / 2:.2f} unidades cuadradas")
        elif opcion == 2:
            print(f"\nPerímetro: {base_mayor + base_menor + lado1 + lado2:.2f} unidades")
        else:
            print("Opción no válida.")
    else:
        print("Entrada inválida. Todos los valores deben ser mayores a 0.")
    input("Presione Enter para continuar...")


def area_perimetro_circulo():
    """Calcula el área o perímetro de un círculo."""
    limpiar_pantalla()
    cambiar_color(15, 7)
    imprimir_titulo("CÍRCULO")
    radio = float(input("Ingrese el radio del círculo: "))

    if radio > 0:
        opcion = elegir_operacion()
        if opcion == 1:
            print(f"\nÁrea: {math.pi * radio ** 2:.2f} unidades cuadradas")
        elif opcion == 2:
            print(f"\nPerímetro: {2 * math.pi * radio:.2f} unidades")
        else:
            print("Opción no válida.")
    else:
        print("Entrada inválida. El radio debe ser mayor a 0.")
    input("Presione Enter para continuar...")


def mostrar_menu():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    while True:
        limpiar_pantalla()
        cambiar_color(15, 1)
        imprimir_titulo("*** MENÚ PRINCIPAL ***")
        print("1.- CUADRADO")
        print("2.- TRIÁNGULO")
        print("3.- TRAPECIO")
        print("4.- CÍRCULO")
        print("\n5.- CONVERSIONES DE ÁNGULOS\n")
        print("6.- SALIR")

        opcion = int(input("\nSeleccione una opción: "))

        if opcion == 1:
            area_perimetro_cuadrado()
        elif opcion == 2:
            area_perimetro_triangulo()
        elif opcion == 3:
            area_perimetro_trapecio()
        elif opcion == 4:
            area_perimetro_circulo()
        elif opcion == 5:
            conversion_angulos()
        elif opcion == 6:
            cambiar_color(15, 0)
            print("\nSaliendo del programa...")
            time.sleep(1)
            break
        else:
            print("Opción no válida.")
            time.sleep(1.5)


if __name__ == "__main__":
    if not validar_contrasena():
        cambiar_color(4, 0)
        print("\nAcceso denegado. Saliendo del programa...")
        time.sleep(1.5)
    else:
        mostrar_menu()
