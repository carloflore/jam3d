import os
import sys
import time
import logging
import fitlab.parallel as parallel
import numpy as np
import qcdlib.tmdlib
import qcdlib.aux
import qcdlib.alphaS
import qcdlib.interpolator
import obslib.idis.stfuncs
import obslib.sidis.stfuncs
import obslib.sidis.residuals
import obslib.sidis.reader
import obslib.sia.stfuncs
import obslib.sia.residuals
import obslib.sia.reader
import obslib.moments.reader
import obslib.moments.moments
import obslib.moments.residuals
import obslib.AN_pp.AN_theory
import obslib.AN_pp.residuals
import obslib.AN_pp.reader
from parman import PARMAN
from tools.config import load_config, conf


class RESMAN:

    def __init__(self, mode='solo', ip=None, nworkers=None):

        # initial setup for parallelization
        self.mode = mode
        self.master = None
        self.slave = None
        self.broker = None

        if self.mode == 'parallel':
            self.master = parallel.Server(ip=ip)
            self.slave = parallel.Worker(ip=ip)
            self.broker = parallel.Broker()
        elif self.mode == 'master':
            self.master = parallel.Server(ip=ip)
        elif self.mode == 'slave':
            self.slave = parallel.Worker(ip=ip)

        # theory setups
        conf['aux'] = qcdlib.aux.AUX()
        self.load_collinear_distributions()
        self.set_alphaS()
        self.setup_tmds()
        conf['parman'] = PARMAN()
        conf['moments'] = obslib.moments.moments.MOMENTS()

        if 'datasets' in conf:

            if 'sidis' in conf['datasets']:
                self.setup_idis()
                self.setup_sidis()

            if 'sia' in conf['datasets']:
                self.setup_sia()

            if 'moments' in conf['datasets']:
                self.setup_moments()

            if 'AN' in conf['datasets']:
                self.setup_AN()

        # final setups for paralleization
        if self.mode == 'parallel':
            self.broker.run_subprocess()
            self.slave.run_subprocess()

    def set_alphaS(self):

        conf['alphaSmode'] = 'backward'
        conf['Q20'] = 1
        conf['order'] = 'NLO'
        conf['alphaS'] = qcdlib.alphaS.ALPHAS()

    def load_collinear_distributions(self):

        defaults={}
        defaults['cpdf']   = 'CJ15lo_0000'
        defaults['cppdf']  = 'CJ15lo_0000'
        defaults['cpipff'] = 'dsspipLO_0000'
        defaults['cpimff'] = 'dsspimLO_0000'
        defaults['cKpff']  = 'dssKpNLO_0000'
        defaults['cKmff']  = 'dssKmNLO_0000'

        for k in defaults:
            if k in conf:  conf[k] = qcdlib.interpolator.INTERPOLATOR(conf[k])
            else:          conf[k] = qcdlib.interpolator.INTERPOLATOR(defaults[k])

    def setup_idis(self):
        conf['dis stfuncs']  = obslib.idis.stfuncs.STFUNCS()

    def setup_tmds(self):
        conf['lam2'] = 0.4 
        conf['Q02']  = 1.0
        if 'pdf'          in conf['params']:conf['pdf']          = qcdlib.tmdlib.PDF()
        if 'ppdf'         in conf['params']:conf['ppdf']         = qcdlib.tmdlib.PPDF()
        if 'ff'           in conf['params']:conf['ff']           = qcdlib.tmdlib.FF()
        if 'transversity' in conf['params']:conf['transversity'] = qcdlib.tmdlib.TRANSVERSITY()
        if 'sivers'       in conf['params']:conf['sivers']       = qcdlib.tmdlib.SIVERS()
        if 'boermulders'  in conf['params']:conf['boermulders']  = qcdlib.tmdlib.BOERMULDERS()
        if 'pretzelosity' in conf['params']:conf['pretzelosity'] = qcdlib.tmdlib.PRETZELOSITY()
        if 'wormgearg'    in conf['params']:conf['wormgearg']    = qcdlib.tmdlib.WORMGEARG()
        if 'wormgearh'    in conf['params']:conf['wormgearh']    = qcdlib.tmdlib.WORMGEARH()
        if 'collins'      in conf['params']:conf['collins']      = qcdlib.tmdlib.COLLINS()
        if 'Htilde'       in conf['params']:conf['Htilde']       = qcdlib.tmdlib.HTILDE()

    def setup_sidis(self):
        conf['sidis tabs']    = obslib.sidis.reader.READER().load_data_sets('sidis')
        conf['sidis stfuncs'] = obslib.sidis.stfuncs.STFUNCS()
        self.sidisres = obslib.sidis.residuals.RESIDUALS()

        if (self.slave):
            self.slave.add_mproc('sidis', self.sidisres.mproc)
        if (self.master):
            self.sidisres.mproc = self.master.wrap_mproc(
                'sidis', self.sidisres.mproc)

    def setup_sia(self):
        conf['sia tabs']    = obslib.sia.reader.READER().load_data_sets('sia')
        conf['sia stfuncs'] = obslib.sia.stfuncs.STFUNCS()
        self.siares = obslib.sia.residuals.RESIDUALS()

        if (self.slave):
            self.slave.add_mproc('sia', self.siares.mproc)
        if (self.master):
            self.siares.mproc = self.master.wrap_mproc(
                'sia', self.siares.mproc)

    def setup_moments(self):
        conf['moments tabs'] = obslib.moments.reader.READER().load_data_sets('moments')
        conf['moments']      = obslib.moments.moments.MOMENTS()
        self.momres = obslib.moments.residuals.RESIDUALS()

        if (self.slave):
            self.slave.add_mproc('moments', self.momres.mproc)
        if (self.master):
            self.momres.mproc = self.master.wrap_mproc(
                'moments', self.momres.mproc)

    def setup_AN(self):
        conf['AN tabs']   = obslib.AN_pp.reader.READER().load_data_sets('AN')
        conf['AN theory'] = obslib.AN_pp.AN_theory.ANTHEORY()
        self.ANres = obslib.AN_pp.residuals.RESIDUALS()

        if (self.slave):
            self.slave.add_mproc('AN', self.ANres.mproc)
        if (self.master):
            self.ANres.mproc = self.master.wrap_mproc('AN', self.ANres.mproc)

    def get_residuals(self, par, calc=True, simple=False):
        conf['parman'].set_new_params(par)

        if (self.master):
            self.master.assign_work()

        res, rres, nres = [], [], []
        if 'sidis' in conf['datasets']:
            out = self.sidisres.get_residuals(calc=calc, simple=simple)
            res = np.append(res, out[0])
            rres = np.append(rres, out[1])
            nres = np.append(nres, out[2])
        if 'sia' in conf['datasets']:
            out = self.siares.get_residuals(calc=calc, simple=simple)
            res = np.append(res, out[0])
            rres = np.append(rres, out[1])
            nres = np.append(nres, out[2])
        if 'moments' in conf['datasets']:
            out = self.momres.get_residuals(calc=calc, simple=simple)
            res = np.append(res, out[0])
            rres = np.append(rres, out[1])
            nres = np.append(nres, out[2])
        if 'AN' in conf['datasets']:
            out = self.ANres.get_residuals(calc=calc, simple=simple)
            res = np.append(res, out[0])
            rres = np.append(rres, out[1])
            nres = np.append(nres, out[2])
        return res, rres, nres

    def gen_report(self, verb=0, level=0):
        L = []
        if 'sidis' in conf['datasets']:
            L.extend(self.sidisres.gen_report(verb, level))
        if 'sia' in conf['datasets']:
            L.extend(self.siares.gen_report(verb, level))
        if 'moments' in conf['datasets']:
            L.extend(self.momres.gen_report(verb, level))
        if 'AN' in conf['datasets']:
            L.extend(self.ANres.gen_report(verb, level))
        return L

    def run_worker(self):
        self.slave.run()

    def shutdown(self):
        if (self.master):
            self.master.finis()
            time.sleep(3)
        if (self.slave):
            self.slave.stop()
        if (self.broker):
            self.broker.stop()
