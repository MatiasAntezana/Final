from tkinter import S
import numpy as np
from math import log
import matplotlib.pyplot as plt
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
    def __init__(self,type_function,function_values,ta,td):
        """
        Constructor of the sound class, the attack, sustain and decay.
        """
        self.type_function = type_function
        self.function_values = function_values
        self.ta = ta
        self.td = td
    
    def linear (self,t):
        """
        Executes the attack of the note.
        Arguments:
        ----------
            t:array -> Array of numbers in an interval
        Return:
            ta:float -> Attack value
        """
        fa = t / self.ta
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

    def invlinear (self,t):
        """
        Execute the decay returning an array.
        Arguments:
        ----------
            t:array -> Array of numbers in an interval
        Return:
            array_decay:array -> Array of elements of t (composing the decay)
        """
        array_decay = []
        for i in t:
            ft = 1 - i / self.td
            if ft < 0:
                ft = 0
            array_decay.append(ft)
        array_decay = np.array(array_decay)
        return array_decay

    def tri (self,t,t1,a):
        """
        Run the attack in a different way.
        Arguments:
        ----------
            t:array -> Array of numbers in an interval
            t1:float -> Second attack value
            a:float -> Third attack value
        Return:
            ft:array -> Array of elements of t (composing the attack)

        """
        if t < t1:
            ft = (t * a) / t1
        elif t > t1:
            ft = ((t - t1) / (t1 - self.ta)) + a
        return ft

    def minor_values(self,t):
        """
        Find the t less than or equal to the attack time, returning an array of t that meet the np.where condition.
        Arguments:
        ----------
            t:array -> Array of numbers in an interval
        Return:
            ata:array -> Array of t that meet the condition of np.where
        """
        ata = np.where(t<=self.ta)
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
        sust = np.where((self.ta<t) & (t<self.td))
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
        ata = np.where(t>=self.td)
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
        s = self.constant(t[0:sust[-1][-1]])
        s = s[-1]
        m = np.concatenate((self.linear(t[0:ata[-1][-1]]),self.constant(t[0:sust[-1][-1]]),self.invlinear(t[0:dec[-1][-1]]) * s,))
        """
        m[0:ata[-1][-1]] = atack(t[0:ata[-1][-1]])

        m[0:sust[-1][-1]] = sustt(t[0:sust[-1][-1]])
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

    def sin(self,f,a):
        ft = 1 * a * np.sin(ft)
        return ft

    def exp (self,t,t0):
        ft = 2.71 ** (5 * (t -t0) / t0)
        return ft

    def invexp (self,t,t0):
        ft = 2.71 ** ((-5 * t) / t0)
        return ft

    def quartcos (self,t,t0):
        ft = np.cos((np.pi * t) / (2 * t0))
        return ft

    def quartsin (self,t,t0):
        ft = np.sin((np.pi * t) / (2 * t0))
        return ft

    def halfcos (self,t,t0):
        ft = (1 + np.cos((np.pi * t) / t0)) / 2
        return ft

    def halfsin (self,t,t0):
        ft = (1 + np.cos(np.pi * (t / t0 - 0.5))) / 2
        return ft

    def loge (self,t,t0):
        ft = log(((9 * t) / t0) + 10,10)
        return ft

    def invlog (self,t,t0):
        if t < t0:
            ft = log(((-9 * t) / t0) + 10,10)
        elif t >= t0:
            ft = 0
        return ft

    def tri (self,t,t1,t0,a):
        if t < t1:
            ft = (t * a) / t1
        elif t > t1:
            ft = ((t - t1) / (t1 - t0)) + a
        return ft

    def pulses (self,t,t1,t0,a):
        """
        Que es el [t / t0]
        """
        td = (t / t0)
        ft = ((1 - a) / t1) * (td - t0 + t1)
        if ft < 0:
            ft = -1 * ft
            ft = + ft + a
        return ft