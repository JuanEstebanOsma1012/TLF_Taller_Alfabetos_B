import tkinter as tk
from tkinter import simpledialog, messagebox

from numpy import character

import string
from random import randint
import random

import copy

# Función para verificar si una cadena es palíndromo
def es_palindromo(cadena):
    for letra in alfabeto:
        if letra not in alfabeto: return False
    return cadena == cadena[::-1]

def aplicar_union(alfabeto1, alfabeto2):
    alfabeto_union = copy.deepcopy(alfabeto1)

    for caracter in alfabeto2:
        if caracter not in alfabeto_union:
            alfabeto_union.append(caracter)

    return alfabeto_union

def aplicar_concatenacion(alfabeto1, alfabeto2):
    alfabeto_concat = []

    for caracter in alfabeto1:
        for caracter2 in alfabeto2:
            alfabeto_concat.append(caracter + caracter2)

    return alfabeto_concat

def aplicar_estrella(alfabeto1):
    alfabeto_estrella = ["ε"]

    while len(alfabeto_estrella)<=6:
        for caracter in alfabeto1:
            for caracter2 in alfabeto1:
                alfabeto_estrella.append(caracter + caracter2)

    alfabeto_estrella.append("...")
    return alfabeto_estrella

# Función para pedir el alfabeto
def pedir_alfabeto():

    bandera = False
    while not bandera:
        numero_elementos = simpledialog.askstring("Input", "Ingresa el numero de elementos del alfabeto:")
        elementos= simpledialog.askstring("Input", "Ingresa los elementos del alfabeto separados por coma:")

        global alfabeto
        alfabeto = elementos.split(",")
        if len(alfabeto) == int (numero_elementos):
            bandera = True
        else:
            print("El numero de elementos y los elementos enviados no coinciden")
            
    return []

# Función para definir tres lenguajes a partir del alfabeto
def definir_lenguajes():
    if not alfabeto:
        messagebox.showerror("Error", "Primero ingresa el alfabeto.")
        return
    
    L1 = [alfabeto[i] for i in range (1, len(alfabeto), 2)]
    L2 = [alfabeto[i] for i in range (0, len(alfabeto), 2)]
    L3 = [alfabeto[i]+alfabeto[i-1] for i in range (1, len(alfabeto), 2)]
    
    resultado = f"Lenguajes generados:\nL1: {L1}\nL2: {L2}\nL3: {L3}\n"
    
    # Operación de unión
    union_12 = aplicar_union(L1, L2)
    union_13 = aplicar_union(L1, L3)
    union_23 = aplicar_union(L2, L3)
    union_todos = aplicar_union(union_12, L3)
    
    resultado += f"\nUniones:\nL1 ∪ L2: {union_12}\nL1 ∪ L3: {union_13}\nL2 ∪ L3: {union_23}\nL1 ∪ L2 ∪ L3: {union_todos}\n"
    
    # Operación de concatenación
    concatenacion_12 = aplicar_concatenacion(L1, L2)
    concatenacion_13 = aplicar_concatenacion(L1, L3)
    concatenacion_23 = aplicar_concatenacion(L2, L3)
    concatenacion_todos = aplicar_concatenacion(concatenacion_12, L3)
    
    resultado += f"\nConcatenaciones:\nL1 • L2: {concatenacion_12}\nL1 • L3: {concatenacion_13}\nL2 • L3: {concatenacion_23}\nL1 • L2 • L3: {concatenacion_todos}\n"
    
    # Cerradura estrella
    cerradura_estrella_L1 = aplicar_estrella(L1)
    cerradura_estrella_L2 = aplicar_estrella(L2)
    cerradura_estrella_L3 = aplicar_estrella(L3)
    
    resultado += f"\nCerradura estrella:\nL1*: {cerradura_estrella_L1}\nL2*: {cerradura_estrella_L2}\nL3*: {cerradura_estrella_L3}\n"
    
    messagebox.showinfo("Lenguajes y Operaciones", resultado)

def generar_palindromos():
    global alfabeto
    if not alfabeto:
        messagebox.showerror("Error", "Primero ingresa el alfabeto.")
        return
    
    palindromos = []
    for _ in range(3):
        # Elegir una longitud aleatoria entre 2 y 4 para la mitad del palíndromo
        longitud_mitad = random.randint(2, 4)
        mitad = "".join(random.choice(alfabeto) for _ in range(longitud_mitad))
        palindromo = mitad + mitad[::-1]  # La otra mitad es la inversa de la primera
        palindromos.append(palindromo)
    
    messagebox.showinfo("Palíndromos", f"Palíndromos generados: {palindromos}")

def generar_palindromos_2():

    max_size = 2

    ran = randint(max_size // 2, 3)  # obtenemos una cantidad random de letras a escoger
    if ran % 2 == 1: ran += 1
    sol: string = ""

    for i in range(0, ran):
        char: character = alfabeto[randint(0, len(alfabeto)-1)]
        sol += char

    messagebox.showinfo("Palíndromos", f"Palíndromos generados: {' , '.join([sol, sol[::-1]])}")    

# Función para verificar si una cadena es un palíndromo
def verificar_palindromo():
    cadena = simpledialog.askstring("Input", "Ingresa una cadena para verificar si es palíndromo:")
    if cadena:
        if es_palindromo(cadena):
            messagebox.showinfo("Resultado", f"La cadena '{cadena}' es un palíndromo.")
        else:
            messagebox.showinfo("Resultado", f"La cadena '{cadena}' no es un palíndromo.")

# Función para invertir cadenas en un lenguaje
def invertir_cadenas():
    if not alfabeto:
        messagebox.showerror("Error", "Primero ingresa el alfabeto.")
        return
    
    L1 = [alfabeto[i]+alfabeto[i-1] for i in range (1, len(alfabeto), 2)]
    L_invertido = [L1[i][::-1] for i in range (0, len(L1))]
    
    messagebox.showinfo("Inversión de Cadenas", f"Lenguaje original: {L1}\nLenguaje invertido: {L_invertido}")

# Crear ventana principal
root = tk.Tk()
root.title("Menú de Lenguajes Formales")

# Botones del menú
btn_pedir_alfabeto = tk.Button(root, text="Pedir alfabeto", command=pedir_alfabeto)
btn_lenguajes = tk.Button(root, text="Definir Lenguajes y Operaciones", command=definir_lenguajes)
btn_palindromos = tk.Button(root, text="Generar Palíndromos", command=generar_palindromos)
btn_verificar_palindromo = tk.Button(root, text="Verificar si es Palíndromo", command=verificar_palindromo)
btn_invertir_cadenas = tk.Button(root, text="Invertir Cadenas en un Lenguaje", command=invertir_cadenas)

# Ubicación de los botones
btn_pedir_alfabeto.pack(pady=10)
btn_lenguajes.pack(pady=10)
btn_palindromos.pack(pady=10)
btn_verificar_palindromo.pack(pady=10)
btn_invertir_cadenas.pack(pady=10)

root.mainloop()