#!/usr/bin/env python
import sys
import os
import numpy as np
import time
from scipy.integrate import quad, fixed_quad
from scipy.special import gamma, psi
from tools.config import conf

class CORE:

    def p2n(self, p):
        return p[[0,3,4,1,2,5,6,7,8,9,10]]

    def charge_conj(self,p):
        return p[[0,2,1,4,3,6,5,8,7,10,9]]

    def get_neutral(self,pp):
        pm=self.charge_conf(pp)
        return 0.5*(pp+pm)

    def pip2piz(self, pip):
        piz = np.copy(pip)
        u = pip[1]
        ub = pip[2]
        d = pip[3]
        db = pip[4]
        piz[1] = 0.5 * (u + ub)
        piz[2] = 0.5 * (u + ub)
        piz[3] = 0.5 * (d + db)
        piz[4] = 0.5 * (d + db)
        return piz

    def beta(self, a, b):
        return gamma(a) * gamma(b) / gamma(a + b)

    def get_s(self,Q2):
        lam2 = conf['lam2']
        Q02  = conf['Q02']
        return np.log(np.log(Q2/lam2)/np.log(Q02/lam2))

    def __get_shape(self,x,p):
        return p[0]*x**p[1]*(1-x)**p[2]*(1+p[3]*x+p[4]*x**2)

    def _get_shape(self,x,p,s):
        N=p[0] + p[5] * s
        a=p[1] + p[6] * s
        b=p[2] + p[7] * s
        c=p[3] + p[8] * s
        d=p[4] + p[9] * s
        n= self.beta(1+a,b+1) + c*self.beta(1+a+1,b + 1) + d*self.beta(1+a+1,b + 1)
        return self.__get_shape(x,[N/n,a,b,c,d])

    def get_shape(self,x,Q2,p1,p2):
        s=self.get_s(Q2)
        shape=self._get_shape(x,p1,s)
        if p2[0]!=0: shape+=self._get_shape(x,p2,s)
        return shape

    def get_collinear(self, x, hadron, Q2):
        N = np.zeros(11)
        for i in range(11): 
            N[i] = self.get_shape(x,Q2,self.shape1[hadron][i],self.shape2[hadron][i])
        return N

    def __get_dshape(self,x,p):
        return p[0]*x**p[1]*(1-x)**p[2]*(p[3]+2*p[4]*x+(1+p[3]*x+p[4]*x**2)*(p[1]/x-p[2]/(1-x)))

    def _get_dshape(self,x,p,s):
        # NS: needs to check normalization 
        N=p[0] + p[5] * s
        a=p[1] + p[6] * s
        b=p[2] + p[7] * s
        c=p[3] + p[8] * s
        d=p[4] + p[9] * s
        n= self.beta(1+a,b+1) + c*self.beta(1+a+1,b + 1) + d*self.beta(1+a+1,b + 1)
        return self.__get_dshape(x,[N/n,a,b,c,d])

    def get_dcollinear(self, x, hadron, Q2):  
        """Derivative of the collinear piece"""
        N = np.zeros(11)
        for i in range(11): N[i] = self.get_dshape(x,self.shape1[hadron][i],self.shape2[hadron][i],Q2)
        return N

    def get_widths(self,Q2,hadron):
        s=self.get_s(Q2)
        return self.widths1[hadron]+s*self.widths2[hadron]

    def get_gauss(self, kT2, hadron):
        w=self.get_width(Q2,hadron)
        return np.exp(-kT2 / s) / np.pi / s

    def get_tmd(self, x, Q2, kT2, hadron):
        C = self.get_C(x, Q2, hadron)
        gauss = self.get_gauss(kT2,Q2, hadron)
        return self.K[hadron] * C * gauss

class PDF(CORE):

    def __init__(self):
        self.aux = conf['aux']
        self.set_default_params()
        self.setup()

    def set_default_params(self):

        self._widths1 = {}
        self._widths1['uv']  = 0.3
        self._widths1['dv']  = 0.3
        self._widths1['sea'] = 0.3

        self._widths2 = {}
        self._widths2['uv']  = 0
        self._widths2['dv']  = 0
        self._widths2['sea'] = 0

        self.widths1 = {}
        self.widths1['p'] = np.ones(11)
        self.widths2 = {}
        self.widths2['p'] = np.ones(11)

        self.K = {}
        self.K['p'] = np.ones(11)
        self.K['n'] = np.ones(11)

    def setup(self):
        for i in range(11):
            if   i == 1: self.widths1['p'][i] = self._widths1['uv']
            elif i == 3: self.widths1['p'][i] = self._widths1['dv']
            else:        self.widths1['p'][i] = self._widths1['sea']
        for i in range(11):
            if   i == 1: self.widths2['p'][i] = self._widths2['uv']
            elif i == 3: self.widths2['p'][i] = self._widths2['dv']
            else:        self.widths2['p'][i] = self._widths2['sea']
        self.widths1['n'] = self.p2n(self.widths1['p'])
        self.widths2['n'] = self.p2n(self.widths2['p'])

    def get_C(self, x, Q2, target='p'):
        C = conf['cpdf'].get_f(x,Q2)
        if target == 'n': C = self.p2n(C)
        return C

    def get_state(self):
        return self.widths1,self,widths2

    def set_state(self, state):
        self.widths1 = state[0]
        self.widths2 = state[1]

class FF(CORE):

    def __init__(self):
        self.aux = conf['aux']
        self.set_default_params()
        self.setup()

    def set_default_params(self):

        self._widths1 = {}
        self._widths1['pi+ fav']   = 0.12
        self._widths1['pi+ unfav'] = 0.12
        self._widths1['h+ fav']    = 0.12
        self._widths1['h+ unfav']  = 0.12
        self._widths1['k+ fav']    = 0.12
        self._widths1['k+ unfav']  = 0.12

        self._widths2 = {}
        self._widths2['pi+ fav']   = 0
        self._widths2['pi+ unfav'] = 0
        self._widths2['h+ fav']    = 0
        self._widths2['h+ unfav']  = 0
        self._widths2['k+ fav']    = 0
        self._widths2['k+ unfav']  = 0

        self.widths1 = {}
        self.widths1['pi+'] = np.ones(11)
        self.widths1['h+']  = np.ones(11)
        self.widths1['k+']  = np.ones(11)

        self.widths2 = {}
        self.widths2['pi+'] = np.ones(11)
        self.widths2['h+']  = np.ones(11)
        self.widths2['k+']  = np.ones(11)

        self.K = {}
        self.K['pi+'] = np.ones(11)
        self.K['pi-'] = np.ones(11)
        self.K['h+']  = np.ones(11)
        self.K['h-']  = np.ones(11)
        self.K['k+']  = np.ones(11)
        self.K['k-']  = np.ones(11)

    def get_K(self, z, hadron):
        return 1.0

    def setup(self):

        for i in range(1, 11):
            if   i == 1: self.widths1['pi+'][i] = self._widths1['pi+ fav']
            elif i == 4: self.widths1['pi+'][i] = self._widths1['pi+ fav']
            else:        self.widths1['pi+'][i] = self._widths1['pi+ unfav']

        for i in range(1, 11):
            if   i == 1: self.widths1['h+'][i] = self._widths1['h+ fav']
            elif i == 4: self.widths1['h+'][i] = self._widths1['h+ fav']
            else:        self.widths1['h+'][i] = self._widths1['h+ unfav']

        for i in range(1, 11):
            if   i == 1: self.widths1['k+'][i] = self._widths1['k+ fav']
            elif i == 6: self.widths1['k+'][i] = self._widths1['k+ fav']
            else:        self.widths1['k+'][i] = self._widths1['k+ unfav']

        for i in range(1, 11):
            if   i == 1: self.widths2['pi+'][i] = self._widths2['pi+ fav']
            elif i == 4: self.widths2['pi+'][i] = self._widths2['pi+ fav']
            else:        self.widths2['pi+'][i] = self._widths2['pi+ unfav']

        for i in range(1, 11):
            if   i == 1: self.widths2['h+'][i] = self._widths2['h+ fav']
            elif i == 4: self.widths2['h+'][i] = self._widths2['h+ fav']
            else:        self.widths2['h+'][i] = self._widths2['h+ unfav']

        for i in range(1, 11):
            if   i == 1: self.widths2['k+'][i] = self._widths2['k+ fav']
            elif i == 6: self.widths2['k+'][i] = self._widths2['k+ fav']
            else:        self.widths2['k+'][i] = self._widths2['k+ unfav']


        self.widths1['pi-'] = self.charge_conj(self.widths1['pi+'])
        self.widths1['h-']  = self.charge_conj(self.widths1['h+'])
        self.widths1['k-']  = self.charge_conj(self.widths1['k+'])

        self.widths2['pi-'] = self.charge_conj(self.widths2['pi+'])
        self.widths2['h-']  = self.charge_conj(self.widths2['h+'])
        self.widths2['k-']  = self.charge_conj(self.widths2['k+'])

    def get_C(self, x, Q2, hadron='pi+'):
        if   hadron=='pi+':  C = conf['cpipff'].get_f(x, Q2)
        elif hadron=='pi-':  C = conf['cpimff'].get_f(x, Q2)
        elif hadron=='k+':   C = conf['cKpff'].get_f(x, Q2)
        elif hadron=='k-':   C = conf['cKmff'].get_f(x, Q2)
        elif hadron=='h+':   C = conf['chpff'].get_f(x, Q2)
        elif hadron=='h-':   C = conf['chmff'].get_f(x, Q2)
        return C

    def get_state(self):
        return self.widths1,self.widths2

    def set_state(self, state):
        self.widths1 = state[0]
        self.widths2 = state[0]

class PPDF(CORE):

    def __init__(self):
        self.aux = conf['aux']
        self.set_default_params()
        self.setup()

    def set_default_params(self):
        self.widths0 = {}
        self.widths0['valence'] = 0.19
        self.widths0['sea'] = 0.19

        self.widths = {}
        self.widths['p'] = np.ones(11)

        self.K = {}
        self.K['p'] = np.ones(11)
        self.K['n'] = np.ones(11)

    def setup(self):
        for i in range(11):
            if i == 1 or i == 3:
                self.widths['p'][i] = self.widths0['valence']
            else:
                self.widths['p'][i] = self.widths0['sea']

        self.widths['n'] = self.p2n(self.widths['p'])

    def get_C(self, x, Q2, target='p'):
        C = conf['cppdf'].get_f(x, Q2)
        if target == 'n': C = self.p2n(C)
        return C

class TRANSVERSITY(CORE):

    def __init__(self):
        self.aux = conf['aux']
        self.set_default_params()
        self.setup()

    def set_default_params(self):

        self.shape1 = {}
        self.shape1['p'] = np.zeros((11, 10))
        self.shape1['p'][1] = [0.46, 0, 1.11, 0, 3.64, 0, 0, 0, 0, 0]  # u
        self.shape1['p'][3] = [-1, 0, 1.11, 0, 3.64, 0, 0, 0, 0, 0]  # d
        self.shape1['p'][2] = [0., 0, 1., 0, 1., 0, 0, 0, 0, 0]  # ub
        self.shape1['p'][4] = [0., 0, 1., 0, 1., 0, 0, 0, 0, 0]  # db
        self.shape1['p'][5] = [0., 0, 1., 0, 1., 0, 0, 0, 0, 0]  # s
        self.shape1['p'][6] = [0., 0, 1., 0, 1., 0, 0, 0, 0, 0]  # sb
        self.shape1['p'][7] = [0., 0, 1., 0, 1., 0, 0, 0, 0, 0]  # c
        self.shape1['p'][8] = [0., 0, 1., 0, 1., 0, 0, 0, 0, 0]  # cb

        self.shape2 = {}
        self.shape2['p'] = np.zeros((11, 10))

        self.widths0 = {}
        self.widths0['valence'] = 0.26
        self.widths0['sea'] = 0.26

        self.widths = {}
        self.widths['p'] = np.ones(11)

    def setup(self):
        for i in range(11):
            if i == 1 or i == 3:  self.widths['p'][i] = self.widths0['valence']
            else:                 self.widths['p'][i] = self.widths0['sea']
        self.shape1['n'] = self.p2n(self.shape1['p'])
        self.shape2['n'] = self.p2n(self.shape2['p'])
        self.widths['n'] = self.p2n(self.widths['p'])

    def get_C(self, x, Q2, target='p'):
        C = self.get_collinear(x, target, Q2)
        if target == 'n': C = self.p2n(C)
        return C

    def get_state(self):
        return (self.widths, self.shape1,self.shape2)

    def set_state(self, state):
        self.widths = state[0]
        self.shape1 = state[1]
        self.shape2 = state[3]

class SIVERS(CORE):

    def __init__(self):
        self.aux = conf['aux']
        self.set_default_params()
        self.setup()

    def set_default_params(self):

        self.shape1 = {}
        self.shape1['p'] = np.zeros((11, 10))
        self.shape1['p'][1] = [0.46, 1.11, 3.64, 0, 0,0,0,0,0,0]
        self.shape1['p'][3] = [-1, 1.11, 3.64, 0, 0,0,0,0,0,0]

        self.shape2 = {}
        self.shape2['p'] = np.zeros((11, 10))

        self.widths0 = {}
        self.widths0['valence'] = 0.26
        self.widths0['sea'] = 0.26

        self.widths = {}
        self.widths['p'] = np.ones(11)

    def setup(self):
        for i in range(11):
            if i == 1 or i == 3:  self.widths['p'][i] = self.widths0['valence']
            else:                 self.widths['p'][i] = self.widths0['sea']
        self.shape1['n'] = self.p2n(self.shape1['p'])
        self.shape2['n'] = self.p2n(self.shape2['p'])
        self.widths['n'] = self.p2n(self.widths['p'])

    def get_C(self, x, Q2, target='p'):
        C = self.get_collinear(x, target, Q2)
        if target == 'n': C = self.p2n(C)
        return C

    def get_state(self):
        return (self.widths, self.shape1,self.shape2)

    def set_state(self, state):
        self.widths = state[0]
        self.shape1 = state[1]
        self.shape2 = state[2]

class BOERMULDERS(CORE):

    def __init__(self):
        self.aux = conf['aux']
        self.set_default_params()
        self.setup()

    def set_default_params(self):

        self.shape1 = {}
        self.shape1['p'] = np.zeros((11, 10))
        self.shape1['p'][1] = [-0.49, 0, 0, 0, 0,0,0,0,0,0]
        self.shape1['p'][3] = [-1.0, 0, 0, 0, 0,0,0,0,0,0]

        self.shape2 = {}
        self.shape2['p'] = np.zeros((11, 10))

        self.widths0 = {}
        self.widths0['valence'] = 0.085
        self.widths0['sea'] = 0.085

        self.widths = {}
        self.widths['p'] = np.ones(11)

        # self.M={}
        # self.M['p']=0.1**0.5
        # self.M['n']=0.1**0.5

        self.K = {}
        # self.norm={}

    def get_K(self, x, hadron):
        return 2 * self.aux.M2 / self.widths[hadron]

    def setup(self):
        for i in range(11):
            if i == 1 or i == 3:  self.widths['p'][i] = self.widths0['valence']
            else:                 self.widths['p'][i] = self.widths0['sea']
        self.shape1['n'] = self.p2n(self.shape1['p'])
        self.shape2['n'] = self.p2n(self.shape2['p'])
        self.widths['n'] = self.p2n(self.widths['p'])
        for hadron in ['p', 'n']:
            # self.norm[hadron]=self.get_norm(hadron)
            self.K[hadron] = self.get_K(1.0, hadron)

    def get_C(self, x, Q2, target='p'):
        C = self.get_collinear(x, target, Q2)
        if target == 'n': C = self.p2n(C)
        return C

class PRETZELOSITY(CORE):

    def __init__(self):
        self.aux = conf['aux']
        self.set_default_params()
        self.setup()

    def set_default_params(self):

        self.shape1 = {}
        self.shape1['p'] = np.zeros((11, 10))
        self.shape1['p'][1] = [1, 2.5, 2, 0, 0,0,0,0,0,0]
        self.shape1['p'][3] = [-1.0, 2.5, 2, 0, 0,0,0,0,0,0]

        self.shape2 = {}
        self.shape2['p'] = np.zeros((11, 10))

        self.widths0 = {}
        self.widths0['valence'] = 0.137
        self.widths0['sea'] = 0.137

        self.widths = {}
        self.widths['p'] = np.ones(11)

        # self.M={}
        # self.M['p']=self.aux.M
        # self.M['n']=self.aux.M

        self.K = {}
        # self.norm={}

    def get_K(self, x, hadron):
        return 2 * self.aux.M2**2 / self.widths[hadron]**2

    def setup(self):
        for i in range(11):
            if i == 1 or i == 3: self.widths['p'][i] = self.widths0['valence']
            else:                self.widths['p'][i] = self.widths0['sea']
        self.shape1['n'] = self.p2n(self.shape1['p'])
        self.shape2['n'] = self.p2n(self.shape2['p'])
        self.widths['n'] = self.p2n(self.widths['p'])
        for hadron in ['p', 'n']:
            self.K[hadron] = self.get_K(1.0, hadron)

    def get_C(self, x, Q2, target='p'):
        C = self.get_collinear(x, target, Q2)
        if target == 'n': C = self.p2n(C)
        return C

class WORMGEARG(CORE):

    def __init__(self):
        self.aux = conf['aux']
        self.set_default_params()
        self.setup()

    def set_default_params(self):
        self.K = {}
        self.K['p'] = np.ones(11)
        self.K['n'] = np.ones(11)

        self.widths0 = {}
        self.widths0['valence'] = 0.19
        self.widths0['sea'] = 0.19

        self.widths = {}
        self.widths['p'] = np.ones(11)

    def setup(self):
        for i in range(11):
            if i == 1 or i == 3: self.widths['p'][i] = self.widths0['valence']
            else:                self.widths['p'][i] = self.widths0['sea']
        self.widths['n'] = self.p2n(self.widths['p'])

    def pol(self, i, x, Q2, target):
        return conf['cppdf'].get_f(x, Q2)[i]

    def get_C(self, x, Q2, target='p'):
        #C = np.array([x*quad(lambda y: self.pol(i,x,Q2,target)/y,x,1)[0] for i in range(11)])
        #C = np.array([x*fixed_quad(np.vectorize(lambda y: self.pol(i,x,Q2,target)/y),x,1)[0] for i in range(11)])
        C = np.zeros(11)
        if target == 'n': C = self.p2n(C)
        return C

class WORMGEARH(CORE):

    def __init__(self):
        self.aux = conf['aux']
        self.set_default_params()
        self.setup()

    def set_default_params(self):
        self.K = {}
        self.K['p'] = np.ones(11)
        self.K['n'] = np.ones(11)

        self.widths0 = {}
        self.widths0['valence'] = 0.25
        self.widths0['sea'] = 0.25

        self.widths = {}
        self.widths['p'] = np.ones(11)

    def setup(self):
        for i in range(11):
            if i == 1 or i == 3: self.widths['p'][i] = self.widths0['valence']
            else:                self.widths['p'][i] = self.widths0['sea']

        self.widths['n'] = self.p2n(self.widths['p'])

    def trans(self, i, x, Q2, target):
        return conf['transversity'].get_C(x, Q2, target)[i]

    def get_C(self, x, Q2, target='p'):
        #C = np.array([x*quad(lambda y: self.trans(i,x,Q2,target)/y,x,1)[0] for i in range(11)])
        #C = np.array([x*fixed_quad(np.vectorize(lambda y: self.trans(i,x,Q2,target)/y),x,1)[0] for i in range(11)])
        C = np.zeros(11)
        if target == 'n': C = self.p2n(C)
        return C

class COLLINS(CORE):

    def __init__(self):
        self.aux = conf['aux']
        self.set_default_params()
        self.setup()

    def set_default_params(self):

        self.Mh = {}
        self.Mh['pi+'] = self.aux.Mpi
        self.Mh['pi-'] = self.aux.Mpi
        self.Mh['pi0'] = self.aux.Mpi
        self.Mh['h+'] = self.aux.Mpi
        self.Mh['h-'] = self.aux.Mpi
        self.Mh['k+'] = self.aux.Mk
        self.Mh['k-'] = self.aux.Mk

        self.widths0 = {}
        self.widths0['pi+ fav'] = 0.11
        self.widths0['pi+ unfav'] = 0.11
        self.widths0['h+ fav'] = 0.11
        self.widths0['h+ unfav'] = 0.11
        self.widths0['k+ fav'] = 0.11
        self.widths0['k+ unfav'] = 0.11

        self.shape1 = {}
        self.shape1['pi+'] = np.zeros((11, 10))
        self.shape1['h+'] = np.zeros((11, 10))
        self.shape1['k+'] = np.zeros((11, 10))

        self.shape2 = {}
        self.shape2['pi+'] = np.zeros((11, 10))
        self.shape2['h+'] = np.zeros((11, 10))
        self.shape2['k+'] = np.zeros((11, 10))

        self.widths = {}
        self.widths['pi+'] = np.ones(11)
        self.widths['h+'] = np.ones(11)
        self.widths['k+'] = np.ones(11)

        self.K = {}
        self.K['pi+'] = np.ones(11)
        self.K['h+'] = np.ones(11)
        self.K['k+'] = np.ones(11)
        self.K['pi-'] = np.ones(11)
        self.K['h-'] = np.ones(11)
        self.K['k-'] = np.ones(11)

        self.norm = {}

    def get_norm(self, hadron):
        # np.sqrt(np.exp(1)/2)*self.widths[hadron]*self.M[hadron]**3/(self.Mh[hadron]*(self.M[hadron]**2+self.widths[hadron])**2)
        return 1

    def get_K(self, z, hadron):
        return 2 * z**2 * self.Mh[hadron]**2 / self.widths[hadron]

    def setup(self):
        # 1,  2,  3,  4,  5,  6,  7,  8,  9, 10
        # u, ub,  d, db,  s, sb,  c, cb,  b, bb
        for i in range(1, 11):
            if i == 1 or i == 4:  self.widths['pi+'][i] = np.copy(self.widths0['pi+ fav'])
            else:                 self.widths['pi+'][i] = np.copy(self.widths0['pi+ unfav'])

        for i in range(1, 11):
            if i == 1 or i == 4:  self.widths['h+'][i] = np.copy(self.widths0['h+ fav'])
            else:                 self.widths['h+'][i] = np.copy(self.widths0['h+ unfav'])

        for i in range(1, 11):
            if i == 1 or i == 6:  self.widths['k+'][i] = np.copy(self.widths0['k+ fav'])
            else:                 self.widths['k+'][i] = np.copy(self.widths0['k+ unfav'])

        self.shape1['pi-'] = self.charge_conj(self.shape1['pi+'])
        self.shape2['pi-'] = self.charge_conj(self.shape2['pi+'])

        self.shape1['h-']  = self.charge_conj(self.shape1['h+'])
        self.shape2['h-']  = self.charge_conj(self.shape2['h+'])

        self.shape1['k-']  = self.charge_conj(self.shape1['k+'])
        self.shape2['k-']  = self.charge_conj(self.shape2['k+'])

        self.widths['pi-'] = self.charge_conj(self.widths['pi+'])
        self.widths['h-']  = self.charge_conj(self.widths['h+'])
        self.widths['k-']  = self.charge_conj(self.widths['k+'])

        for hadron in ['pi+', 'pi-', 'h+', 'h-', 'k+', 'k-']:
            self.norm[hadron] = self.get_norm(hadron)
            self.K[hadron] = self.get_K(1.0, hadron)

    def get_C(self, z, Q2, hadron='pi+'):
        C = self.get_collinear(z, hadron, Q2)
        return C

    def get_dC(self, z, Q2, hadron='pi+'):
        C = self.get_dcollinear(z, hadron, Q2)  # *ff
        return C

    def get_state(self):
        return (self.widths, self.shape1, self.shape2)

    def set_state(self, state):
        self.widths = state[0]
        self.shape1 = state[1]
        self.shape2 = state[2]

class HTILDE(CORE):  # Htilde has same form as Collins

    def __init__(self):
        self.aux = conf['aux']
        self.set_default_params()
        self.setup()

    def set_default_params(self):

        self.Mh = {}
        self.Mh['pi+'] = self.aux.Mpi
        self.Mh['pi-'] = self.aux.Mpi
        self.Mh['pi0'] = self.aux.Mpi
        self.Mh['h+'] = self.aux.Mpi
        self.Mh['h-'] = self.aux.Mpi
        self.Mh['k+'] = self.aux.Mk
        self.Mh['k-'] = self.aux.Mk

        self.widths0 = {}
        self.widths0['pi+ fav'] = 0.11
        self.widths0['pi+ unfav'] = 0.11
        self.widths0['h+ fav'] = 0.11
        self.widths0['h+ unfav'] = 0.11
        self.widths0['k+ fav'] = 0.11
        self.widths0['k+ unfav'] = 0.11

        self.shape1 = {}
        self.shape1['pi+'] = np.zeros((11, 10))
        self.shape1['h+'] = np.zeros((11, 10))
        self.shape1['k+'] = np.zeros((11, 10))

        self.shape2={}
        self.shape2['pi+']=np.zeros((11,10))
        self.shape2['h+']=np.zeros((11,10))
        self.shape2['k+']=np.zeros((11,10))

        self.widths = {}
        self.widths['pi+'] = np.ones(11)
        self.widths['h+'] = np.ones(11)
        self.widths['k+'] = np.ones(11)

        self.K = {}
        self.K['pi+'] = np.ones(11)
        self.K['h+'] = np.ones(11)
        self.K['k+'] = np.ones(11)
        self.K['pi-'] = np.ones(11)
        self.K['h-'] = np.ones(11)
        self.K['k-'] = np.ones(11)

        self.norm = {}

    def get_norm(self, hadron):
        # np.sqrt(np.exp(1)/2)*self.widths[hadron]*self.M[hadron]**3/(self.Mh[hadron]*(self.M[hadron]**2+self.widths[hadron])**2)
        return 1

    def get_K(self, z, hadron):
        return 2 * z**2 * self.Mh[hadron]**2 / self.widths[hadron]

    def setup(self):
        # 1,  2,  3,  4,  5,  6,  7,  8,  9, 10
        # u, ub,  d, db,  s, sb,  c, cb,  b, bb
        for i in range(1, 11):
            if i == 1 or i == 4: self.widths['pi+'][i] = np.copy(self.widths0['pi+ fav'])
            else:                self.widths['pi+'][i] = np.copy(self.widths0['pi+ unfav'])

        for i in range(1, 11):
            if i == 1 or i == 4: self.widths['h+'][i] = np.copy(self.widths0['h+ fav'])
            else:                self.widths['h+'][i] = np.copy(self.widths0['h+ unfav'])

        for i in range(1, 11):
            if i == 1 or i == 6: self.widths['k+'][i] = np.copy(self.widths0['k+ fav'])
            else:                self.widths['k+'][i] = np.copy(self.widths0['k+ unfav'])

        self.shape1['pi-'] = self.charge_conj(self.shape1['pi+'])
        self.shape2['pi-'] = self.charge_conj(self.shape2['pi+'])

        self.shape1['h-']  = self.charge_conj(self.shape1['h+'])
        self.shape2['h-']  = self.charge_conj(self.shape2['h+'])

        self.shape1['k-']  = self.charge_conj(self.shape1['k+'])
        self.shape2['k-']  = self.charge_conj(self.shape2['k+'])

        self.widths['pi-'] = self.charge_conj(self.widths['pi+'])
        self.widths['h-']  = self.charge_conj(self.widths['h+'])
        self.widths['k-']  = self.charge_conj(self.widths['k+'])

        for hadron in ['pi+', 'pi-', 'h+', 'h-', 'k+', 'k-']:
            self.norm[hadron] = self.get_norm(hadron)
            self.K[hadron] = self.get_K(1.0, hadron)

    def get_C(self, z, Q2, hadron='pi+'):
        C = self.get_collinear(z, hadron, Q2)  # *ff
        #if hadron == 'pi0':
        #    C = self.pip2piz(C)  # pi0 only for A_N (collinear)
        return C

    def get_state(self):
        return (self.widths, self.shape1,self.shape2)

    def set_state(self, state):
        self.widths = state[0]
        self.shape1 = state[1]
        self.shape2 = state[2]


if __name__ == '__main__':

    from qcdlib.aux import AUX
    from qcdlib.interpolator import INTERPOLATOR

    conf['aux']    = AUX()
    conf['cpdf']   = INTERPOLATOR('CJ15nlo_0000')
    conf['cppdf']  = INTERPOLATOR('CJ15nlo_0000')
    conf['cpipff'] = INTERPOLATOR('dsspipNLO_0000')
    conf['cpimff'] = INTERPOLATOR('dsspimNLO_0000')
    conf['cKpff']  = INTERPOLATOR('dssKpNLO_0000')
    conf['cKmff']  = INTERPOLATOR('dssKmNLO_0000')

    conf['lam2'] = 0.4 
    conf['Q02']  = 1.0
    conf['pdf']          = PDF()
    conf['ppdf']         = PPDF()
    conf['ff']           = FF()
    conf['transversity'] = TRANSVERSITY()
    conf['sivers']       = SIVERS()
    conf['boermulders']  = BOERMULDERS()
    conf['pretzelosity'] = PRETZELOSITY()
    conf['wormgearg']    = WORMGEARG()
    conf['wormgearh']    = WORMGEARH()
    conf['collins']      = COLLINS()
    #conf['dcollinsdz']   = DCOLLINSDZ()
    #conf['Htilde']       = HTILDE()


    x = 0.15
    Q2 = 2.4
    dist = []
    dist.append('pdf')
    dist.append('ff')
    #dist.append('ppdf')
    #dist.append('transversity')
    #dist.append('sivers')
    #dist.append('boermulders')
    #dist.append('pretzelosity')
    #dist.append('wormgearg')
    #dist.append('wormgearh')
    #dist.append('collins')
    #dist.append('dcollinsdz')
    #dist.append('Htilde')

    
    for k in dist:
        print k
        print conf[k].get_C(x, Q2)
















