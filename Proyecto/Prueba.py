import tkinter as tk
from tkinter import messagebox

def f_evaluada(funcion, x_valores):
    # Evalúa la función para cada valor de x en la lista x_valores
    return [eval(funcion, {"x": x}) for x in x_valores]

def calcular_error(exacto, aproximado):
    return abs(exacto - aproximado)

def metodo_trapezoidal(funcion, a, b, n):
    x = [a + i * (b - a) / n for i in range(n + 1)]
    fx = f_evaluada(funcion, x)
    h = (b - a) / n
    resultado = (h / 2) * (fx[0] + 2 * sum(fx[1:n]) + fx[n])
    return resultado

def metodo_simpson_13(funcion, a, b, n):
    if n % 2 != 0:
        messagebox.showerror("Error", "Para Simpson 1/3, n debe ser par.")
        return None
    x = [a + i * (b - a) / n for i in range(n + 1)]
    fx = f_evaluada(funcion, x)
    h = (b - a) / n
    resultado = (h / 3) * (fx[0] + 4 * sum(fx[1:n:2]) + 2 * sum(fx[2:n-1:2]) + fx[n])
    return resultado

def metodo_simpson_38(funcion, a, b, n):
    if n % 3 != 0:
        messagebox.showerror("Error", "Para Simpson 3/8, n debe ser múltiplo de 3.")
        return None
    x = [a + i * (b - a) / n for i in range(n + 1)]
    fx = f_evaluada(funcion, x)
    h = (b - a) / n
    resultado = (3 * h / 8) * (fx[0] + 3 * sum(fx[1:n:3] + fx[2:n:3]) + 2 * sum(fx[3:n-2:3]) + fx[n])
    return resultado

def calcular_integral():
    try:
        funcion = entry_funcion.get()
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = int(entry_n.get())
        if n <= 0:
            messagebox.showerror("Error", "El número de subintervalos debe ser mayor a 0.")
            return
    except ValueError:
        messagebox.showerror("Error", "Límites o subintervalos inválidos.")
        return

    # Selección
    metodo = metodo_seleccion.get()
    resultado = None

    if metodo == "Trapezoidal":
        resultado = metodo_trapezoidal(funcion, a, b, n)
    elif metodo == "Simpson 1/3":
        resultado = metodo_simpson_13(funcion, a, b, n)
    elif metodo == "Simpson 3/8":
        resultado = metodo_simpson_38(funcion, a, b, n)

    if resultado is not None:
        resultado_var.set(f"Resultado: {resultado:.6f}")
    else:
        resultado_var.set("Error en el cálculo")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Métodos de Integración Numérica")

# Variables de selección y resultado
metodo_seleccion = tk.StringVar(value="Trapezoidal")
resultado_var = tk.StringVar()

# Etiquetas y Entradas
tk.Label(root, text="Función f(x):").grid(row=0, column=0, sticky="e")
entry_funcion = tk.Entry(root, width=30)
entry_funcion.grid(row=0, column=1)
entry_funcion.insert(0, "x**2")  # Ejemplo de entrada por defecto

tk.Label(root, text="Límite inferior (a):").grid(row=1, column=0, sticky="e")
entry_a = tk.Entry(root, width=15)
entry_a.grid(row=1, column=1)
entry_a.insert(0, "0")  # Ejemplo de entrada por defecto

tk.Label(root, text="Límite superior (b):").grid(row=2, column=0, sticky="e")
entry_b = tk.Entry(root, width=15)
entry_b.grid(row=2, column=1)
entry_b.insert(0, "1")  # Ejemplo de entrada por defecto

tk.Label(root, text="Subintervalos (n):").grid(row=3, column=0, sticky="e")
entry_n = tk.Entry(root, width=15)
entry_n.grid(row=3, column=1)
entry_n.insert(0, "10")  # Ejemplo de entrada por defecto

# Selección
tk.Label(root, text="Método de Integración:").grid(row=4, column=0, sticky="e")
tk.Radiobutton(root, text="Trapezoidal", variable=metodo_seleccion, value="Trapezoidal").grid(row=4, column=1, sticky="w")
tk.Radiobutton(root, text="Simpson 1/3", variable=metodo_seleccion, value="Simpson 1/3").grid(row=5, column=1, sticky="w")
tk.Radiobutton(root, text="Simpson 3/8", variable=metodo_seleccion, value="Simpson 3/8").grid(row=6, column=1, sticky="w")

# Botón Calcular
tk.Button(root, text="Calcular Integral", command=calcular_integral).grid(row=7, column=0, columnspan=2)

# Resultados
tk.Label(root, textvariable=resultado_var, fg="green").grid(row=9, column=0, columnspan=2)

# Iniciar la aplicación
root.mainloop()
