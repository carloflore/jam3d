#!/usr/bin/env python
import sys
import os
import numpy as np
from scipy.integrate import quad
from external.DSSLIB.DSS import DSS
from qcdlib.tmdlib import FF
from qcdlib.tmdlib import COLLINS
from qcdlib.aux import AUX
from tools.residuals import _RESIDUALS
from reader import READER
from stfuncs import STFUNCS
from tools.config import conf


class RESIDUALS(_RESIDUALS):

    def __init__(self):
        self.reaction = 'sia'
        self.tabs = conf['sia tabs']
        self.stfuncs = conf['sia stfuncs']
        self.setup()

    def _get_theory(self, entry):
        k, i = entry
        obs = self.tabs[k]['obs'][i].strip()
        col = self.tabs[k]['col'][i].strip()
        z1 = self.tabs[k]['z1'][i]
        z2 = self.tabs[k]['z2'][i]
        Q2 = self.tabs[k]['Q2'][i]
        factor = self.tabs[k]['S2/1+C2'][i]

        if obs == 'AUL-0-PT':
            pT = self.tabs[k]['pT'][i]
            h1 = self.tabs[k]['hadron1'][i]
            h2 = self.tabs[k]['hadron2'][i]
            ZUuu = self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLuu = self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            ZUcol = self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLcol = self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            thy = factor * (ZUcol / ZUuu - ZLcol / ZLuu)
        elif obs == 'AUC-0-PT':
            pT = self.tabs[k]['pT'][i]
            h1 = self.tabs[k]['hadron1'][i]
            h2 = self.tabs[k]['hadron2'][i]
            ZUuu = self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLuu = self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            ZUcol = self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLcol = self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            ZCuu = ZUuu + ZLuu
            ZCcol = ZUcol + ZLcol
            thy = factor * (ZUcol / ZUuu - ZCcol / ZCuu)
        elif obs == 'AUL-0-PT-INT':
            #if self.tabs[k]['col'][i]=='BaBaR': pT = self.tabs[k]['pT'][i]
            #if self.tabs[k]['col'][i]=='belle': pT = None
            pT = None
            h1 = self.tabs[k]['hadron1'][i]
            h2 = self.tabs[k]['hadron2'][i]
            ZUuu = self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLuu = self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            ZUcol = self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLcol = self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            thy = factor * (ZUcol / ZUuu - ZLcol / ZLuu)
        elif obs == 'AUC-0-PT-INT':
            #if self.tabs[k]['col'][i]=='BaBaR': pT = self.tabs[k]['pT'][i]
            #if self.tabs[k]['col'][i]=='belle': pT = None
            pT = None
            h1 = self.tabs[k]['hadron1'][i]
            h2 = self.tabs[k]['hadron2'][i]
            ZUuu = self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLuu = self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                self.stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            ZUcol = self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLcol = self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                self.stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            ZCuu = ZUuu + ZLuu
            ZCcol = ZUcol + ZLcol
            thy = factor * (ZUcol / ZUuu - ZCcol / ZCuu)

        else:
            print 'ERR: obs=%s  not implemented' % obs
            sys.exit()

        if not col == 'BESIII':
            thy = thy * 100.  # from obs to %

        return k, i, thy

    def gen_report(self, verb=1, level=1):
        """
        verb = 0: Do not print on screen. Only return list of strings
        verv = 1: print on screen the report
        level= 0: only the total chi2s
        level= 1: include point by point 
        """

        L = []

        L.append('reaction: %s' % self.reaction)

        for k in self.tabs:
            if len(self.tabs[k]['value']) == 0:
                continue
            res = self._get_residuals(k)
            rres = self._get_rres(k)
            nres = self._get_nres(k)

            chi2 = np.sum(res**2)
            rchi2 = np.sum(rres**2)
            nchi2 = nres**2
            col = self.tabs[k]['col'][0].split()[0]
            npts = res.size
            L.append('%7d %10s %5d %10.2f %10.2f %10.2f' %
                     (k, col, npts, chi2, rchi2, nchi2))

        if level == 1:
            L.append('-' * 100)

            msg = 'col=%7s  '
            msg += 'obs=%7s  '
            msg += 'z1=%10.3e  '
            msg += 'z2=%10.3e  '
            msg += 'Q2=%10.3e  '
            msg += 'exp=%10.3e  '
            msg += 'alpha=%10.3e  '
            msg += 'thy=%10.3e  '
            msg += 'shift=%10.3e  '
            msg += 'chi2=%10.3f  '

            for k in self.tabs:
                if len(self.tabs[k]['value']) == 0:
                    continue
                for i in range(len(self.tabs[k]['value'])):
                    z1 = self.tabs[k]['z1'][i]
                    z2 = self.tabs[k]['z2'][i]
                    Q2 = self.tabs[k]['Q2'][i]
                    res = self.tabs[k]['residuals'][i]
                    thy = self.tabs[k]['thy'][i]
                    exp = self.tabs[k]['value'][i]
                    alpha = self.tabs[k]['alpha'][i]
                    rres = self.tabs[k]['r-residuals'][i]
                    col = self.tabs[k]['col'][i]
                    obs = self.tabs[k]['obs'][i]
                    shift = self.tabs[k]['shift'][i]
                    if res < 0:
                        chi2 = -res**2
                    else:
                        chi2 = res**2
                    L.append(msg % (col, obs, z1, z2, Q2,
                                    exp, alpha, thy, shift, chi2))

        if verb == 0:
            return L
        elif verb == 1:
            for l in L:
                print l


if __name__ == '__main__':

    conf['aux'] = AUX()
    conf['path2DSS'] = '../../external/DSSLIB'
    conf['_ff'] = DSS()
    conf['ff'] = FF()
    conf['collins'] = COLLINS()
    conf['sia stfuncs'] = STFUNCS()

    conf['datasets'] = {}
    conf['datasets']['sia'] = {}
    conf['datasets']['sia']['xlsx'] = {}
    # babar      | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
    conf['datasets']['sia']['xlsx'][1000] = '../../database/sia/expdata/1000.xlsx'
    # babar      | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
    conf['datasets']['sia']['xlsx'][1001] = '../../database/sia/expdata/1001.xlsx'
    # conf['datasets']['sia']['xlsx'][1002]='../database/sia/expdata/1002.xlsx'  #   babar      | pi,pi | AUC-0     | 36     | z1,z2      |
    # conf['datasets']['sia']['xlsx'][1003]='../database/sia/expdata/1003.xlsx'  #   babar      | pi,pi | AUL-0     | 36     | z1,z2      |
    # conf['datasets']['sia']['xlsx'][1004]='../database/sia/expdata/1004.xlsx'  #   belle      | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
    # conf['datasets']['sia']['xlsx'][1005]='../database/sia/expdata/1005.xlsx'  #   belle      | pi,pi | AUT-0     | 16     | z1,z2,qT   |
    conf['datasets']['sia']['norm'] = {}
    conf['datasets']['sia']['norm'][1000] = {'value': 1, 'fixed': False}
    conf['datasets']['sia']['norm'][1001] = {'value': 1, 'fixed': False}
    # conf['datasets']['sia']['norm'][1002]={'value':1,'fixed':False}
    # conf['datasets']['sia']['norm'][1003]={'value':1,'fixed':False}
    # conf['datasets']['sia']['norm'][1004]={'value':1,'fixed':False}
    # conf['datasets']['sia']['norm'][1005]={'value':1,'fixed':False}

    # conf['datasets']['sia']['filters']=[]
    # conf['datasets']['sia']['filters'].append("z<0.6")
    # conf['datasets']['sia']['filters'].append("Q2>1.69")
    #conf['datasets']['sia']['filters'].append("pT>0.2 and pT<0.8")
    conf['sia tabs'] = READER().load_data_sets('sia')
    conf['residuals'] = RESIDUALS()
    conf['residuals'].get_residuals()
    conf['residuals'].gen_report(verb=1, level=1)
