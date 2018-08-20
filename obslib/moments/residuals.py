#!/usr/bin/env python
import sys
import os
import numpy as np
from mpmath import fp, mp
from scipy.integrate import quad
import pandas as pd
import time
from tools.residuals import _RESIDUALS
from reader import READER
from moments import MOMENTS
from qcdlib.tmdlib import PDF, PPDF, FF
from qcdlib.tmdlib import TRANSVERSITY
from qcdlib.tmdlib import BOERMULDERS
from qcdlib.tmdlib import SIVERS
from qcdlib.tmdlib import PRETZELOSITY
from qcdlib.tmdlib import COLLINS
from qcdlib.tmdlib import WORMGEARG
from qcdlib.tmdlib import WORMGEARH
from qcdlib.aux import AUX
from qcdlib.alphaS import ALPHAS
from obslib.idis.stfuncs import STFUNCS as DIS_STFUNCS
from tools.config import conf


class RESIDUALS(_RESIDUALS):

    def __init__(self):
        self.reaction = 'moments'
        self.tabs = conf['moments tabs']
        self.moments = conf['moments']
        self.setup()

    def _get_theory(self, entry):
        k, i = entry
        obs = self.tabs[k]['obs'][i].strip()

        if obs == 'gT':
            thy = self.moments.get_gT()
        elif obs == 'gTu':
            thy = self.moments.get_flav('u')
        elif obs == 'gTd':
            thy = self.moments.get_flav('d')
        elif obs == 'gTs':
            thy = self.moments.get_flav('s')
        elif obs == 'gTc':
            thy = self.moments.get_flav('c')
        elif obs == 'gT(u-d)':
            thy = self.moments.get_gT()
        elif obs == 'gT(u+d)':
            thy = self.moments.get_flav('u') + self.moments.get_flav('d')

        return k, i, thy

    def gen_report(self, verb=1, level=1):
        """
        verb = 0: Do not print on screen. Only return list of strings
        verv = 1: print on screen the report
        level= 0: only the total chi2s
        level= 1: include point by point 
        """

        L = []

        L.append(self.reaction)

        for k in self.tabs:
            print k, len(self.tabs[k]['value'])
            if self.tabs[k]['value'].size == 0:
                continue
            res = self._get_residuals(k)
            rres = self._get_rres(k)
            nres = self._get_nres(k)

            chi2 = np.sum(res**2)
            rchi2 = np.sum(rres**2)
            nchi2 = nres**2
            obs = self.tabs[k]['obs'][0].split()[0]
            npts = res.size
            L.append('%7d %10s %5d %10.2f %10.2f %10.2f' %
                     (k, obs, npts, chi2, rchi2, nchi2))

        if level == 1:
            L.append('-' * 100)

            msg = 'obs=%7s  '
            msg += 'exp=%10.3e  '
            msg += 'dexp=%10.3e  '
            msg += 'thy=%10.3e  '
            msg += 'chi2=%10.3f  '

            for k in self.tabs:
                if len(self.tabs[k]['value']) == 0:
                    continue
                for i in range(len(self.tabs[k]['value'])):
                    obs = self.tabs[k]['obs'][i]
                    res = self.tabs[k]['residuals'][i]
                    thy = self.tabs[k]['thy'][i]
                    exp = self.tabs[k]['value'][i]
                    alpha = self.tabs[k]['alpha'][i]
                    rres = self.tabs[k]['r-residuals'][i]
                    col = self.tabs[k]['col'][i]
                    shift = self.tabs[k]['shift'][i]
                    if res < 0:
                        chi2 = -res**2
                    else:
                        chi2 = res**2
                    L.append(msg % (obs, exp, alpha, thy, chi2))

        if verb == 0:
            return L
        elif verb == 1:
            for l in L:
                print l


if __name__ == '__main__':

    conf['datasets'] = {}
    conf['datasets']['lattice'] = {}
    conf['datasets']['lattice']['xlsx'] = {}
    conf['datasets']['lattice']['norm'] = {}
    # lattice gT(u-d)
    conf['datasets']['lattice']['xlsx'][1000] = '../../database/lattice/1000.xlsx'
    conf['datasets']['lattice']['norm'][1000] = {
        'value': 1, 'fixed': True, 'min': 0, 'max': 2}
    conf['lattice tabs'] = READER(conf).load_data_sets('lattice')

    #####################################################
    conf['path2CJ'] = '../../external/CJLIB'
    conf['path2LSS'] = '../../external/LSSLIB'
    conf['path2DSS'] = '../../external/DSSLIB'

    # setup for inclusive dis
    conf['alphaSmode'] = 'backward'
    conf['Q20'] = 1
    conf['order'] = 'LO'
    conf['aux'] = AUX()
    conf['alphaS'] = ALPHAS(conf)
    conf['pdf-NLO'] = CJ(conf)
    conf['dis stfuncs'] = DIS_STFUNCS(conf)

    # setup tmd sidis
    conf['order'] = 'LO'
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
    conf['moments'] = MOMENTS(conf)
    #####################################################
    conf['residuals'] = RESIDUALS(conf)
    conf['residuals'].get_residuals()
    conf['residuals'].gen_report(verb=1, level=1)
