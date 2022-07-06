
import unittest

from numpy import array

from atack_sus_decayed import *


class test_attack_sus_decayed(unittest.TestCase):
    
    def test_linear(self):
        """
        test if attack value is 0.
        """
        t=8
        ta=0
        with self.assertRaises(ZeroDivisionError):
            fa= t/ ta
            return fa


    def test_constant(self):
        """ 
        test if constant function assert a Value Error
        """
        t=np.array([])
        try:
            fs = np.ones_like(t)
            return fs
        except:
            self.assertRaises(ValueError,t)

    def test_invlinear(self):
        """ 
        test if invlinear function assert a Value Error

        """
        t=np.array([1,2,3,4,5])
        t_sd=4
        try:
            for i in t:
                    ft = 1 - i / t_sd
                    if ft<0:
                        ft=0
        except:
            self.assertRaises(ValueError)

    def test_sin(self):
        """
        Test if sin function assert a Value Error
        """
        t=np.array([1,2,3,4,5])
        try:
            a = self.list_func[1][1]
            f = self.list_func[1][2]
            ft = 1 * a * np.sin(f * t)
            return ft
        except:
            self.assertRaises(ValueError)

    def test_exp(self):
        """ 
        test if exp function assert a Value Error.
        
        """
        t=np.array([1,2,3,4,5])
        t0=4
        try:
            t0 = self.list_func[0][1]
            ft = 2.71 ** (5 * (t -t0) / t0)
            return ft
        except:
            self.assertRaises(ValueError)

    def test_invexp(self):
        """
        test if invexp function assert a Value Error.

        """
        t=np.array([1,2,3,4,5])
        t_sd=5
        try:
            ft = 2.71 ** ((-5 * t)/t_sd)
            return ft
        except:
            self.assertRaises(ValueError)

    def test_quartcos(self):
        """
        Test if quartcos function assert a Value Error.

        """ 
        t=np.array([1,2,3,4,5])
        t_sd=5
        try:
            ft = np.cos((np.pi * t) / (2 * t_sd))
            return ft
        except:
            self.assertRaises(ValueError)

    
    def test_quartsin(self):
        """
        Test if quartsin function assert a Value Error.

        """
        t=np.array([1,2,3,4,5])
        t0=6
        try:
            ft = np.sin((np.pi * t) / (2 * t0))
            return ft
        except:
            self.assertRaises(ValueError)

    def test_halfcos(self):
        """
        Test if halfcos function assert a Value Error.

        """
        t=np.array([1,2,3,4,5])
        t_sd=6
        try:
            ft = (1 + np.cos((np.pi * t) / t_sd)) / 2
            return ft
        except:
            self.assertRaises(ValueError)

    def test_halfsin(self):
        """

        Test if halfsin function assert a Value Error.

        """
        t=np.array([1,2,3,4,5])
        t0=6
        try:
            ft = (1 + np.cos(np.pi * (t / t0 - 0.5))) / 2
            return ft
        except:
            self.assertRaises(ValueError)


    def test_loge(self):
        """ 
        Test if log function assert a Value Error.
        """
        t0=4
        t=np.array([1,2,3,4,5])
        try:
            list_new = []
            for element in t:
                ft = log((((9 * element) / t0) + 10),10)
                list_new.append(ft)
            list_new = np.array(list_new)
            return list_new
        except:
            self.assertRaises(ValueError)

    def test_pulses(self):
        """
        Test that pulses function assert a Value Error.

        """
        try:
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
        except:
            self.assertRaises(ValueError)

    def test_minor_values(self):
        """
        Test that the minor values are correctly calculate.
        """
        t=np.array([1,2,3,4])
        try:
            ta = self.list_func[0][1]
            ata = np.where(t<=ta)
            return ata
        except:
            self.assertRaises(ValueError)

    def test_medium_values(self):
        """
        Test that the medium values are correctly calculate.
        """
        t=np.array([1,2,3,4])
        try:
            ta = self.list_func[0][1]
            td = self.list_func[2][1]
            sust = np.where((ta<t) & (t<td))
            return sust
        except:
            self.assertRaises(ValueError)

    def test_bigger_values(self):
        """
        test that the bigger values are correctly calculate.

        """
        t=np.array([1,2,3,4])
        try:
            td = self.list_func[2][1]
            ata = np.where(t>=td)
            return ata
        except:
            self.assertRaises(ValueError)
            











                


if __name__ == "__main__":
    unittest.main()
