#!/usr/bin/env python
import sys
import os
import numpy as np
import math
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
from scipy.special import gamma
from tools.config import conf


class MOMENTS:

    def __init__(self):
        self.aux = conf['aux']

    def beta(self, a, b):
        return gamma(a) * gamma(b) / gamma(a + b)

    def get_moment(self, p):
        # AP: needs to check normalization
        N=p[0] + p[5] * s
        a=p[1] + p[6] * s
        b=p[2] + p[7] * s
        c=p[3] + p[8] * s
        d=p[4] + p[9] * s
        n= self.beta(1+a,b+1) + c*self.beta(1+a+1,b + 1) + d*self.beta(1+a+1,b + 1)
        return N * (self.beta(1 + a, b + 1) + c * self.beta(1 + 0.5 + a, b + 1) + d * self.beta(1 + 1 + a, b + 1))

    def get_flav(self, flav):
        shape = conf['transversity'].shape1['p']
        if flav == 'u':
            return self.get_moment(shape[1]) - self.get_moment(shape[2])
        if flav == 'd':
            return self.get_moment(shape[3]) - self.get_moment(shape[4])
        # if flav=='uv': return self.get_moment(shape[1])-self.get_moment(shape[2])
        # if flav=='dv': return self.get_moment(shape[3])-self.get_moment(shape[4])
        if flav == 's':
            return self.get_moment(shape[5]) - self.get_moment(shape[6])
        if flav == 'c':
            return self.get_moment(shape[7]) - self.get_moment(shape[8])

    def get_gT(self):
        shape = conf['transversity'].shape1['p']
        # mom_u=self.get_moment(shape[1])
        # mom_d=self.get_moment(shape[3])
        mom_u = self.get_flav('u')
        mom_d = self.get_flav('d')
        return mom_u - mom_d

if __name__ == '__main__':

    conf['path2CJ'] = '../../external/CJLIB'
    conf['path2LSS'] = '../../external/LSSLIB'
    conf['path2DSS'] = '../../external/DSSLIB'

    conf['order'] = 'LO'
    conf['aux'] = AUX()
    conf['_pdf'] = CJ(conf)
    conf['_ppdf'] = LSS(conf)
    conf['_ff'] = DSS(conf)

    conf['pdf'] = PDF(conf)
    conf['ppdf'] = PPDF(conf)
    conf['ff'] = FF(conf)
    conf['transversity'] = TRANSVERSITY(conf)
    conf['sivers'] = SIVERS(conf)
    conf['boermulders'] = BOERMULDERS(conf)
    conf['pretzelosity'] = PRETZELOSITY(conf)
    conf['wormgearg'] = WORMGEARG(conf)
    conf['wormgearh'] = WORMGEARH(conf)
    conf['collins'] = COLLINS(conf)

    mom = MOMENTS(conf)
    print mom.get_gT()
