import numpy as np
import pickle

from typing import Union, List, Tuple

from numpy.core.fromnumeric import shape

def random_matrix_Ab(m:int):
    """Funkcja tworząca zestaw składający się z macierzy A (m,m) i wektora b (m,)  zawierających losowe wartości
    Parameters:
    m(int): rozmiar macierzy
    Results:
    (np.ndarray, np.ndarray): macierz o rozmiarze (m,m) i wektorem (m,)
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(m,int) and m>0:
        return [np.random.randint(0,m,size=(m,m)),np.random.randint(0,m,size=(m,))]
    else:
       return None

def residual_norm(A:np.ndarray,x:np.ndarray, b:np.ndarray):
    """Funkcja obliczająca normę residuum dla równania postaci:
    Ax = b

      Parameters:
      A: macierz A (m,m) zawierająca współczynniki równania 
      x: wektor x (m.) zawierający rozwiązania równania 
      b: wektor b (m,) zawierający współczynniki po prawej stronie równania

      Results:
      (float)- wartość normy residuom dla podanych parametrów"""
    cos,spr=A.shape
    if isinstance(A,np.ndarray) and (x,np.ndarray) and (b,np.ndarray) and b.shape==x.shape and (spr==len(x)) :
        return np.linalg.norm(A@x-b)
    else:
      return None


def log_sing_value(n:int, min_order:Union[int,float], max_order:Union[int,float]):
    """Funkcja generująca wektor wartości singularnych rozłożonych w skali logarytmiczne
    
        Parameters:
         n(np.ndarray): rozmiar wektora wartości singularnych (n,), gdzie n>0
         min_order(int,float): rząd najmniejszej wartości w wektorze wartości singularnych
         max_order(int,float): rząd największej wartości w wektorze wartości singularnych
         Results:
         np.ndarray - wektor nierosnących wartości logarytmicznych o wymiarze (n,) zawierający wartości logarytmiczne na zadanym przedziale
         """
    if isinstance(n,int) and isinstance(min_order,(int,float),) and isinstance(max_order,(int,float)) and n>0 and min_order<max_order:
        v=np.logspace(min_order,max_order,n)
        v=np.flip(np.sort(v))
        return v
    else:
        return None
    
def order_sing_value(n:int, order:Union[int,float] = 2, site:str = 'gre'):
    """Funkcja generująca wektor losowych wartości singularnych (n,) będących wartościami zmiennoprzecinkowymi losowanymi przy użyciu funkcji np.random.rand(n)*10. 
        A następnie ustawiająca wartość minimalną (site = 'low') albo maksymalną (site = 'gre') na wartość o  10**order razy mniejszą/większą.
    
        Parameters:
        n(np.ndarray): rozmiar wektora wartości singularnych (n,), gdzie n>0
        order(int,float): rząd przeskalowania wartości skrajnej
        site(str): zmienna wskazująca stronnę zmiany:
            - site = 'low' -> sing_value[-1] * 10**order
            - site = 'gre' -> sing_value[0] * 10**order
        
        Results:
        np.ndarray - wektor wartości singularnych o wymiarze (n,) zawierający wartości logarytmiczne na zadanym przedziale
        """
    if isinstance(n,int) and isinstance(order,(int,float)) and isinstance(site,(str)) and n>0:
        v=np.random.rand(n)
        if site=='gre':
            v[0]=v[0]*(10**order)
            return np.flip(np.sort(v))
        elif site=='low':
            v[-1]=v[-1]*(10**(1/order))
            return np.flip(np.sort(v))
        else:
            return None
    else:
        return None


def create_matrix_from_A(A:np.ndarray, sing_value:np.ndarray):
    """Funkcja generująca rozkład SVD dla macierzy A i zwracająca otworzenie macierzy A z wykorzystaniem zdefiniowanego wektora warości singularnych

            Parameters:
            A(np.ndarray): rozmiarz macierzy A (m,m)
            sing_value(np.ndarray): wektor wartości singularnych (m,)


            Results:
            np.ndarray: macierz (m,m) utworzoną na podstawie rozkładu SVD zadanej macierzy A z podmienionym wektorem wartości singularnych na wektor sing_valu """
    if isinstance(A,np.ndarray) and isinstance(sing_value,np.ndarray):
        cos,spr=A.shape
        if spr==len(sing_value):
            U,S,V = np.linalg.svd(A)
            return np.dot(U * sing_value, V)
        else:
            return None
    else:
       return None