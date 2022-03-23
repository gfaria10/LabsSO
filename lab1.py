import math
import time
import multiprocessing

n = int(input('Entre com o número de termos da série: '))
print()

numerador = 2
denominador = 3
produto = numerador/denominador

inicio = time.time()

for i in range(1, n+1):
    if i % 2 == 1:
        numerador = numerador + 2
    else:
        denominador = denominador + 2
    produto = produto*(numerador/denominador)
    
pi = 4 * produto

fim = time.time()

print('Tempo de execução: %.3f s' %(fim - inicio))
print('Aproximação de pi com %d iterações: %.10f' %(n, pi))
print('Valor exato de pi: %.10f' %math.pi)

erro = abs(math.pi - pi)
print('Erro de aproximação: %.10f' %erro)