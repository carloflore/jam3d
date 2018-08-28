#!/usr/bin/env python
import sys
import os
import numpy as np
from tools.residuals import _RESIDUALS
from tools.config import conf

class RESIDUALS(_RESIDUALS):

    def __init__(self):
        self.reaction = 'sidis'
        self.tabs = conf['sidis tabs']
        self.stfuncs = conf['sidis stfuncs']
        self.dis_stfuncs = conf['dis stfuncs']
        self.setup()

    def _get_theory(self, entry):
        k, i = entry
        x = self.tabs[k]['x'][i]
        y = self.tabs[k]['y'][i]
        z = self.tabs[k]['z'][i]
        Q2 = self.tabs[k]['Q2'][i]
        pT = self.tabs[k]['pT'][i]
        target = self.tabs[k]['target'][i]
        hadron = self.tabs[k]['hadron'][i]
        obs = self.tabs[k]['obs'][i].strip()
        col = self.tabs[k]['col'][i].strip().upper()

        if obs == 'xsec':
            phi_h = self.tabs[k]['phi'][i]
            phi_S = 0
            Sperp = 0
            Spar = 0
            le = 0
            thy = self.stfuncs.get_xsec(
                x, z, y, Q2, pT, phi_h, phi_S, Sperp, Spar, le, 'p', hadron)

        elif obs == 'FUU' and target == 'proton':

            FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron, obs)
            thy = FUU

        elif obs == 'M_EIC' and target == 'proton':

            FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron, obs)
            thy = FUU

        elif obs == 'M_Hermes' and target == 'proton':

            FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron, obs)
            F2 = self.dis_stfuncs.get_F2(x, Q2, 'p')
            thy = 2 * np.pi * pT * FUU / F2

        elif obs == 'M_Hermes' and target == 'deuteron':

            FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron, obs)\
                + self.stfuncs.get_FX(1, x, z, Q2, pT, 'n', hadron, obs)

            F2 = self.dis_stfuncs.get_F2(x, Q2, 'p')\
                + self.dis_stfuncs.get_F2(x, Q2, 'n')

            thy = 2 * np.pi * pT * FUU / F2

        elif obs == 'AUTcollins':

            coeff = 1.
            if col == 'HERMES':
                coeff = 1   # hermes is sin(phi_s+phi_h)
            if col == 'COMPASS':
                coeff = -1   # compass is sin(phi_s+phi_h+pi)
            if col == 'HERMES':
                # add depolarization factor only for HERMES
                coeff *= 2 * (1 - y) / (1 + (1 - y)**2)


            if target == 'proton':

                FUT = self.stfuncs.get_FX(4, x, z, Q2, pT, 'p', hadron, obs)
                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron, obs)
                thy = coeff * FUT / FUU

            elif target == 'neutron':

                FUT = self.stfuncs.get_FX(4, x, z, Q2, pT, 'n', hadron, obs)
                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'n', hadron, obs)
                thy = coeff * FUT / FUU

            elif target == 'deuteron':

                FUT = self.stfuncs.get_FX(4, x, z, Q2, pT, 'p', hadron, obs)\
                    + self.stfuncs.get_FX(4, x, z, Q2, pT, 'n', hadron, obs)
                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron, obs)\
                    + self.stfuncs.get_FX(1, x, z, Q2, pT, 'n', hadron, obs)

                thy = coeff * FUT / FUU

        elif obs == 'AUTsivers':


            if target == 'proton':

                FUT = self.stfuncs.get_FX(5, x, z, Q2, pT, 'p', hadron, obs)
                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron, obs)
                thy = FUT / FUU

            elif target == 'neutron':

                FUT = self.stfuncs.get_FX(5, x, z, Q2, pT, 'n', hadron, obs)
                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'n', hadron, obs)
                thy = FUT / FUU

            elif target == 'deuteron':

                FUT = self.stfuncs.get_FX(5, x, z, Q2, pT, 'p', hadron, obs)\
                    + self.stfuncs.get_FX(5, x, z, Q2, pT, 'n', hadron, obs)
                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron, obs)\
                    + self.stfuncs.get_FX(1, x, z, Q2, pT, 'n', hadron, obs)

                thy = FUT / FUU

        elif obs == 'AUUcos':


            if target == 'proton':

                FUUcos = self.stfuncs.get_FX(16, x, z, Q2, pT, 'p', hadron, obs) \
                    + self.stfuncs.get_FX(17, x, z, Q2, pT, 'p', hadron, obs)
                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron, obs)

            elif target == 'neutron':

                FUUcos = self.stfuncs.get_FX(16, x, z, Q2, pT, 'n', hadron, obs) \
                    + self.stfuncs.get_FX(17, x, z, Q2, pT, 'n', hadron, obs)
                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'n', hadron, obs)

            elif target == 'deuteron':

                FUUcos = self.stfuncs.get_FX(16, x, z, Q2, pT, 'p', hadron, obs) \
                    + self.stfuncs.get_FX(17, x, z, Q2, pT, 'p', hadron, obs) \
                    + self.stfuncs.get_FX(16, x, z, Q2, pT, 'n', hadron, obs) \
                    + self.stfuncs.get_FX(17, x, z, Q2, pT, 'n', hadron, obs)

                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron, obs)\
                    + self.stfuncs.get_FX(1, x, z, Q2, pT, 'n', hadron, obs)

            epsilon = (1 - y) / (1 - y + 0.5 * y**2)
            coeff = 1.
            if col == 'HERMES':
                # add depolarization factor for HERMES
                coeff = np.sqrt(2 * epsilon * (1 + epsilon))
            if col == 'COMPASS':
                coeff = 1.
            if col == 'JLAB':
                # add depolarization factor for CLAS
                coeff = np.sqrt(2 * epsilon * (1 + epsilon))

            thy = coeff * FUUcos / FUU

        elif obs == 'AUUcos2':

            if target == 'proton':
                FUUcos2 = self.stfuncs.get_FX(
                    7, x, z, Q2, pT, 'p', hadron, obs)
                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron, obs)

            elif target == 'neutron':

                FUUcos2 = self.stfuncs.get_FX(
                    7, x, z, Q2, pT, 'n', hadron, obs)
                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'n', hadron, obs)

            elif target == 'deuteron':

                FUUcos2 = self.stfuncs.get_FX(7, x, z, Q2, pT, 'p', hadron, obs)\
                    + self.stfuncs.get_FX(7, x, z, Q2, pT, 'n', hadron, obs)

                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron, obs)\
                    + self.stfuncs.get_FX(1, x, z, Q2, pT, 'n', hadron, obs)

            epsilon = (1 - y) / (1 - y + 0.5 * y**2)
            coeff = 1.
            if col == 'HERMES':
                coeff = epsilon  # add depolarization factor for HERMES
            if col == 'COMPASS':
                coeff = 1.
            if col == 'JLAB':
                coeff = epsilon  # add depolarization factor for CLAS

            thy = coeff * FUUcos2 / FUU

        elif obs == 'A_pretzelosity':

            if target == 'proton':
                FUTsin3 = self.stfuncs.get_FX(
                    8, x, z, Q2, pT, 'p', hadron, obs)
                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron, obs)

            elif target == 'neutron':

                FUTsin3 = self.stfuncs.get_FX(
                    8, x, z, Q2, pT, 'n', hadron, obs)
                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'n', hadron, obs)

            elif target == 'deuteron':

                FUTsin3 = self.stfuncs.get_FX(8, x, z, Q2, pT, 'p', hadron, obs)\
                    + self.stfuncs.get_FX(8, x, z, Q2, pT, 'n', hadron, obs)

                FUU = self.stfuncs.get_FX(8, x, z, Q2, pT, 'p', hadron, obs)\
                    + self.stfuncs.get_FX(8, x, z, Q2, pT, 'n', hadron, obs)

            coeff = 1.
            if col == 'HERMES':
                # add depolarization factor for HERMES
                coeff = 2 * (1 - y) / (1 + (1 - y)**2)
            if col == 'COMPASS':
                coeff = 1.
            if col == 'JLAB':
                # add depolarization factor for CLAS
                coeff = 2 * (1 - y) / (1 + (1 - y)**2)

            thy = coeff * FUTsin3 / FUU

        elif obs == 'ALL':

            if target == 'proton':
                FLL = self.stfuncs.get_FX(3, x, z, Q2, pT, 'p', hadron, obs)
                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron, obs)

            coeff = 1.
            if col == 'HERMES':
                # add depolarization factor for HERMES
                coeff = y * (2 - y) / (1 + (1 - y)**2)
            if col == 'COMPASS':
                coeff = 1.
            if col == 'CLAS':
                # add depolarization factor for CLAS
                coeff = y * (2 - y) / (1 + (1 - y)**2)

            thy = coeff * FLL / FUU

        elif obs == 'AUTsinphiS':  # This is for collinear!

            if target == 'proton':
                FUTsinphiS = self.stfuncs.get_FX(
                    23, x, z, Q2, pT, 'p', hadron, obs)
                FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron, obs)

            coeff = 1.
            if col == 'HERMES':
                # add depolarization factor for HERMES
                coeff = np.sqrt(1.0 - y) * (2 - y) / (1 - y + 0.5 * y**2)
            if col == 'COMPASS':
                coeff = 1.

            thy = coeff * FUTsinphiS / FUU

        else:
            print 'ERR: exp=%d obs=%s and target=%s not implemented' % (
                k, obs, target)
            sys.exit()

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

        L.append('%7s %10s %10s %10s %10s %5s %10s %10s %10s' % (
            'idx', 'tar', 'had', 'col', 'obs', 'npts', 'chi2', 'rchi2', 'nchi2'))
        for k in self.tabs:
            #print k,len(self.tabs[k]['value'])
            if self.tabs[k]['value'].size == 0:
                continue
            res = self._get_residuals(k)
            rres = self._get_rres(k)
            nres = self._get_nres(k)

            chi2 = np.sum(res**2)
            rchi2 = np.sum(rres**2)
            nchi2 = nres**2
            tar = self.tabs[k]['target'][0]
            col = self.tabs[k]['col'][0].split()[0]
            obs = self.tabs[k]['obs'][0].split()[0]
            had = self.tabs[k]['hadron'][0].split()[0]
            npts = res.size
            L.append('%7d %10s %10s %10s %10s %5d %10.2f %10.2f %10.2f' %
                     (k, tar, had, col, obs, npts, chi2, rchi2, nchi2))

        if level == 1:
            L.append('-' * 100)

            msg = 'idx=%7d,  '
            msg += 'col=%7s,  '
            msg += 'tar=%7s,  '
            msg += 'had=%7s,  '
            msg += 'obs=%7s,  '
            if 'dependence' in self.tabs[k]:
                msg += 'dep=%7s,  '
            if 'Dependence' in self.tabs[k]:
                msg += 'dep=%7s,  '
            msg += 'x=%10.3e,  '
            msg += 'z=%10.3e,  '
            msg += 'pT=%10.3e,  '
            msg += 'Q2=%10.3e,  '
            msg += 'yh=%10.3e,  '
            msg += 'yp=%10.3e,  '
            msg += 'dy=%10.3e,  '
            msg += 'exp=%10.3e,  '
            msg += 'alpha=%10.3e,  '
            msg += 'thy=%10.3e,  '
            if 'dthy' in self.tabs[k]:
                msg += 'dthy=%10.3e,  '
            msg += 'shift=%10.3e,  '
            msg += 'chi2=%10.3f  '

            for k in self.tabs:
                if len(self.tabs[k]['value']) == 0:
                    continue
                for i in range(len(self.tabs[k]['value'])):
                    row = [k]
                    row.append(self.tabs[k]['col'][i])
                    row.append(self.tabs[k]['target'][i])
                    row.append(self.tabs[k]['hadron'][i])
                    row.append(self.tabs[k]['obs'][i])
                    if 'dependence' in self.tabs[k]:
                        row.append(self.tabs[k]['dependence'][i].strip())
                    if 'Dependence' in self.tabs[k]:
                        row.append(self.tabs[k]['Dependence'][i].strip())
                    row.append(self.tabs[k]['x'][i])
                    row.append(self.tabs[k]['z'][i])
                    row.append(self.tabs[k]['pT'][i])
                    row.append(self.tabs[k]['Q2'][i])
                    row.append(self.tabs[k]['yh'][i])
                    row.append(self.tabs[k]['yp'][i])
                    row.append(self.tabs[k]['dy'][i])
                    row.append(self.tabs[k]['value'][i])
                    row.append(self.tabs[k]['alpha'][i])
                    row.append(self.tabs[k]['thy'][i])
                    if 'dthy' in self.tabs[k]:
                        row.append(self.tabs[k]['dthy'][i])
                    row.append(self.tabs[k]['shift'][i])
                    # row.append(self.tabs[k]['residuals'][i])
                    # row.append(self.tabs[k]['r-residuals'][i])
                    res = self.tabs[k]['residuals'][i]
                    if res < 0:
                        chi2 = -res**2
                    else:
                        chi2 = res**2
                    row.append(chi2)
                    row = tuple(row)
                    L.append(msg % row)

        if verb == 0:
            return L
        elif verb == 1:
            for l in L:
                print l
            return L

if __name__ == '__main__':

    from qcdlib.interpolator import INTERPOLATOR
    from stfuncs import STFUNCS
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
    from reader import READER

    conf['aux']    = AUX()
    conf['alphaSmode'] = 'backward'
    conf['order'] = 'NLO'
    conf['Q20'] = 1
    conf['alphaS'] = ALPHAS()

    conf['cpdf']   = INTERPOLATOR('CJ15lo_0000')
    conf['cppdf']  = INTERPOLATOR('CJ15lo_0000')
    conf['cpipff'] = INTERPOLATOR('dsspipLO_0000')
    conf['cpimff'] = INTERPOLATOR('dsspimLO_0000')
    conf['cKpff']  = INTERPOLATOR('dssKpLO_0000')
    conf['cKmff']  = INTERPOLATOR('dssKmLO_0000')

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


    conf['sidis stfuncs'] = STFUNCS()
    conf['dis stfuncs']   = DIS_STFUNCS()


    conf['datasets']={}
    conf['datasets']['sidis']={}
    
    conf['datasets']['sidis']['xlsx']={}
    conf['datasets']['sidis']['xlsx'][1000]='sidis/expdata/1000.xlsx'  # |  proton   | pi+   | M_Hermes | hermes 
    conf['datasets']['sidis']['xlsx'][1001]='sidis/expdata/1001.xlsx'  # |  proton   | pi-   | M_Hermes | hermes 
    conf['datasets']['sidis']['xlsx'][1004]='sidis/expdata/1004.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes 
    conf['datasets']['sidis']['xlsx'][1005]='sidis/expdata/1005.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes 
    conf['datasets']['sidis']['xlsx'][1002]='sidis/expdata/1002.xlsx'  # |  proton   | k+    | M_Hermes | hermes 
    conf['datasets']['sidis']['xlsx'][1003]='sidis/expdata/1003.xlsx'  # |  proton   | k-    | M_Hermes | hermes 
    conf['datasets']['sidis']['xlsx'][1006]='sidis/expdata/1006.xlsx'  # |  deuteron | k+    | M_Hermes | hermes 
    conf['datasets']['sidis']['xlsx'][1007]='sidis/expdata/1007.xlsx'  # |  deuteron | k-    | M_Hermes | hermes 
    conf['datasets']['sidis']['norm']={}
    for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 
    conf['datasets']['sidis']['filters']={}
    conf['datasets']['sidis']['filters'][1000]="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"
    conf['datasets']['sidis']['filters'][1001]="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"
    conf['datasets']['sidis']['filters'][1004]="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"
    conf['datasets']['sidis']['filters'][1005]="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"
    conf['datasets']['sidis']['filters'][1002]="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"
    conf['datasets']['sidis']['filters'][1003]="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"
    conf['datasets']['sidis']['filters'][1006]="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"
    conf['datasets']['sidis']['filters'][1007]="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"

    conf['sidis tabs'] = READER().load_data_sets('sidis')
    conf['residuals']= RESIDUALS()
    conf['residuals'].get_residuals()
    conf['residuals'].gen_report(verb=1, level=1)










