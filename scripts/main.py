# Paso de valor
def doblar_valor(numero):
    numero *= 2
n = 10
doblar_valor(n)
m = 10
doblar_valor(m)

doblar_valor(10)

# Paso de referencia
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ns = [10, 50, 100]

def next_multiple(n, m):
    return n + (m - n % m) % m

# Dada un numero n

def main():
    print(next_multiple(4, 4))  # 4
    print(next_multiple(6, 4))  # 8

if __name__ == '__main__':
    main()
