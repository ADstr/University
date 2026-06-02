import numpy as np
import scipy as sp
import pickle

from typing import Union, List, Tuple, Optional

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


def diag_dominant_matrix_A_b(m: int) -> Tuple[np.ndarray, np.ndarray]:
    """Funkcja tworząca zestaw składający się z macierzy A (m,m), wektora b (m,) o losowych wartościach całkowitych z przedziału 0, 9
    Macierz A ma być diagonalnie zdominowana, tzn. wyrazy na przekątnej sa wieksze od pozostałych w danej kolumnie i wierszu
    Parameters:
    m int: wymiary macierzy i wektora
    
    Returns:
    Tuple[np.ndarray, np.ndarray]: macierz diagonalnie zdominowana o rozmiarze (m,m) i wektorem (m,)
                                   Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(m,int) and m>0:
       A= np.random.randint(0,8,size=(m,m))
       d=np.diag(A)
       C=A.T
       for i in range(m):
           A[i][i]=9
        
            
       b= np.random.randint(0,9,size=(m))
       return (A,b)
    else : 
        return None   
      


def is_diag_dominant(A: np.ndarray) -> bool:
    """Funkcja sprawdzająca czy macierzy A (m,m) jest diagonalnie zdominowana
    Parameters:
    A np.ndarray: macierz wejściowa
    
    Returns:
    bool: sprawdzenie warunku 
          Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(A,np.ndarray) :
        if len(A.shape) == 2 :
         m,n=A.shape
         if m==n:
                d=np.diag(A)
                for i in range(m):
                    for j in range(m):
                        if A[i][j]>=d[i] or A[i][j]>=d[j]:
                            if(i!=j):
                                return False
                return True
    else :
     return None


def symmetric_matrix_A_b(m: int) -> Tuple[np.ndarray, np.ndarray]:
    """Funkcja tworząca zestaw składający się z macierzy A (m,m), wektora b (m,) o losowych wartościach całkowitych z przedziału 0, 9
    Parameters:
    m int: wymiary macierzy i wektora
    
    Returns:
    Tuple[np.ndarray, np.ndarray]: symetryczną macierz o rozmiarze (m,m) i wektorem (m,)
                                   Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(m,int) and m>0:
        A=np.zeros((m,m))
        for  i in range(m):
            for j in range(i+1):
                A[j][i]=np.random.randint(0,9)
                A[i][j]=A[j][i]
        b= np.random.randint(0,9,size=(m))
        return (A,b)
    else: 
        return None  


def is_symmetric(A: np.ndarray) -> bool:
    """Funkcja sprawdzająca czy macierzy A (m,m) jest symetryczna
    Parameters:
    A np.ndarray: macierz wejściowa
    
    Returns:
    bool: sprawdzenie warunku 
          Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(A,np.ndarray) :
        if len(A.shape) == 2 :
            s,k=A.shape
            if s==k:
                for  i in range(s):
                    for j in range(i):
                        if A[i][j]!=A[j][i]:
                            return False
                return True
            else:
                return None
        else: 
         return None
    else: 
        return None


def solve_jacobi(A: np.ndarray, b: np.ndarray, x_init: np.ndarray,
                 epsilon: Optional[float] = 1e-8, maxiter: Optional[int] = 100) -> Tuple[np.ndarray, int]:
    """Funkcja tworząca zestaw składający się z macierzy A (m,m), wektora b (m,) o losowych wartościach całkowitych
    Parameters:
    A np.ndarray: macierz współczynników
    b np.ndarray: wektor wartości prawej strony układu
    x_init np.ndarray: rozwiązanie początkowe
    epsilon Optional[float]: zadana dokładność
    maxiter Optional[int]: ograniczenie iteracji
    
    Returns:
    np.ndarray: przybliżone rozwiązanie (m,)
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    int: iteracja
    """
    if isinstance(A,np.ndarray) and isinstance(b,np.ndarray) and isinstance(x_init,np.ndarray) and isinstance(epsilon,float) and isinstance(maxiter,int)  :
     if maxiter>0 and epsilon>0 and A.shape[0]==A.shape[1] and b.shape[0]==A.shape[1] and b.shape[0]==x_init.shape[0]:
            D = np.diag(np.diag(A))
            LU = A - D
            x = x_init
            D_inv = np.diag(1 / np.diag(D))

            for i in range(maxiter):
                x_new = np.dot(D_inv, b - np.dot(LU, x))
                       
                if np.linalg.norm(x_new - x) < epsilon:
                    return x_new, i
                x = x_new
            return x, maxiter
     else:
         return None
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