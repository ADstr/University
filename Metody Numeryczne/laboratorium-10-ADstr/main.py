import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
from numpy.core._multiarray_umath import ndarray
from numpy.polynomial import polynomial as P
import pickle

# zad1
def polly_A(x: np.ndarray):
    """Funkcja wyznaczajaca współczynniki wielomianu przy znanym wektorze pierwiastków.
    Parameters:
    x: wektor pierwiastków
    Results:
    (np.ndarray): wektor współczynników
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None 
    """
    if isinstance(x,np.ndarray):
        return P.polyfromroots(x)
    else:
     return None

def roots_20(a: np.ndarray):
    """Funkcja zaburzająca lekko współczynniki wielomianu na postawie wyznaczonych współczynników wielomianu
        oraz zwracająca dla danych współczynników, miejsca zerowe wielomianu funkcją polyroots.
    Parameters:
    a: wektor współczynników
    Results:
    (np.ndarray, np. ndarray): wektor współczynników i miejsc zerowych w danej pętli
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(a,np.ndarray):
    #  e=np.ndarray([20,20])
    #  r=np.ndarray([20,20])
    #  for j in range(20):
    #     for i in range(len(a)):
    #         e[j][i]=a[i]+1e-10*np.random.random_sample()
    #     r[j]=P.polyroots(e[j])
    #  return e,r
        cop=a
        for i in range(len(a)):
          cop[i]+=1e-10*np.random.random_sample()
        return cop,P.polyroots(cop)
    else:
     return None


# zad 2

def frob_a(wsp: np.ndarray):
    """Funkcja zaburzająca lekko współczynniki wielomianu na postawie wyznaczonych współczynników wielomianu
        oraz zwracająca dla danych współczynników, miejsca zerowe wielomianu funkcją polyroots.
    Parameters:
    a: wektor współczynników
    Results:
    (np.ndarray, np. ndarray, np.ndarray, np. ndarray,): macierz Frobenusa o rozmiarze nxn, gdzie n-1 stopień wielomianu,
    wektor własności własnych, wektor wartości z rozkładu schura, wektor miejsc zerowych otrzymanych za pomocą funkcji polyroots

                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(wsp,np.ndarray):
        m=wsp.shape[0]
        A=np.zeros((m,m))
        for  i in range(m-1):
            A[i][i+1]=1
        for i in range(m):
            A[m-1][i]=-wsp[i]
        return A,np.linalg.eigvals(A),scipy.linalg.schur(A),P.polyroots(wsp)
            

    else:
     return None



