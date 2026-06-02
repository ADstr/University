##
import numpy as np
import scipy
import pickle
import matplotlib.pyplot as plt

from typing import Union, List, Tuple

def chebyshev_nodes(n:int=10)-> np.ndarray:
    """Funkcja tworząca wektor zawierający węzły czybyszewa w postaci wektora (n+1,)
    
    Parameters:
    n(int): numer ostaniego węzła Czebyszewa. Wartość musi być większa od 0.
     
    Results:
    np.ndarray: wektor węzłów Czybyszewa o rozmiarze (n+1,). 
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(n,int):
        w=[]
        for x in range(n+1):
                w.append(np.cos(np.pi*x/n))
        return np.array(w) 
    else:
        return None

def bar_czeb_weights(n:int=10)-> np.ndarray:
    """Funkcja tworząca wektor wag dla węzłów czybyszewa w postaci (n+1,)
    
    Parameters:
    n(int): numer ostaniej wagi dla węzłów Czebyszewa. Wartość musi być większa od 0.
     
    Results:
    np.ndarray: wektor wag dla węzłów Czybyszewa o rozmiarze (n+1,). 
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(n,int):
        weight=[]
        for j in range(n+1):
            wj=(-1)**j
            if j==0 or j==n:
                wj=wj/2
            weight.append(wj)
        return np.array(weight)
    else:
        return None
    
def  barycentric_inte(xi:np.ndarray,yi:np.ndarray,wi:np.ndarray,x:np.ndarray)-> np.ndarray:
    """Funkcja przprowadza interpolację metodą barycentryczną dla zadanych węzłów xi
        i wartości funkcji interpolowanej yi używając wag wi. Zwraca wyliczone wartości
        funkcji interpolującej dla argumentów x w postaci wektora (n,) gdzie n to dłógość
        wektora n. 
    
    Parameters:
    xi(np.ndarray): węzły interpolacji w postaci wektora (m,), gdzie m > 0
    yi(np.ndarray): wartości funkcji interpolowanej w węzłach w postaci wektora (m,), gdzie m>0
    wi(np.ndarray): wagi interpolacji w postaci wektora (m,), gdzie m>0
    x(np.ndarray): argumenty dla funkcji interpolującej (n,), gdzie n>0 
     
    Results:
    np.ndarray: wektor wartości funkcji interpolujący o rozmiarze (n,). 
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if all(isinstance(i,np.ndarray) for i in [xi,yi,wi,x]):
          if xi.shape==yi.shape and yi.shape==wi.shape:      
                Y=[]
                for x in np.nditer(x):
                    L=wi/(x-xi)
                    Y.append(yi@L/sum(L))
                Y=np.array(Y)
                return Y
    else:
        return None
    
def L_inf(xr:Union[int, float, List, np.ndarray],x:Union[int, float, List, np.ndarray])-> float:
    """Obliczenie normy  L nieskończonośćg. 
    Funkcja powinna działać zarówno na wartościach skalarnych, listach jak i wektorach biblioteki numpy.
      
    Parameters:
    xr (Union[int, float, List, np.ndarray]): wartość dokładna w postaci wektora (n,)
    x (Union[int, float, List, np.ndarray]): wartość przybliżona w postaci wektora (n,1)
    
    Returns:
    float: wartość normy L nieskończoność,
                                    NaN w przypadku błędnych danych wejściowych
    """
    if all(isinstance(i,np.ndarray) for i in [xr,x]):
        if xr.shape==x.shape:
            return max(np.abs(xr-x))
        else:
            return np.Nan
    elif all(isinstance(i,(int,float)) for i in [xr,x]):
        return np.abs(xr-x)
    elif all(isinstance(i,list) for i in [xr,x]):
        return np.abs(max(xr)-max(x))
    else:
        return np.Nan

    