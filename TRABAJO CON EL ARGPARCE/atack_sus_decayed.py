def atack (t,ta):
    """
    Function that executes the attack of the note.
    Parameters:
    ----------
        t -> Linspace element
        ta:float -> Attack time
    Return:
        ta:float -> Attack value
    """
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
    fs = t * 1
    return fs

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
    print(type(mt))
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