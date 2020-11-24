#!/usr/bin/env python
# coding: utf-8

# ## Ejercicio 1
# 
# Escribe una función llamada ejercicio1 que genere una lista con 15 valores enteros aleatorios que vayan de 1 a 100. La función debe devolver la lista con todos los valores.
# 

# In[ ]:


import random
import math


# In[ ]:


def ejercicio1():
    return random.sample(range(1, 100), 15)


# In[ ]:


randomlist = ejercicio1()


# ## Ejercicio 2
# 
# Escribe una función llamada ejercicio2 que recibe 2 argumentos: el primero será la lista que hemos implementado en el Ejercicio 1 y el segundo un número por el que se dividirá cada uno de los elementos de la lista. El resultado será una nueva lista.

# In[ ]:


def ejercicio2(randomlist,number):
    return list(map(lambda x: x / number , randomlist))


# In[ ]:


divided_randomlist = ejercicio2(randomlist,2)


# ## Ejercicio 3
# 
# Usando funciones anónimas, crea una nueva lista que contenga los valores enteros de cada uno de los elementos de la lista que devuelve la función implementada en el Ejercicio 2.

# In[ ]:


ejercicio3 = lambda x: list(map(lambda x: int(x), x))


# ## Ejercicio 4
# 
# Implementa una función, llamada ejercicio4, que reciba como argumentos dos números enteros y devuelva en una tupla los siguientes valores: el factorial del primer argumento y el máximo común divisor de ambos argumentos.

# In[ ]:


def ejercicio4(num1,num2):
    return math.factorial(num1),math.gcd(num1,num2)


# In[ ]:


ejercicio4(6,3)


# ## Ejercicio 5
# 
# Crea una función ejercicio5 que devuelva una lista con todos los valores contenidos en una lista que se pasa por argumento pero eliminando los valores repetidos. Prueba el funcionamiento de esta función con la lista obtenida en el Ejercicio 1.

# In[ ]:


def ejercicio5(repeated_list):
    return list(set(repeated_list))


# In[ ]:


ejercicio5(randomlist)

