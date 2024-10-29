import sympy as sp

# Definir variable simbólica para la función
x = sp.symbols('x')

# Solicitar al usuario la función, límites y tolerancia
funcion_str = input("Ingresa la función en términos de x (ej. x**2 - 4): ")
a = float(input("Ingresa el límite inferior (a): "))
b = float(input("Ingresa el límite superior (b): "))
epsilon = float(input("Ingresa la tolerancia de error (epsilon): "))

# Convertir la cadena de función en una expresión simbólica
funcion = sp.sympify(funcion_str)

# Convertir la función simbólica en una función numérica
f = sp.lambdify(x, funcion)

# Verificar que f(a) y f(b) tengan signos opuestos
if f(a) * f(b) < 0:
    print("Error: f(a) y f(b) deben tener signos opuestos.")
else:
    # Implementación
    iteracion = 0
    while abs(b - a) > epsilon:
        # Calcular el punto medio
        c = (a + b) / 2.0
        # Evaluar f(c)
        f_c = f(c)

        print(f"Iteración {iteracion}: a = {a}, b = {b}, c = {c}, f(c) = {f_c}")

        # Verificar si hemos encontrado la raíz con suficiente precisión
        if abs(f_c) < epsilon:
            print("Raíz encontrada con la tolerancia de error.")
            break

        # Decidir el nuevo intervalo
        if f(a) * f_c < 0:
            b = c
        else:
            a = c

        iteracion += 1

    # Imprimir resultado final
    raiz = (a + b) / 2.0
    print(f"La raíz aproximada es: {raiz} con una tolerancia de {epsilon}")
