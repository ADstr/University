import numpy as np
import scipy as sp
from scipy import linalg
from  datetime import datetime
import pickle

from typing import Union, List, Tuple


def spare_matrix_Abt(m: int,n: int):
    """Funkcja tworząca zestaw składający się z macierzy A (m,n), 
    wektora b (n,)  i
     pomocniczego wektora t (m,) zawierających losowe wartości
    Parameters:
    m(int): ilość wierszy macierzy A
    n(int): ilość kolumn macierzy A
    Results:
    (np.ndarray, np.ndarray): macierz o rozmiarze (m,n) i wektorem (m,)
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(m,int) and isinstance(n,int):
        t=np.linspace(0,1,m)
        b = np.cos(4*t)
        a=np.vander(t,n,increasing='True')
        return (a,b)
    else:  
      return None


def square_from_rectan(A: np.ndarray, b: np.ndarray):
    """Funkcja przekształcająca układ równań z prostokątną macierzą współczynników na kwadratowy układ równań. 
    Funkcja ma zwrócić nową
     macierz współczynników  i nowy wektor współczynników
    Parameters:
      A: macierz A (m,n) zawierająca współczynniki równania
      b: wektor b (m,) zawierający współczynniki po prawej stronie równania
    Results:
    (np.ndarray, np.ndarray): macierz o rozmiarze (n,n) i wektorem (n,)
             Jeżeli dane wejściowe niepoprawne funkcja zwraca None
     """
    if isinstance(A,np.ndarray) and isinstance(b,np.ndarray):
      if (np.ndim(A)==2) and (np.ndim(b)==1):
        At=A.transpose()
        return (At@A,At@b)
      else:
       return None
    else:
     return None



def residual_norm(A: np.ndarray, x: np.ndarray, b: np.ndarray):
    """Funkcja obliczająca normę residuum dla równania postaci:
    Ax = b

      Parameters:
      A: macierz A (m,n) zawierająca współczynniki równania
      x: wektor x (n,) zawierający rozwiązania równania
      b: wektor b (m,) zawierający współczynniki po prawej stronie równania

      Results:
      (float)- wartość normy residuom dla podanych parametrów
      """
    if isinstance(A,np.ndarray) and (x,np.ndarray) and (b,np.ndarray) :
        return np.linalg.norm(A@x-b)
    else:
      return None




def rectangle(A:np.ndarray,b:np.ndarray):
    A2,b2= square_from_rectan(A,b)
    return np.linalg.solve(A2,b2)

def lstsq(A:np.ndarray,b:np.ndarray):
    return np.linalg.lstsq(A,b)[0]

def qr(A:np.ndarray,b:np.ndarray):
    q, r = np.linalg.qr(A)
    return sp.linalg.solve_triangular(r, q.T @ b)

def SVD(A:np.ndarray,b:np.ndarray):
    [U, S, V] = np.linalg.svd(A,full_matrices=False)
    S = np.diag(S)
    return V.T @ np.linalg.solve(S, U.T @ b)