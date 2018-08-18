import os
import argparse
import sys
import time
import logging
import fitlab.parallel as parallel

import numpy as np
import external.CJLIB.CJ
import external.DSSLIB.DSS
import external.LSSLIB.LSS
import external.PDF.CT10  # Alexei 4/20/2018
import qcdlib.tmdlib
import qcdlib.aux
import qcdlib.alphaS
import obslib.dis.stfuncs
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
from mcsamp import MCSAMP
from maxlike import ML
from tools.config import load_config, conf


class RESMAN:

    def __init__(self, mode='solo', ip=None, nworkers=None):

        self.mode = mode
        self.master = None
        self.slave = None
        self.broker = None

        conf['aux'] = qcdlib.aux.AUX()
        self.setup_tmds()
        conf['parman'] = PARMAN()

        if self.mode == 'parallel':
            self.master = parallel.Server(ip=ip)
            self.slave = parallel.Worker(ip=ip)
            self.broker = parallel.Broker()
        elif self.mode == 'master':
            self.master = parallel.Server(ip=ip)
        elif self.mode == 'slave':
            self.slave = parallel.Worker(ip=ip)

        conf['moments'] = obslib.moments.moments.MOMENTS()

        if 'datasets' in conf:
            if 'sidis' in conf['datasets']:
                self.setup_dis()
                self.setup_sidis()
            if 'sia' in conf['datasets']:
                self.setup_sia()
            if 'moments' in conf['datasets']:
                self.setup_moments()
            if 'AN' in conf['datasets']:
                self.setup_AN()

        if self.mode == 'parallel':
            self.broker.run_subprocess()
            self.slave.run_subprocess()

    def setup_dis(self):
        conf['alphaSmode'] = 'backward'
        conf['Q20'] = 1
        # conf['order']='NLO'
        conf['order'] = 'LO'
        conf['alphaS'] = qcdlib.alphaS.ALPHAS()
        conf['pdf-NLO'] = external.CJLIB.CJ.CJ()
        conf['dis stfuncs'] = obslib.dis.stfuncs.STFUNCS()

    def setup_tmds(self):
        conf['order'] = 'LO'
        conf['path2CT10'] = '%s/external/PDF' % os.environ['FITPACK']
        conf['path2CJ'] = '%s/external/CJLIB' % os.environ['FITPACK']
        conf['path2LSS'] = '%s/external/LSSLIB' % os.environ['FITPACK']
        conf['path2DSS'] = '%s/external/DSSLIB' % os.environ['FITPACK']
        conf['_pdf'] = external.CJLIB.CJ.CJ()
        #conf['_pdf'] =external.PDF.CT10.CT10()
        conf['_ppdf'] = external.LSSLIB.LSS.LSS()
        conf['_ff'] = external.DSSLIB.DSS.DSS()
        conf['pdf'] = qcdlib.tmdlib.PDF()
        conf['ppdf'] = qcdlib.tmdlib.PPDF()
        conf['ff'] = qcdlib.tmdlib.FF()
        conf['transversity'] = qcdlib.tmdlib.TRANSVERSITY()
        conf['sivers'] = qcdlib.tmdlib.SIVERS()
        conf['boermulders'] = qcdlib.tmdlib.BOERMULDERS()
        conf['pretzelosity'] = qcdlib.tmdlib.PRETZELOSITY()
        conf['wormgearg'] = qcdlib.tmdlib.WORMGEARG()
        conf['wormgearh'] = qcdlib.tmdlib.WORMGEARH()
        conf['collins'] = qcdlib.tmdlib.COLLINS()
        conf['Htilde'] = qcdlib.tmdlib.HTILDE()

    def setup_sidis(self):
        conf['sidis tabs'] = obslib.sidis.reader.READER().load_data_sets('sidis')
        conf['sidis stfuncs'] = obslib.sidis.stfuncs.STFUNCS()
        self.sidisres = obslib.sidis.residuals.RESIDUALS()

        if (self.slave):
            self.slave.add_mproc('sidis', self.sidisres.mproc)
        if (self.master):
            self.sidisres.mproc = self.master.wrap_mproc(
                'sidis', self.sidisres.mproc)

    def setup_sia(self):
        conf['sia tabs'] = obslib.sia.reader.READER().load_data_sets('sia')
        conf['sia stfuncs'] = obslib.sia.stfuncs.STFUNCS()
        self.siares = obslib.sia.residuals.RESIDUALS()

        if (self.slave):
            self.slave.add_mproc('sia', self.siares.mproc)
        if (self.master):
            self.siares.mproc = self.master.wrap_mproc(
                'sia', self.siares.mproc)

    def setup_moments(self):
        conf['moments tabs'] = obslib.moments.reader.READER(
        ).load_data_sets('moments')
        conf['moments'] = obslib.moments.moments.MOMENTS()
        self.momres = obslib.moments.residuals.RESIDUALS()

        if (self.slave):
            self.slave.add_mproc('moments', self.momres.mproc)
        if (self.master):
            self.momres.mproc = self.master.wrap_mproc(
                'moments', self.momres.mproc)

    def setup_AN(self):
        conf['AN tabs'] = obslib.AN_pp.reader.READER().load_data_sets('AN')
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
