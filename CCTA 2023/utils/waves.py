from lib2to3.pygram import Symbols
from math import inf
import sympy as sym
from sympy import *
import numpy as np
import copy


t_sym = Symbol('t')
A , D , F = symbols('A,D,F')

class Wave():    
    def __init__(self,_name="null",_fnc = t_sym,x=t_sym,arg=(t_sym)):
        self.t_limits = (-inf,inf)
        self.name = _name
        self._fnc0 = _fnc
        self._arg = arg
        self.x = x
        self.reset()      
        self.set_arguments(self._arg)  


    def set_arguments(self,arg):
        self.arg = arg
        full_args = (self.x,*self.arg)
        self.lambda_y    = lambdify(full_args,self.fnc)
        self.lambda_yd  = lambdify(full_args,self.fnc_d)
        self.lambda_ydd = lambdify(full_args,self.fnc_dd)
    
    def reset(self):
        self._fnc  = self._fnc0
        self.fnc = self._fnc(t_sym)
        self.fnc_d = diff(self.fnc,t_sym)
        self.fnc_dd = diff(self.fnc_d,t_sym)       

    def set_limits(self,arg):
        self.t_limits = arg


    def set_constants(self,*arg):
        self.fnc = self.fnc.subs(arg)
        self.fnc_d = diff(self.fnc,t_sym)
        self.fnc_dd = diff(self.fnc_d,t_sym)  

        self.set_arguments(())  


    def isActive(self,t):
        if(t>=self.t_limits[0] and t<=self.t_limits[1]):
            return true
        return false

    def y(self,*arg):
        if len(arg)==1:
            arg = (arg[0],*self.arg)

        if self.isActive(arg[0]):
            return self.lambda_y(*arg)
        else:
            return 0
    
    def yd(self,*arg):
        if self.isActive(arg[0]):
            return self.lambda_yd(*arg)
        else:
            return 0
    
    def ydd(self,*arg):
        if self.isActive(arg[0]):
            return self.lambda_ydd(*arg)
        else:
            return 0

    def print(self):
        print("WAVE 3")
        print(self.name)


WAVES = {}
WAVES["SIN"] = Wave("sin",lambda t_sym:A*sin(2*np.pi*t_sym*F+D),t_sym,(A,F,D))
WAVES["SIN"].set_arguments((A,F,D))
# WAVES["SIN"].set_constants((A,2),(F,1),(D,0))


def cloneWave(wave):
    return copy.copy(WAVES["SIN"])










