import numpy as np
import scipy
import pickle
import typing
import math
import types
import pickle 
from inspect import isfunction


from typing import Union, List, Tuple

def fun(x):
    return np.exp(-2*x)+x**2-1

def dfun(x):
    return -2*np.exp(-2*x) + 2*x

def ddfun(x):
    return 4*np.exp(-2*x) + 2


def bisection(a: Union[int,float], b: Union[int,float], f: typing.Callable[[float], float], epsilon: float, iteration: int) -> Tuple[float, int]:
    '''funkcja aproksymująca rozwiązanie równania f(x) = 0 na przedziale [a,b] metodą bisekcji.

    Parametry:
    a - początek przedziału
    b - koniec przedziału
    f - funkcja dla której jest poszukiwane rozwiązanie
    epsilon - tolerancja zera maszynowego (warunek stopu)
    iteration - ilość iteracji

    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and callable(f) and isinstance(epsilon,float) and isinstance(iteration,int):
      if epsilon>0 and iteration>0:  
        if f(a)*f(b)<0:
            for i in range(iteration):
                new=(b+a)/2
                if abs(f(new))<epsilon:
                    return new,i
                elif f(new)>0:
                    if f(a)>0:
                        a=new
                    else:
                        b=new
                else: 
                    if f(a)<0:
                        a=new
                    else:
                        b=new
            return new,iteration 
        else:
         return None  
      else:
          return None
    else:
      return None


def secant(a: Union[int,float], b: Union[int,float], f: typing.Callable[[float], float], epsilon: float, iteration: int) -> Tuple[float, int]:
    '''funkcja aproksymująca rozwiązanie równania f(x) = 0 na przedziale [a,b] metodą siecznych.

    Parametry:
    a - początek przedziału
    b - koniec przedziału
    f - funkcja dla której jest poszukiwane rozwiązanie
    epsilon - tolerancja zera maszynowego (warunek stopu)
    iteration - ilość iteracji

    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and callable(f) and isinstance(epsilon,float) and isinstance(iteration,int):
      if epsilon>0 and iteration>0:  
        if f(a)*f(b)<0:
            for i in range(iteration):
                new=(f(b)*a-f(a)*b)/(f(b)-f(a))
                if abs(f(new))<epsilon:
                    return new,i
                elif f(new)>0:
                    if f(a)>0:
                        a=new
                    else:
                        b=new
                else: 
                    if f(a)<0:
                        a=new
                    else:
                        b=new
            if abs(b - a) < epsilon:    
                return new,i   
            return new,iteration
        else:
            return None
      else:
         return None
    else:
      return None
    return None

def newton(f: typing.Callable[[float], float], df: typing.Callable[[float], float], ddf: typing.Callable[[float], float], a: Union[int,float], b: Union[int,float], epsilon: float, iteration: int) -> Tuple[float, int]:
    ''' Funkcja aproksymująca rozwiązanie równania f(x) = 0 metodą Newtona.
    Parametry: 
    f - funkcja dla której jest poszukiwane rozwiązanie
    df - pochodna funkcji dla której jest poszukiwane rozwiązanie
    ddf - druga pochodna funkcji dla której jest poszukiwane rozwiązanie
    a - początek przedziału
    b - koniec przedziału
    epsilon - tolerancja zera maszynowego (warunek stopu)
    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    if isinstance(a,int and float) and isinstance(b,int and float) and callable(df) and callable(f) and callable(ddf) and isinstance(epsilon,float) and isinstance(iteration,int):
      if epsilon>0 and iteration>0:
        dist=np.linspace(a,b,1000)
        fprim=df(dist)
        fbis=ddf(dist)
        if (np.all(np.sign(fprim))>0 or np.all(np.sign(fprim))<0) and (np.all(np.sign(fbis))>0 or np.all(np.sign(fbis))<0):
            if f(a)*f(b)<0:
                if f(a)*ddf(a)>0:
                 b=a
                for i in range(iteration):
                    b_new=b-f(b)/df(b)
                    if abs(b_new-b)<=epsilon:
                        return b_new,i
                    b=b_new
                return b_new,iteration
            else:
             return None
        else:
         return None
      else:
         return None
    else:
      return None
