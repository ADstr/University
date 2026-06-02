import numpy as np
from typing import Union, Callable

from numpy.core.function_base import linspace


def solve_euler(fun: Callable, t_span: np.array, y0: np.array):
    ''' 
    Funkcja umożliwiająca rozwiązanie układu równań różniczkowych z wykorzystaniem metody Eulera w przód.
    
    Parameters:
    fun: Prawa strona równania. Podana funkcja musi mieć postać fun(t, y). 
    Tutaj t jest skalarem i istnieją dwie opcje dla ndarray y: Może mieć kształt (n,); wtedy fun musi zwrócić array_like z kształtem (n,). 
    Alternatywnie może mieć kształt (n, k); wtedy fun musi zwrócić tablicę typu array_like z kształtem (n, k), tj. każda kolumna odpowiada jednej kolumnie w y. 
    t_span: wektor czasu dla którego ma zostać rozwiązane równanie
    y0: warunke początkowy równanai o wymiarze (n,)
    Results:
    (np.array): macierz o wymiarze (n,m) zawierająca w wkolumnach kolejne rozwiązania fun w czasie t_span.  

    '''
    l=np.size(y0)
    t=np.size(t_span)
    new=np.zeros([t,l])  
    new[0]=y0
    h=t_span[1]-t_span[0]

    for ind in range(1,t):
      f=fun(new[ind-1],t_span[ind-1])
      for i in range(l):
          f[i]*=h
      new[ind]=new[ind-1]+f
    return new








    # if np.size(y0)==1 :
    #     return (seuler(fun,t_span,y0[0]))
    # else :
    #     return (seuler(fun,t_span,y0[0]),seuler(fun,t_span,y0[1]))
 

def seuler(fun: Callable, t_span: np.array, y0: int):
    new=np.zeros(np.size(t_span))
    new[0]=y0
    h=t_span[1]-t_span[0]
    for ind in range(1,np.size(t_span)):
      new[ind]=new[ind-1]+h*fun(new[ind-1],t_span[ind-1])
        
    return new