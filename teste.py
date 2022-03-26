import threading
import time 

inicio = time.time()

def py_exp(y, n):
    result = 1
    for index in range(n):
        result = result * y
    return result 
  
y= 40
n= 400 
fim = time.time()

print(py_exp(y,n))
print('Tempo de execução: %.3f s' %(fim - inicio))