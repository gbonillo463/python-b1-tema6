"""
Enunciado:
Utilizando un depurador de código para Python. Corrije el error de la
función llamada 'average_of_even_numbers(numbers)' que acepta una lista de
números enteros como entrada y calcula el promedio de todos los números pares
en la lista.

Para depurar el código se puede usar pdb o herramientas de depuración
externas.

La función debe devolver un número flotante redondeado a dos decimales. Si no
hay números pares en la lista, la función debe devolver 0.

Parámetros:
    numbers: una lista de números enteros.

Ejemplo:
    Entrada:
        numbers = [2, 3, 4, 5, 6]
    Salida:
        4.0

"""


from typing import List

    
def average_of_even_numbers(numbers):
    #Find the error and rewrite the correct code.
    total = 0
    count = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
            count += 1
    if total == 0:
        return 0
    return round(total / count, 2)


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

numbers = [2, 3, 4, 5, 6]
result = average_of_even_numbers(numbers)
print(result)
