from tkinter import S
import numpy as np
from math import log
import matplotlib.pyplot as plt

def atack (t):
    """
    Function that executes the attack of the note.
    Parameters:
    ----------
        t -> Linspace element
        ta:float -> Attack time
    Return:
        ta:float -> Attack value
    """
    ta = 0.02
    fa = t / ta
    #fa = np.sin((np.pi * lista) / (2 * t0))
    return fa

def sost (t):
    """
    Function that will return the value of the sharp.
    Parameters:
    ----------
        t -> Linspace element
    Return:
        fs:float -> Support Value
    """
    f = np.ones_like(t)
    return f

def decay (t):
    t0 = 0.06
    lista = []
    for i in t:
        ft = 1 - i / t0
        if ft < 0:
            ft = 0
        lista.append(ft)
    lista = np.array(lista)
    return lista

def condi_menor(t,ta):
    ata = np.where(t<=ta)
    return ata

def condi_medio(t,ta,td):
    sos = np.where((ta<t) & (t<td))
    return sos

def condi_mayor(t,td):
    ata = np.where(t>=td)
    return ata

def funcion (t,wave,ta,td):
    """
    lista_sos = []
    for element_t in t:
        if element_t > ta:
            if element_t < td: 
                lista_sos.append(element_t)
    arrat_sos = np.array(lista_sos)
    """
    #print(t)
    ata = condi_menor(t,ta)
    sos = condi_medio(t,ta,td)
    dec = condi_mayor(t,td)
    #print(sos[-1][-1])
    #print(dec[-1][-1])
    s = sost(t[0:sos[-1][-1]])
    s = s[-1]
    m = np.concatenate((atack(t[0:ata[-1][-1]]),sost(t[0:sos[-1][-1]]),decay(t[0:dec[-1][-1]]) * s,))
    """
    m[0:ata[-1][-1]] = atack(t[0:ata[-1][-1]])

    m[0:sos[-1][-1]] = sost(t[0:sos[-1][-1]])
    m[0:dec[-1][-1]] = decay(t[0:dec[-1][-1]]) * s
    """
    
    wav1 = wave * m[0:len(wave)]
    """
    plt.plot(wav1, color = 'k', label = 'Frecuencia de notas hz')
    plt.title('Simulacro de notas')
    plt.xlabel('Hz')
    plt.ylabel('Variacion')
    plt.legend(loc=3)
    plt.show()
    """
    return wav1

def sin(f,a):
    ft = 1 * a * np.sin(ft)
    return ft

    """
    plt.plot(m[:1000], color = 'k', label = 'Frecuencia de notas hz')
    plt.title('Simulacro de notas')
    plt.xlabel('Hz')
    plt.ylabel('Variacion')
    plt.legend(loc=3)
    plt.show()

    plt.plot(t[:1000], color = 'k', label = 'Frecuencia de notas hz')
    plt.title('Simulacro de notas')
    plt.xlabel('Hz')
    plt.ylabel('Variacion')
    plt.legend(loc=3)
    plt.show()
    """

def exp (t,t0):
    ft = 2.71 ** (5 * (t -t0) / t0)
    return ft

def invexp (t,t0):
    ft = 2.71 ** ((-5 * t) / t0)
    return ft

def quartcos (t,t0):
    ft = np.cos((np.pi * t) / (2 * t0))
    return ft

def quartsin (t,t0):
    ft = np.sin((np.pi * t) / (2 * t0))
    return ft

def halfcos (t,t0):
    ft = (1 + np.cos((np.pi * t) / t0)) / 2
    return ft

def halfsin (t,t0):
    ft = (1 + np.cos(np.pi * (t / t0 - 0.5))) / 2
    return ft

def loge (t,t0):
    ft = log(((9 * t) / t0) + 10,10)
    return ft

def invlog (t,t0):
    if t < t0:
        ft = log(((-9 * t) / t0) + 10,10)
    elif t >= t0:
        ft = 0
    return ft

def tri (t,t1,t0,a):
    if t < t1:
        ft = (t * a) / t1
    elif t > t1:
        ft = ((t - t1) / (t1 - t0)) + a
    return ft

def pulses (t,t1,t0,a):
    """
    Que es el [t / t0]
    """
    td = (t / t0)
    ft = ((1 - a) / t1) * (td - t0 + t1)
    if ft < 0:
        ft = -1 * ft
    ft = + ft + a
    return ft

    return ft



def m_t(t,ta,td):
    """
    Function that filters the element of the linspace to execute the attack, sustain or decay.
    Parameters:
    ----------
        t -> inspace element
        ta:float -> Attack time
    Return:
        mt:float -> Transformed value of attack, sustain and decay 
    """
    if t < ta:
        mt = atack(t,ta)
        #print(mt)
    elif ta < t < td:
        mt = sost(t)
        #print(mt)
    elif td > t:
        mt = decaimiento(t,td)
        #print(mt)
    else:
        mt = 0.7
    return mt

def recor (t,conta):
    """
    Function that will return the element of t depending on the conta (counter).
    Parameters:
    ----------
        t -> Inspace element
        conta:int -> Counter
    Return:
        t -> Element of t
    """
    t = t[conta]
    return t

def decaimiento (t,td):
    """
    Function that will return the value of the decay.
    Parameters:
    ----------
        t -> Linspace element
        td:float -> Decay time
    Return:
        fd:float -> Decay value
    """
    fd = 1 - (t / td)
    if fd < 0:
        fd = 0.7
    return fd