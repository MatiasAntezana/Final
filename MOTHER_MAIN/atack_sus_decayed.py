import numpy as np
from math import log
class Atack_sust_decay:
    """
    Represents the attack, sustain and decay of the note.
    Attributes:
    ----------
        ta:float -> Attack time
        td:float -> Decay time
    
    Methods
    -------
    atack (t):
        Executes the attack of the note.

    sust (t):
        Execute sustain by returning a series of ones.

    decay (t):
        Execute the decay returning an array.
    
    minor_values (t):
        Find the t less than or equal to the attack time, returning an array of t that meet the np.where condition.
    
    medium_values (t):
        Find all t greater than the attack time and less than the decay time.
    
    bigger_values (t):
        Find the elements of t greater than or equal to the decay time.
    
    main_method (t,wave):
        Main method that calls the other methods to execute the attack, sustain, and decay, to return the modified note.

    """
    def __init__(self,list_func):
        """
        Constructor of the sound class, the attack, sustain and decay.
        """
        self.list_func = list_func
    
    def linear (self,t):
        """
        Executes the attack of the note.
        Arguments:
        ----------
            t:array -> Array of numbers in an interval
        Return:
            ta:float -> Attack value
        """
        ta = self.list_func[0][1]
        fa = t / ta
        return fa

    def constant (self,t):
        """
        Execute sustain by returning a series of ones.
        
        Arguments:
        ----------
            t:array -> Array of numbers in an interval
        Return:
            fs:float -> Support Value
        """
        fs = np.ones_like(t)
        return fs

    def invlinear (self,t,condition):
        """
        Execute the decay returning an array.
        Arguments:
        ----------
            t:array -> Array of numbers in an interval
        Return:
            array_decay:array -> Array of elements of t (composing the decay)
        """
        if condition == "s":
            t_sd = self.list_func[1][1]
        elif condition == "d":
            t_sd = self.list_func[2][1]
        array_decay = []
        for i in t:
            ft = 1 - i / t_sd
            if ft < 0:
                ft = 0
            array_decay.append(ft)
        array_decay = np.array(array_decay)
        return array_decay

    def sin(self,t):
        """
        Recreates the sustained of the matrix of t.
        Arguments:
        ---------
            t:array -> Array of numbers in an interval
        Return:
            ft:array -> Sustained value
        """
        a = self.list_func[1][1]
        f = self.list_func[1][2]
        ft = 1 * a * np.sin(f * t)
        return ft
    
    def exp (self,t):
        """
        Recreates the attack of the matrix of t.
        Arguments:
        ---------
            t:array -> Array of numbers in an interval
        Return:
            ft:array -> Attack value
        """
        t0 = self.list_func[0][1]
        ft = 2.71 ** (5 * (t -t0) / t0)
        return ft

    def invexp (self,t,condition):
        """
        Can recreate sustain and decay.
        Arguments:
        ---------
            t:array -> Array of numbers in an interval
            condition:str -> Value that indicates if it is executed for the sustain or for the decay.
        Return:
            ft:array -> Sharp value or decay value
        """
        if condition == "s":
            t_sd = self.list_func[1][1]
        elif condition == "d":
            t_sd = self.list_func[2][1]
        ft = 2.71 ** ((-5 * t)/t_sd)
        return ft

    def quartcos (self,t,condition):
        """
        Can recreate sustain and decay.
        Arguments:
        ---------
            t:array -> Array of numbers in an interval
            condition:str -> Value that indicates if it is executed for the sustain or for the decay
        Return:
            ft:array -> Sharp value or decay value
        """
        if condition == "s":
            t_sd = self.list_func[1][1]
        elif condition == "d":
            t_sd = self.list_func[2][1]
        ft = np.cos((np.pi * t) / (2 * t_sd))
        return ft

    def quartsin (self,t):
        """
        Recreates the attack of the matrix of t.
        Arguments:
        ---------
            t:array -> Array of numbers in an interval
        Return:
            ft:arrat -> Attack value
        """
        t0 = self.list_func[0][1]
        ft = np.sin((np.pi * t) / (2 * t0))
        return ft

    def halfcos (self,t,condition):
        """
        Can recreate sustain and decay.
        Arguments:
        ---------
            t:array -> Array of numbers in an interval
            condition:str -> Value that indicates if it is executed for the sustain or for the decay
        Return:
            ft:array -> Sharp value or decay value
        """
        if condition == "s":
            t_sd = self.list_func[1][1]
        elif condition == "d":
            t_sd = self.list_func[2][1]
        ft = (1 + np.cos((np.pi * t) / t_sd)) / 2
        return ft 

    def halfsin (self,t):
        """
        Recreates the attack of the matrix of t.
        Arguments:
        ---------
            t:array -> Array of numbers in an interval
        Return:
            ft:arrat -> Attack value
        """
        t0 = self.list_func[0][1]
        ft = (1 + np.cos(np.pi * (t / t0 - 0.5))) / 2
        return ft

    def loge (self,t):
        """
        Recreates the attack of the matrix of t.
        Arguments:
        ---------
            t:array -> Array of numbers in an interval
        Return:
            list_new:arrat -> Attack value
        """
        t0 = self.list_func[0][1]
        list_new = []
        for element in t:
            ft = log((((9 * element) / t0) + 10),10)
            list_new.append(ft)
        list_new = np.array(list_new)
        return list_new

    def invlog (self,t,condition):
        """
        Can recreate sustain and decay.
        Arguments:
        ---------
            t:array -> Array of numbers in an interval
            condition:str -> Value that indicates if it is executed for the sustain or for the decay
        Return:
            ft:array -> Sharp value or decay value
        """
        if condition == "s":
            t_sd0 = self.list_func[1][1]
        elif condition == "d":
            t_sd0 = self.list_func[2][1]
        list_new = []
        for element in t:
            if element < t_sd0:
                ft = log(((-9 * element) / t_sd0) + 10,10)
            elif element >= t_sd0:
                ft = 0
            list_new.append(ft)
        list_new = np.array(list_new)
        return list_new

    def pulses (self,t):
        """
        Recreates the sustained of the matrix of t.
        Arguments:
        ---------
            t:array -> Array of numbers in an interval
        Return:
            ft:array -> Sustained value
        """
        t0 = self.list_func[1][1]
        t1 = self.list_func[1][2]
        a = self.list_func[1][3]
        list_new = []
        for element in t:
            td = (element / t0)
            if td < 0:
                td = td * (-1)
            td = (element / t0) - td
            ft = ((1 - a) / t1) * (td - t0 + t1)
            if ft < 0:
                ft = -1 * ft
            ft = ft + a
            list_new.append(ft)
        list_new = np.array(list_new)
        return list_new

    def minor_values(self,t):
        """
        Find the t less than or equal to the attack time, returning an array of t that meet the np.where condition.
        Arguments:
        ----------
            t:array -> Array of numbers in an interval
        Return:
            ata:array -> Array of t that meet the condition of np.where
        """
        ta = self.list_func[0][1]
        ata = np.where(t<=ta)
        return ata

    def medium_values(self,t):
        """
        Find all t greater than the attack time and less than the decay time.
        Arguments:
        ----------
            t:array -> Array of numbers in an interval
        Return:
            sust:array -> Elements of t that meet the condition of np.where
        """
        ta = self.list_func[0][1]
        td = self.list_func[2][1]
        sust = np.where((ta<t) & (t<td))
        return sust

    def bigger_values(self,t):
        """
        Find the elements of t greater than or equal to the decay time.
        Arguments:
        ----------
            t:array -> Array of numbers in an interval
        Return:
            Elements of t that meet the condition of np.where.
        """
        td = self.list_func[2][1]
        ata = np.where(t>=td)
        return ata

    def main_method (self,t,wave):
        """
        Main method that calls the other methods to execute the attack, sustain, and decay, to return the modified note.

        Arguments:
        ----------
            t:array -> Array of numbers in an interval
            wave:array -> Matrix of the np.sin function of a note, including the sum of the harmonics
        Return: 
            wav1:array -> Note modified by attack, sustain and decay
        """
   
        ata = self.minor_values(t)
        sust = self.medium_values(t)
        dec = self.bigger_values(t)
        atack = self.list_func[0][0]
        sust_func = self.list_func[1][0]
        decay_func = self.list_func[2][0]
        if atack == "linear":
            atack_func = self.linear(t[0:ata[-1][-1]])
        elif atack == "exp":
            atack_func = self.exp(t[0:ata[-1][-1]])
        elif atack == "quartsin":
            atack_func = self.quartsin(t[0:ata[-1][-1]])
        elif atack == "halfsin":
            atack_func = self.halfsin(t[0:ata[-1][-1]])
        elif atack == "log":
            atack_func = self.loge(t[0:ata[-1][-1]])
        elif atack == "tri":
            atack_func = self.tri(t[0:ata[-1][-1]])

        if sust_func == "constant":
            sust_fun = self.constant(t[0:sust[-1][-1]])
        elif sust_func == "invlinear":
            sust_fun = self.invlinear(t[0:sust[-1][-1]],"s")
        elif sust_func == "sin":
            sust_fun = self.sin(t[0:sust[-1][-1]])
        elif sust_func == "invexp":
            sust_fun = self.invexp(t[0:sust[-1][-1]],"s")
        elif sust_func == "quartcos":
            sust_fun = self.quartcos(t[0:sust[-1][-1]],"s")
        elif sust_func == "halfcos":
            sust_fun = self.halfcos(t[0:sust[-1][-1]],"s")
        elif sust_func == "invlog":
            sust_fun = self.invlog(t[0:sust[-1][-1]],"s")
        elif sust_func == "pulses":
            sust_fun = self.pulses(t[0:sust[-1][-1]])
        s = sust_fun[-1]
        if decay_func == "invlinear":
            dec_fun = self.invlinear(t[0:dec[-1][-1]],"d")
        elif decay_func == "invexp":
            dec_fun = self.invexp(t[0:dec[-1][-1]],"d")
        elif decay_func == "quartcos":
            dec_fun = self.quartcos(t[0:dec[-1][-1]],"d")
        elif decay_func == "halfcos":
            dec_fun = self.halfcos(t[0:dec[-1][-1]],"d")
        elif decay_func == "invlog":
            dec_fun = self.invlog(t[0:dec[-1][-1]],"d")
        m = np.concatenate((atack_func,sust_fun,dec_fun * s))
        wav1 = wave * m[0:len(wave)]
        return wav1