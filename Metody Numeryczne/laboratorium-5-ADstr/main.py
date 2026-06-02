import numpy as np
import scipy
import pickle
import matplotlib
import matplotlib.pyplot as plt

from typing import Union, List, Tuple


def first_spline(x: np.ndarray, y: np.ndarray):
    """Funkcja wyznaczająca wartości współczynników spline pierwszego stopnia.

    Parametrs:
    x(float): argumenty, dla danych punktów
    y(float): wartości funkcji dla danych argumentów

    return (a,b) - krotka zawierająca współczynniki funkcji linowych"""
    if isinstance(x,np.ndarray) and (y,np.ndarray):
      if x.shape==y.shape:
          a=[]
          b=[]
          for i in range(len(x)-1):
              a.append((y[i+1]-y[i])/(x[i+1]-x[i]))
              b.append(y[i]-a[i]*x[i])
          return (a,b)

      else:
          return None
    else:
       return None


def cubic_spline(x: np.ndarray, y: np.ndarray, tol=1e-100):
    """
    Interpolacja splajnów cubicznych

    Returns:
    b współczynnik przy x stopnia 1
    c współczynnik przy x stopnia 2
    d współczynnik przy x stopnia 3
    """
    return None

def jacobi(A, b, x0, tol, n_iterations=300):
    """
    Iteracyjne rozwiązanie równania Ax=b dla zadanego x0

    Returns:
    x - estymowane rozwiązanie
    """

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

def chebyshev_nodes(n:int=10):

    if isinstance(n, int):

        nodes = np.zeros(n + 1)
        for k in range(n + 1):
            nodes[k] = np.cos(k * np.pi / n)

        return nodes
    else:
        return None

    
def bar_czeb_weights(n:int=10):

    if isinstance(n, int):
        weights = np.zeros(n + 1)

        for j in range(n + 1):

            if j == 0 or j == n:
                omega = 0.5
                weights[j] = (-1)**j * omega

            else:
                omega = 1
                weights[j] = (-1)**j * omega

        return weights
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
    if all(isinstance(i, np.ndarray) for i in [xi, yi, wi, x]): 
        if xi.shape == yi.shape and yi.shape == wi.shape:
            Y = []
            for x in np.nditer(x):
                L = wi/(x-xi)

                Y.append(yi @ L / sum(L))

            Y = np.array(Y)
            return Y
    else:
        return None
