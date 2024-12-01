import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import time
import math


# Funciones originales del código sin cambios

def cambiar_color(texto, fondo):
    os.system(f'color {fondo:X}{texto:X}')


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def imprimir_titulo(titulo):
    print("*******************************************")
    print(f"             {titulo}")
    print("*******************************************")


def validar_contrasena():
    contrasena_correcta = "170522"
    intentos = 3

    while intentos > 0:
        entrada = simpledialog.askstring("Validación", "Ingrese la CLAVE:", show="*")
        if entrada == contrasena_correcta:
            messagebox.showinfo("Acceso permitido", "Contraseña correcta. Bienvenido.")
            return True
        else:
            intentos -= 1
            messagebox.showwarning(
                "Contraseña incorrecta",
                f"Contraseña incorrecta. Intentos restantes: {intentos}",
            )
    messagebox.showerror("Acceso denegado", "Se agotaron los intentos. Saliendo.")
    return False


def conversion_angulos():
    def convertir():
        try:
            angulo = float(entry_angulo.get())
            opcion = var_opcion.get()
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
                messagebox.showerror("Error", "Opción no válida.")
                return
            lbl_resultado.config(text=f"Resultado: {resultado:.6f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un ángulo válido.")

    ventana_conv = tk.Toplevel()
    ventana_conv.title("Conversiones de ángulos")
    tk.Label(ventana_conv, text="Seleccione la conversión:").pack()
    var_opcion = tk.IntVar(value=1)
    opciones = [
        "1. Centesimal a Radian",
        "2. Centesimal a Sexagesimal",
        "3. Sexagesimal a Centesimal",
        "4. Sexagesimal a Radian",
        "5. Radian a Centesimal",
        "6. Radian a Sexagesimal",
    ]
    for i, opcion in enumerate(opciones, 1):
        tk.Radiobutton(ventana_conv, text=opcion, variable=var_opcion, value=i).pack(anchor="w")
    tk.Label(ventana_conv, text="Ingrese el ángulo:").pack()
    entry_angulo = tk.Entry(ventana_conv)
    entry_angulo.pack()
    lbl_resultado = tk.Label(ventana_conv, text="Resultado: ")
    lbl_resultado.pack()
    tk.Button(ventana_conv, text="Convertir", command=convertir).pack(pady=5)


def elegir_operacion():
    return simpledialog.askinteger("Operación", "¿Qué desea calcular? 1. Área 2. Perímetro")


def area_perimetro_cuadrado():
    def calcular():
        try:
            lado = float(entry_lado.get())
            if lado > 0:
                opcion = elegir_operacion()
                if opcion == 1:
                    resultado = lado * lado
                    lbl_resultado.config(text=f"Área: {resultado:.2f} unidades cuadradas")
                elif opcion == 2:
                    resultado = lado * 4
                    lbl_resultado.config(text=f"Perímetro: {resultado:.2f} unidades")
                else:
                    messagebox.showerror("Error", "Opción no válida.")
            else:
                messagebox.showerror("Error", "El lado debe ser mayor a 0.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido para el lado.")

    ventana = tk.Toplevel()
    ventana.title("CUADRADO")
    tk.Label(ventana, text="Ingrese el lado del cuadrado:").pack()
    entry_lado = tk.Entry(ventana)
    entry_lado.pack()
    lbl_resultado = tk.Label(ventana, text="Resultado: ")
    lbl_resultado.pack()
    tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)


def area_perimetro_triangulo():
    def calcular():
        try:
            base = float(entry_base.get())
            altura = float(entry_altura.get())
            lado1 = float(entry_lado1.get())
            lado2 = float(entry_lado2.get())
            if base > 0 and altura > 0 and lado1 > 0 and lado2 > 0:
                opcion = elegir_operacion()
                if opcion == 1:
                    resultado = (base * altura) / 2
                    lbl_resultado.config(text=f"Área: {resultado:.2f} unidades cuadradas")
                elif opcion == 2:
                    resultado = base + lado1 + lado2
                    lbl_resultado.config(text=f"Perímetro: {resultado:.2f} unidades")
                else:
                    messagebox.showerror("Error", "Opción no válida.")
            else:
                messagebox.showerror("Error", "Todos los valores deben ser mayores a 0.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

    ventana = tk.Toplevel()
    ventana.title("TRIÁNGULO")
    tk.Label(ventana, text="Ingrese la base del triángulo:").pack()
    entry_base = tk.Entry(ventana)
    entry_base.pack()
    tk.Label(ventana, text="Ingrese la altura del triángulo:").pack()
    entry_altura = tk.Entry(ventana)
    entry_altura.pack()
    tk.Label(ventana, text="Ingrese el primer lado del triángulo:").pack()
    entry_lado1 = tk.Entry(ventana)
    entry_lado1.pack()
    tk.Label(ventana, text="Ingrese el segundo lado del triángulo:").pack()
    entry_lado2 = tk.Entry(ventana)
    entry_lado2.pack()
    lbl_resultado = tk.Label(ventana, text="Resultado: ")
    lbl_resultado.pack()
    tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)


def area_perimetro_trapecio():
    def calcular():
        try:
            base_mayor = float(entry_base_mayor.get())
            base_menor = float(entry_base_menor.get())
            altura = float(entry_altura.get())
            lado1 = float(entry_lado1.get())
            lado2 = float(entry_lado2.get())
            if base_mayor > 0 and base_menor > 0 and altura > 0 and lado1 > 0 and lado2 > 0:
                opcion = elegir_operacion()
                if opcion == 1:
                    resultado = ((base_mayor + base_menor) * altura) / 2
                    lbl_resultado.config(text=f"Área: {resultado:.2f} unidades cuadradas")
                elif opcion == 2:
                    resultado = base_mayor + base_menor + lado1 + lado2
                    lbl_resultado.config(text=f"Perímetro: {resultado:.2f} unidades")
                else:
                    messagebox.showerror("Error", "Opción no válida.")
            else:
                messagebox.showerror("Error", "Todos los valores deben ser mayores a 0.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

    ventana = tk.Toplevel()
    ventana.title("TRAPECIO")
    tk.Label(ventana, text="Ingrese la base mayor del trapecio:").pack()
    entry_base_mayor = tk.Entry(ventana)
    entry_base_mayor.pack()
    tk.Label(ventana, text="Ingrese la base menor del trapecio:").pack()
    entry_base_menor = tk.Entry(ventana)
    entry_base_menor.pack()
    tk.Label(ventana, text="Ingrese la altura del trapecio:").pack()
    entry_altura = tk.Entry(ventana)
    entry_altura.pack()
    tk.Label(ventana, text="Ingrese el primer lado del trapecio:").pack()
    entry_lado1 = tk.Entry(ventana)
    entry_lado1.pack()
    tk.Label(ventana, text="Ingrese el segundo lado del trapecio:").pack()
    entry_lado2 = tk.Entry(ventana)
    entry_lado2.pack()
    lbl_resultado = tk.Label(ventana, text="Resultado: ")
    lbl_resultado.pack()
    tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)


def area_perimetro_circulo():
    def calcular():
        try:
            radio = float(entry_radio.get())
            if radio > 0:
                opcion = elegir_operacion()
                if opcion == 1:
                    resultado = math.pi * radio ** 2
                    lbl_resultado.config(text=f"Área: {resultado:.2f} unidades cuadradas")
                elif opcion == 2:
                    resultado = 2 * math.pi * radio
                    lbl_resultado.config(text=f"Perímetro: {resultado:.2f} unidades")
                else:
                    messagebox.showerror("Error", "Opción no válida.")
            else:
                messagebox.showerror("Error", "El radio debe ser mayor a 0.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido para el radio.")

    ventana = tk.Toplevel()
    ventana.title("CÍRCULO")
    tk.Label(ventana, text="Ingrese el radio del círculo:").pack()
    entry_radio = tk.Entry(ventana)
    entry_radio.pack()
    lbl_resultado = tk.Label(ventana, text="Resultado: ")
    lbl_resultado.pack()
    tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)


def ejecutar_con_interfaz():
    def ejecutar_validar_contrasena():
        if validar_contrasena():
            ejecutar_menu()

    def ejecutar_menu():
        ventana_menu = tk.Toplevel(root)
        ventana_menu.title("Menú principal")
        tk.Label(ventana_menu, text="*** MENÚ PRINCIPAL ***", font=("Arial", 16)).pack(pady=10)
        botones = [
            ("CUADRADO", area_perimetro_cuadrado),
            ("TRIÁNGULO", area_perimetro_triangulo),
            ("TRAPECIO", area_perimetro_trapecio),
            ("CÍRCULO", area_perimetro_circulo),
            ("CONVERSIONES DE ÁNGULOS", conversion_angulos),
            ("SALIR", lambda: ventana_menu.destroy()),
        ]
        for texto, comando in botones:
            tk.Button(ventana_menu, text=texto, command=comando).pack(pady=5)

    root = tk.Tk()
    root.title("Sistema con interfaz gráfica")
    root.geometry("400x300")
    tk.Label(root, text="Sistema protegido", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="Ingresar", command=ejecutar_validar_contrasena).pack(pady=10)
    tk.Button(root, text="Salir", command=root.quit).pack(pady=10)
    root.mainloop()


if __name__ == "__main__":
    ejecutar_con_interfaz()
