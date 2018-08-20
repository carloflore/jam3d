#!/usr/bin/env python
import sys
import os
import numpy as np
from tools.tools import load_config
from qcdlib.tmdlib import PDF, PPDF, FF
from qcdlib.tmdlib import TRANSVERSITY
from qcdlib.tmdlib import BOERMULDERS
from qcdlib.tmdlib import SIVERS
from qcdlib.tmdlib import PRETZELOSITY
from qcdlib.tmdlib import COLLINS
from qcdlib.tmdlib import WORMGEARG
from qcdlib.tmdlib import WORMGEARH
from qcdlib.aux import AUX
from tools.config import conf

class STFUNCS:

    def __init__(self):
        self.aux = conf['aux']
        eu2, ed2 = 4 / 9., 1 / 9.
        self.e2 = []
        self.e2.append(0)   # g
        self.e2.append(eu2)  # u
        self.e2.append(eu2)  # ub
        self.e2.append(ed2)  # d
        self.e2.append(ed2)  # db
        self.e2.append(ed2)  # s
        self.e2.append(ed2)  # sb
        self.e2.append(0)   # c
        self.e2.append(0)   # cb
        self.e2.append(0)   # b
        self.e2.append(0)   # bb
        self.e2 = np.array(self.e2)

        self.Mh = {}
        self.Mh['pi+'] = self.aux.Mpi
        self.Mh['pi-'] = self.aux.Mpi
        self.Mh['k+'] = self.aux.Mk
        self.Mh['k-'] = self.aux.Mk

        self.D = {}
        self.D[1] = {'k1': 'pdf', 'k2': 'ff'}
        self.D[2] = {'k1': None, 'k2': None}
        self.D[3] = {'k1': 'ppdf', 'k2': 'ff'}
        self.D[4] = {'k1': 'transversity', 'k2': 'collins'}
        self.D[5] = {'k1': 'sivers', 'k2': 'ff'}
        self.D[6] = {'k1': None, 'k2': None}
        self.D[7] = {'k1': 'boermulders', 'k2': 'collins'}
        self.D[8] = {'k1': 'pretzelosity', 'k2': 'collins'}
        self.D[9] = {'k1': 'wormgearg', 'k2': 'ff'}
        self.D[10] = {'k1': 'wormgearh', 'k2': 'collins'}
        self.D[11] = {'k1': 'wormgearg', 'k2': 'ff'}
        self.D[12] = {'k1': 'ppdf', 'k2': 'ff'}
        self.D[13] = {'k1': 'wormgearg', 'k2': 'ff'}
        self.D[14] = {'k1': 'wormgearh', 'k2': 'collins'}
        self.D[15] = {'k1': None, 'k2': None}
        self.D[16] = {'k1': 'boermulders', 'k2': 'collins'}
        self.D[17] = {'k1': 'pdf', 'k2': 'ff'}
        self.D[18] = {'k1': 'sivers', 'k2': 'ff'}
        self.D[19] = {'k1': 'transversity', 'k2': 'collins'}
        self.D[20] = {'k1': 'sivers', 'k2': 'ff'}
        self.D[21] = {'k1': 'pretzelosity', 'k2': 'collins'}
        self.D[22] = {'k1': 'pdf', 'k2': 'ff'}
        # This is for collinear!
        self.D[23] = {'k1': 'transversity', 'k2': 'Htilde'}

        if 'basis' not in conf:
            conf['basis'] = 'default'

    def get_K(self, i, x, Q2, z, pT, wq, k1, k2, target, hadron):
        if i == 1:
            return x
        elif i == 2:
            return 0
        elif i == 3:
            return x
        elif i == 4:
            return 2 * x * z * pT * self.Mh[hadron] / wq
        elif i == 5:
            return -2 * x * z * pT * self.aux.M / wq
        elif i == 6:
            return 0
        elif i == 7:
            return 4 * x * z**2 * self.aux.M * pT**2 * self.Mh[hadron] / wq**2
        elif i == 8:
            return 2 * x * z**3 * pT**3 * self.Mh[hadron] * self.aux.M**2 / wq**3
        elif i == 9:
            return 2 * x * z * self.aux.M * pT / wq
        elif i == 10:
            return 4 * x * z**2 * self.aux.M * pT**2 * self.Mh[hadron] / wq**2
        elif i == 11:
            return -2 * self.aux.M / np.sqrt(Q2) * x * (z**2 * conf[k1].widths[target] * (pT**2 + conf[k2].widths[hadron]) + conf[k2].widths[hadron]**2) / wq**2
        elif i == 12:
            return -2 * x * z * pT * conf[k1].widths[target] / (np.sqrt(Q2) * wq)
        elif i == 13:
            return -2 * x * z**2 * pT**2 * self.aux.M * conf[k1].widths[target] / (np.sqrt(Q2) * wq**2)
        elif i == 14:
            return -8 * self.aux.M**3 / np.sqrt(Q2) * x * (z**2 * conf[k1].widths[target] * (pT**2 - z**2 * conf[k1].widths[target]) + conf[k2].widths[hadron]**2) / wq**3
        elif i == 15:
            return 0
        elif i == 16:
            return -8 * self.aux.M * z * pT * self.Mh[hadron] / np.sqrt(Q2) * x * (conf[k2].widths[hadron]**2 + z**2 * conf[k1].widths[target] * (pT**2 - z**2 * conf[k1].widths[target])) / wq**3
        elif i == 17:
            return -2 * self.aux.M / np.sqrt(Q2) * x * (z * pT / self.aux.M) * conf[k1].widths[target] / wq
        elif i == 18:
            return -2 * self.aux.M / np.sqrt(Q2) * x * (z**2 * conf[k1].widths[target] * (pT**2 + conf[k2].widths[hadron]) + conf[k2].widths[hadron]**2) / wq**2
        elif i == 19:
            return 4 * x * z**2 * self.Mh[hadron] / np.sqrt(Q2) * conf[k1].widths[target] * (-pT**2 + wq) / wq**2
        elif i == 20:
            return -2 * self.aux.M**3 / np.sqrt(Q2) * x * conf[k1].widths[target] / wq**2
        elif i == 21:
            return -8 * self.aux.M**2 * self.Mh[hadron] / np.sqrt(Q2) * x * z**2 * pT**2 / wq**2
        elif i == 22:
            return 2 * x * z**2 * pT**2 / Q2 * conf[k1].widths[target]**2 / wq**2
        elif i == 23:
            return -2.0 * (x / z) * self.Mh[hadron] / np.sqrt(Q2)

    def get_wq(self, z, k1, k2, target, hadron):
        return z**2 * np.abs(conf[k1].widths[target]) + np.abs(conf[k2].widths[hadron])

    def get_gauss(self, z, pT, wq):
        return np.exp(-pT**2 / wq) / (np.pi * wq)

    def combine(self, K, F, D, gauss):
        if conf['basis'] == 'default':
            return np.sum(self.e2 * K * F * D * gauss)
        elif conf['basis'] == 'valence':
            # g  u ub  d db  s sb  c cb  b bb
            # 0  1  2  3  4  5  6  7  8  9 10
            # return np.sum(self.e2*K*F*D*gauss)
            _F = np.copy(F)
            _F[1] -= _F[2]
            _F[3] -= _F[4]
            out = np.sum(self.e2 * _F * D * gauss)
            out += self.e2[1] * _F[2] * D[1] * gauss[2] + \
                self.e2[3] * _F[4] * D[3] * gauss[4]
            out *= K
            return out

    def get_FX(self, i, x, z, Q2, pT, target, hadron, obs=None):
        k1 = self.D[i]['k1']
        k2 = self.D[i]['k2']
        if k1 == None or k2 == None:
            return 0
        mu2 = Q2
        F = conf[k1].get_C(x, mu2, target)
        D = conf[k2].get_C(z, mu2, hadron)
        F[0],D[0]=0,0
        wq = self.get_wq(z, k1, k2, target, hadron)
        if obs == 'AUTsinphiS':
            gauss = 1  # AUTsinphiS is collinear
        else:
            gauss = self.get_gauss(z, pT, wq)
        K = self.get_K(i, x, Q2, z, pT, wq, k1, k2, target, hadron)
        # return np.sum(self.e2*K*F*D*gauss)
        return self.combine(K, F, D, gauss)

    def dcs(self, x, Q2, y, z, pT, sangle, hangle, target, hadron):
        coupling = 1.0 / 137
        p1 = (1.0 - y) / (1.0 - y + y**2 / 2)
        p2 = y * (1.0 - y / 2) / (1.0 - y + y**2 / 2)
        p3 = (2.0 - y) * (math.sqrt(1.0 - y)) / (1.0 - y + y**2 / 2)
        p4 = y * math.sqrt(1.0 - y) / (1.0 - y + y**2 / 2)
        SL = math.cos(sangle)
        ST = math.sin(sangle)
        helicity = 1.0
        factor = coupling**2 / (x * y * Q2) * (1 - y + y**2)
        csleading = factor * (self.get_FX(1, x, z, Q2, pT, target, hadron) + math.cos(2 * hangle) * p1 * self.get_FX(7, x, z, Q2, pT, target, hadron) + SL * math.sin(2 * hangle) * p1 * self.get_FX(10, x, z, Q2, pT, target, hadron) + helicity * SL * p2 * self.get_FX(3, x, z, Q2, pT, target, hadron) + helicity * ST * math.cos(
            hangle - sangle) * p2 * self.get_FX(9, x, z, Q2, pT, target, hadron) + ST * math.sin(hangle - sangle) * self.get_FX(5, x, z, Q2, pT, target, hadron) + ST * math.sin(hangle + sangle) * p1 * self.get_FX(4, x, z, Q2, pT, target, hadron) + ST * math.sin(3 * hangle - sangle) * p1 * self.get_FX(8, x, z, Q2, pT, target, hadron))

        cssubleading = factor * (math.cos(hangle) * p3 * (self.get_FX(16, x, z, Q2, pT, target, hadron) + self.get_FX(17, x, z, Q2, pT, target, hadron)) + helicity * math.sin(hangle) * p4 * self.get_FX(15, x, z, Q2, pT, target, hadron) + SL * math.sin(hangle) * p3 * self.get_FX(14, x, z, Q2, pT, target, hadron) + ST * math.sin(sangle) * p3 * (self.get_FX(18, x, z, Q2, pT, target, hadron) + self.get_FX(19, x, z, Q2, pT, target,
                                                                                                                                                                                                                                                                                                                                                                                   hadron)) + ST * math.sin(2 * hangle - sangle) * p3 * (self.get_FX(20, x, z, Q2, pT, target, hadron) + self.get_FX(21, x, z, Q2, pT, target, hadron)) + helicity * SL * math.cos(hangle) * p4 * self.get_FX(12, x, z, Q2, pT, target, hadron) + helicity * ST * math.cos(sangle) * p4 * self.get_FX(11, x, z, Q2, pT, target, hadron) + helicity * ST * math.cos(2 * hangle - sangle) * p4 * self.get_FX(13, x, z, Q2, pT, target, hadron))

        cstotal = csleading + cssubleading
        return cstotal / (2 * 0.938 * 11.0 * x)

    def unpolarizedCS(self, x, Q2, y, z, pT, sangle, hangle, target, hadron):
        coupling = 1.0 / 137
        p1 = (1.0 - y) / (1.0 - y + y**2 / 2)
        p2 = y * (1.0 - y / 2) / (1.0 - y + y**2 / 2)
        p3 = (2.0 - y) * (math.sqrt(1.0 - y)) / (1.0 - y + y**2 / 2)
        p4 = y * math.sqrt(1.0 - y) / (1.0 - y + y**2 / 2)
        SL = math.cos(sangle)
        ST = math.sin(sangle)
        helicity = 1.0
        factor = coupling**2 / (x * y * Q2) * (1 - y + y**2)
        cs = factor * (self.get_FX(1, x, z, Q2, pT, target, hadron) + math.cos(2 * hangle) * p1 * self.get_FX(7, x, z, Q2, pT, target, hadron) +
                     math.cos(hangle) * p3 * (self.get_FX(16, x, z, Q2, pT, target, hadron) + self.get_FX(17, x, z, Q2, pT, target, hadron)))

        return cs / (2 * 0.938 * 11.0 * x)

    def get_xsec(self, x, z, y, Q2, pT, phi_h, phi_S, Sperp, Spar, le, target, hadron):
        alfa2 = self.aux.alfa**2
        gamma = 2 * self.aux.M * x / np.sqrt(Q2)
        eps = (1 - y - 0.25 * gamma**2 * y**2) / (1 - y + 0.5 * y**2 + 0.25 * gamma**2 * y**2)

        beta = np.zeros(19)
        beta[1] = 1
        #beta[2]  =eps
        #beta[3]  =Spar  * le * np.sqrt(1-eps**2)
        #beta[4]  =Sperp * eps * np.sin(phi_h+phi_S)
        #beta[5]  =Sperp * np.sin(phi_h-phi_S)
        #beta[6]  =Sperp * eps * np.sin(phi_h-phi_S)
        beta[7] = eps * np.cos(2 * phi_h)
        #beta[8]  =Sperp * eps * np.sin(3*phi_h-phi_S)
        #beta[9]  =Sperp * le * np.sqrt(1-eps**2) * np.cos(phi_h-phi_S)
        #beta[10] =Spar  * eps * np.sin(2*phi_h)
        #beta[11] =Sperp * le * np.sqrt(2*eps*(1-eps)) * np.cos(phi_S)
        beta[12] = Spar * le * np.sqrt(2 * eps * (1 - eps)) * np.cos(phi_h)
        #beta[13] =Sperp * le * np.sqrt(2*eps*(1-eps)) * np.cos(2*phi_h-phi_S)
        #beta[14] =Spar  * np.sqrt(2*eps*(1+eps))*np.sin(phi_h)
        #beta[15] =le    * np.sqrt(2*eps*(1-eps))*np.sin(phi_h)
        #beta[16] =np.sqrt(2*eps*(1+eps))*np.cos(phi_h)
        #beta[17] =Sperp * np.sqrt(2*eps*(1+eps))*np.sin(phi_S)
        #beta[18] =Sperp * np.sqrt(2*eps*(1+eps))*np.sin(2*phi_h-phi_S)

        F = np.zeros(19)
        F[1] = self.get_FX(1, x, z, Q2, pT, target, hadron)
        F[7] = self.get_FX(7, x, z, Q2, pT, target, hadron)
        F[12] = self.get_FX(12, x, z, Q2, pT, target, hadron)
        #for i in range(1,16): F[i]=self.get_FX(i,x,z,Q2,pT,target,hadron)
        # F[16]=self.get_FX(16,x,z,Q2,pT,target,hadron)+self.get_FX(17,x,z,Q2,pT,target,hadron)
        # F[17]=self.get_FX(18,x,z,Q2,pT,target,hadron)+self.get_FX(19,x,z,Q2,pT,target,hadron)
        # F[18]=self.get_FX(20,x,z,Q2,pT,target,hadron)+self.get_FX(21,x,z,Q2,pT,target,hadron)

        prefactor = (alfa2 / x / y / Q2) * (y**2 / 2 / (1 - eps))
        xsec = prefactor * np.sum(beta * F)
        if xsec < 0:
            print '\nerr: unphysical xsec\n'
            print 'xsec      = %10.2e' % (xsec)
            print 'prefactor = %10.2e' % (prefactor)
            for i in range(1, 19):
                print '%s i=%2d beta=%10.2e F=%10.2e tot=%10.2e' % (
                    '->', i, beta[i], F[i], beta[i] * F[i])
            sys.exit()

        return xsec

if __name__ == '__main__':

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


    stfuncs = STFUNCS()
    x = 0.25
    z = 0.5
    Q2 = 2.4
    mu2 = 2.0
    E = 11.0
    m = 0.938
    pT = 0.3
    y = Q2 / (2 * m * E * x)
    sangle = np.pi * 0.0
    hangle = np.pi / 2
    target = 'p'
    hadron = 'pi+'
    for i in range(1, 22):
        print i, stfuncs.get_FX(i, x, z, Q2, pT, target, hadron)

