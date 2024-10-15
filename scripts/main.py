# Paso de valor
def doblar_valor(numero):
    numero *= 2
n = 10
doblar_valor(n)
m = 10
doblar_valor(m)
    
print(n) # 10

# Paso de referencia
def doblar_valores(*numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2
ns = [10, 50, 100]
doblar_valores(*ns)

