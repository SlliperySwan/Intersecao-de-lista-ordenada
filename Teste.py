import time
import random
from IntersecaoComRepeticao import intersecao as intersecaoR
from IntersecaoSemRepeticao import intersecao

# Exemplo COM repetição 

array1 = [1, 3, 4, 5, 7, 9, 11, 11, 12, 15]
array2 = [1, 2, 2, 5, 6, 10, 10, 11, 12, 20]

inicio_r = time.time()
resultado_r = intersecaoR(array1, array2)
fim_r = time.time()

print("Interseção COM repetição 100 elementos")
print("Array 1:", array1)
print("Array 2:", array2)
print("Resultado:", resultado_r)
print("Tempo: {:.6f} segundos".format(fim_r - inicio_r))
print("================================================================================")

array1 = sorted(set([i * 4 for i in range(100)] + [i * 5 for i in range(30)]))
array2 = sorted(set([i * 4 for i in range(100)] + [i * 5 for i in range(30)]))

inicio_r = time.time()
resultado_r = intersecaoR(array1, array2)
fim_r = time.time()

print("Interseção COM repetição 100 elementos")
print("Array 1:", array1)
print("Array 2:", array2)
print("Resultado:", resultado_r)
print("Tempo: {:.6f} segundos".format(fim_r - inicio_r))
print("================================================================================")

array1 = sorted([random.randint(1, 10000) for _ in range(1000)])
array2 = sorted([random.randint(1, 10000) for _ in range(1000)])

inicio_r = time.time()
resultado_r = intersecaoR(array1, array2)
fim_r = time.time()

print("Interseção COM repetição 1000 elementos")
print("Array 1:", array1)
print("Array 2:", array2)
print("Resultado:", resultado_r)
print("Tempo: {:.6f} segundos".format(fim_r - inicio_r))
print("================================================================================")

array1 = sorted([random.randint(1, 10000) for _ in range(10_000)])
array2 = sorted([random.randint(1, 10000) for _ in range(10_000)])

inicio_r = time.time()
resultado_r = intersecaoR(array1, array2)
fim_r = time.time()

print("Interseção COM repetição 10.000 elementos")
print("Array 1:", array1)
print("Array 2:", array2)
print("Resultado:", resultado_r)
print("Tempo: {:.6f} segundos".format(fim_r - inicio_r))
print("================================================================================")

array1 = sorted([random.randint(1, 10000) for _ in range(100_000)])
array2 = sorted([random.randint(1, 10000) for _ in range(100_000)])

inicio_r = time.time()
resultado_r = intersecaoR(array1, array2)
fim_r = time.time()

print("Interseção COM repetição 100.000 elementos")
print("Array 1:", array1)
print("Array 2:", array2)
print("Resultado:", resultado_r)
print("Tempo: {:.6f} segundos".format(fim_r - inicio_r))
print("================================================================================")

array1 = sorted([random.randint(1, 10000) for _ in range(1_000_000)])
array2 = sorted([random.randint(1, 10000) for _ in range(1_000_000)])

inicio_r = time.time()
resultado_r = intersecaoR(array1, array2)
fim_r = time.time()

print("Interseção COM repetição 1.000.000 elementos")
print("Resultado:", resultado_r)
print("Tempo: {:.6f} segundos".format(fim_r - inicio_r))
print("================================================================================")
print("================================================================================")

# Exemplo SEM repetição

array3 = [1, 3, 4, 5, 7, 9, 10, 13, 15, 17]
array4 = [1, 2, 4, 6, 8, 10, 12, 15, 16, 20]

inicio_sr = time.time()
resultado_r2 = intersecao(array3, array4)
fim_sr = time.time()

print("Interseção SEM repetição 10 elementos")
print("Array 3:", array3)
print("Array 4:", array4)
print("Resultado:", resultado_r2)
print("Tempo: {:.6f} segundos".format(fim_sr - inicio_sr))
print("================================================================================")

array3 = sorted(random.sample(range(1, 10001), 100))
array4 = sorted(random.sample(range(1, 10001), 100))

inicio_sr = time.time()
resultado_r2 = intersecao(array3, array4)
fim_sr = time.time()

print("Interseção SEM repetição 100 elementos")
print("Array 3:", array3)
print("Array 4:", array4)
print("Resultado:", resultado_r2)
print("Tempo: {:.6f} segundos".format(fim_sr - inicio_sr))
print("================================================================================")

array3 = sorted(random.sample(range(1, 10001), 1000))
array4 = sorted(random.sample(range(1, 10001), 1000))

inicio_sr = time.time()
resultado_r2 = intersecao(array3, array4)
fim_sr = time.time()

print("Interseção SEM repetição 1000 elementos")
print("Array 3:", array3)
print("Array 4:", array4)
print("Resultado:", resultado_r2)
print("Tempo: {:.6f} segundos".format(fim_sr - inicio_sr))
print("================================================================================")

array3 = sorted(random.sample(range(1, 100000), 10000))
array4 = sorted(random.sample(range(1, 10001), 10000))

inicio_sr = time.time()
resultado_r2 = intersecao(array3, array4)
fim_sr = time.time()

print("Interseção SEM repetição 10.000 elementos")
print("Array 3:", array3)
print("Array 4:", array4)
print("Resultado:", resultado_r2)
print("Tempo: {:.6f} segundos".format(fim_sr - inicio_sr))
print("================================================================================")

array3 = sorted(random.sample(range(1, 100001), 100000))
array4 = sorted(random.sample(range(1, 100001), 100000))

inicio_sr = time.time()
resultado_r2 = intersecao(array3, array4)
fim_sr = time.time()

print("Interseção SEM repetição 100.000 elementos")
print("Array 3:", array3)
print("Array 4:", array4)
print("Resultado:", resultado_r2)
print("Tempo: {:.6f} segundos".format(fim_sr - inicio_sr))
print("================================================================================")

array3 = sorted(random.sample(range(1, 10000001), 1_000_000))
array4 = sorted(random.sample(range(1, 10000001), 1_000_000))

inicio_sr = time.time()
resultado_r2 = intersecao(array3, array4)
fim_sr = time.time()

print("Interseção SEM repetição 1.000.000.000 elementos")
print("Array 3:", array3)
print("Array 4:", array4)
print("Resultado:", resultado_r2)
print("Tempo: {:.6f} segundos".format(fim_sr - inicio_sr))
print("================================================================================")
