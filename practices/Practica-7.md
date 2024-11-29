# Practica 6 - Simulación de administracion de memoria en la CPU

## Objetivo

El objetivo de esta práctica es simular el funcionamiento de un sistema operativo y realizar un resumen de los pasos que se llevan a cabo en la administración de memoria en la CPU.
Estos pasos son:

1. Cargar el programa en memoria.
2. Asignar espacio de memoria a las variables.
3. Asignar espacio de memoria a las instrucciones.
4. Ejecutar el programa.

## Desarrollo

Para realizar esta práctica, se debe realizar un programa en Python que simule la administración de memoria en la CPU. El programa debe realizar los siguientes pasos:

1. Cargar el programa en memoria.

- Esto se puede simular con un diccionario que contenga las instrucciones del programa.

```python
programa = {
    0: "cargar 1, 2",
    1: "sumar 1, 2, 3",
    2: "imprimir 3"
}
```

2. Asignar espacio de memoria a las variables.

- Esto se puede simular con un array que contenga las variables del programa y que se asigne un espacio de memoria a cada una.

```python
variables = [
    "a": 0,
    "b": 0,
    "c": 0
]
```

3. Asignar espacio de memoria a las instrucciones.

- Esto se puede simular con un array que contenga las instrucciones del programa y que se ejecute una por una.

```python
instrucciones = [
    "cargar 1, 2",
    "sumar 1, 2, 3",
    "imprimir 3"
]
```

4. Ejecutar el programa.

- Esto se puede simular con un ciclo que recorra las instrucciones del programa y las ejecute, asignando los valores de las variables a las instrucciones.

```python
for instruccion in instrucciones:
    if instruccion.startswith("cargar"):
        instruccion = instruccion.split(" ")
        variables[int(instruccion[2])] = int(instruccion[1])
    elif instruccion.startswith("sumar"):
        instruccion = instruccion.split(" ")
        variables[int(instruccion[3])] = variables[int(instruccion[1])] + variables[int(instruccion[2])]
    elif instruccion.startswith("imprimir"):
        instruccion = instruccion.split(" ")
        print(variables[int(instruccion[1])])
```

5. Mostar el resultado.

- Al finalizar la ejecución del programa, se debe mostrar el resultado de las variables.

```python
print(variables)
```

## Entregable

El entregable de esta práctica es un programa en Python que simule la administración de memoria en la CPU. El programa debe realizar los pasos mencionados anteriormente y debe incluir comentarios que expliquen cada uno de los pasos.

## Fecha de entrega

Jueves 5 de Diciembre de 2024.
