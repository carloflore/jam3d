import os
import numpy as np
from tools.tools import load, save, checkdir
from tools.config import conf
from tools.randomstr import id_generator
import nest
from multiprocessing import Process, Queue, Pool, Pipe


class MCSAMP:

    def __init__(self):
        pass

    def get_residuals(self, par):
        res, rres, nres = conf['resman'].get_residuals(par)
        if len(rres) != 0:
            res = np.append(res, rres)
        if len(nres) != 0:
            res = np.append(res, nres)
        return res

    def loglike(self, par):
        return -0.5 * np.sum(self.get_residuals(par)**2)

    def nll(self, par):
        res = self.get_residuals(par)
        return 0.5 * (np.sum(res**2))

    def linmap(self, q, pmin, pmax):
        return (pmax - pmin) * q + pmin

    def get_par_lims(self):
        plims = []
        for i in range(len(conf['parman'].order)):
            ii, k, kk = conf['parman'].order[i]
            if ii == 1:
                pmin = conf['params'][k][kk]['min']
                pmax = conf['params'][k][kk]['max']
            elif ii == 2:
                pmin = conf['datasets'][k]['norm'][kk]['min']
                pmax = conf['datasets'][k]['norm'][kk]['max']
            plims.append([pmin, pmax])
        return plims

    def single_run(self, path, nestout, factor=2, kappa=1, tol=1e-10, itmax=10, sample_size=1000, method='cov', nll_shift=0):

        # set nest params if not specified in conf
        if 'factor' not in conf:
            conf['factor'] = factor
        if 'tol' not in conf:
            conf['tol'] = tol
        if 'itmax' not in conf:
            conf['itmax'] = itmax
        if 'kappa' not in conf:
            conf['kappa'] = kappa
        if 'method' not in conf:
            conf['method'] = method
        if 'sample size' not in conf:
            conf['sample size'] = sample_size
        if 'nll shift' not in conf:
            conf['nll shift'] = nll_shift

        conf['nestout'] = nestout

        npar = len(conf['parman'].par)
        conf['nll'] = self.nll
        conf['par lims'] = self.get_par_lims()
        conf['num points'] = int(npar * conf['factor'])

        par = conf['parman'].par
        res = self.get_residuals(par)
        conf['nll shift'] = 0  # 0.5*(len(res)+conf['nll shift'])

        if 's3 cmd' in conf:
            cmd = conf['s3 cmd']
        else:
            cmd = None
        nest.NEST().run(path, cmd)

        # results=nest.NEST().run()
        # save(results,path)

    def run(self, nruns=1):

        if 'nruns' in conf:
            nruns = conf['nruns']

        # set outputdir
        if 'args' in conf:
            outputdir = '%s/mcdata' % conf['args'].config.split(
                '/')[-1].replace('.py', '')
        else:
            outputdir = 'mcdata'
        checkdir(outputdir)

        # get exisiting runs
        idx = [int(x.replace('.dat', '')) for x in os.listdir(outputdir)]

        if len(idx) == 0:
            fname = ['%s/%i.dat' % (outputdir, i) for i in range(nruns)]
            nestout = [None for i in range(nruns)]
        else:
            fname = ['%s/%s' % (outputdir, _) for _ in os.listdir(outputdir)]
            nestout = [load('%s/%s' % (outputdir, _))
                       for _ in os.listdir(outputdir)]

        for i in range(nruns):
            print 'run ', i
            self.single_run(fname[i], nestout[i])

        #P = [Process(target=self.single_run, args=(fname[i],nestout[i])) for i  in range(nruns)]
        #for p in P: p.start()
        #for p in P: p.join()

    def run2(self):
        nruns = conf['nruns']
        for i in range(nruns):
            fname = id_generator(size=6)
            self.single_run(fname, None)

    def get_MC_samples(self, mcpath):
        F = os.listdir(mcpath)
        data = []
        for f in F:
            data.append(load('%s/%s' % (mcpath, f)))

        samples = []
        likelihoods = []
        n = 0
        for d in data:
            for p in d['samples']:
                samples.append(p)
            likelihoods.extend(d['l'])
            n += len(d['active nll'])

        samples = np.array(samples)
        likelihoods = np.array(likelihoods)
        I = np.argsort(likelihoods)[::-1]
        x = np.array([((n - 1.) / n)**i for i in range(len(likelihoods) + 1)])
        dx = (0.5 * (x[:-1] - x[1:]))[::-1]
        x = x[::-1]
        likelihoods = likelihoods[I]
        samples = samples[I]
        weights = np.array([likelihoods[i] * dx[i] for i in range(dx.size)])
        weights /= np.sum(weights)

        weights2 = np.array([weights[i]
                             for i in range(weights.size) if weights[i] > 1e-4])
        samples2 = np.array([samples[i]
                             for i in range(len(weights)) if weights[i] > 1e-4])
        weights2 /= np.sum(weights2)

        print 'runs max likelihoods'
        for d in data:
            print d['active nll'][0]

        print 'sample  size=', weights.size
        print 'sample2 size=', weights2.size

        out = {}
        out['samples'] = samples
        out['weights'] = weights
        out['samples2'] = samples2
        out['weights2'] = weights2
        out['order'] = conf['parman'].order
        out['runs'] = {}
        cnt = 0
        for d in data:
            out['runs'][cnt] = {
                'samples': d['samples'], 'weights': d['weights']}
            cnt += 1
        return out

    def get_stat(self, w, F):
        F = np.array(F)
        # ibest=np.argmax(w)
        # f0=F[ibest]
        f0 = np.einsum('i,ij->j', w, F)

        df2min = []
        for i in range(f0.size):
            K = [k for k in range(len(F)) if F[k][i] <= f0[i]]
            fi = [F[k][i] for k in K]
            wi = [w[k] for k in K]
            fi = np.append(fi, [f0[i] + (f0[i] - f) for f in fi])
            wi = np.append(wi, [w[k] for k in K])
            wi = wi / np.sum(wi)
            df2min.append(np.einsum('i,i', wi, (fi - f0[i])**2))
        dfmin = np.array(df2min)**0.5

        df2max = []
        for i in range(f0.size):
            K = [k for k in range(len(F)) if F[k][i] > f0[i]]
            fi = [F[k][i] for k in K]
            wi = [w[k] for k in K]
            fi = np.append(fi, [f0[i] - (f - f0[i]) for f in fi])
            wi = np.append(wi, [w[k] for k in K])
            wi = wi / np.sum(wi)
            df2max.append(np.einsum('i,i', wi, (fi - f0[i])**2))
        dfmax = np.array(df2max)**0.5

        return {'f0': f0, 'dfmin': dfmin, 'dfmax': dfmax}

    # analysis routines. Use analysis as the gate

    def analysis(self):
        self.gen_report()
        # self.check_snapshot()

    def gen_report(self):
        inputfile = conf['args'].config
        nestfile = conf['args'].fname
        nestout = load(nestfile)
        weight = nestout['weights'][0]
        q = nestout['samples'][0]
        self.get_residuals(q)
        report = conf['resman'].gen_report(verb=1, level=1)
        save(report, 'report')

        with open(inputfile) as f:
            L = f.readlines()
        for i in range(len(L)):

            if L[i].startswith('#'):
                continue

            if 'params' in L[i] and '<<' in L[i]:
                l = L[i].split('=')[0].replace('conf', '').replace("'", '')
                k, kk = l.replace('][', '@').replace(
                    '[', '').replace(']', '').split('@')[1:]
                left = L[i].split('<<')[0]
                right = L[i].split('>>')[1]
                L[i] = left + '<<%30.20e>>' % conf['params'][k.strip()][kk.strip()
                                                                      ]['value'] + right

            if 'norm' in L[i] and '<<' in L[i]:
                l = L[i].split('=')[0].replace('conf', '').replace("'", '')
                dum1, k, dum2, kk = l.replace('][', '@').replace(
                    '[', '').replace(']', '').split('@')
                left = L[i].split('<<')[0]
                right = L[i].split('>>')[1]

                value = conf['datasets'][k.strip()]['norm'][int(kk)]['value']
                L[i] = left + '<<%30.20e>>' % value + right

        with open(inputfile, 'w') as f:
            f.writelines(L)

    def check_snapshot(self):
        self.npar = len(conf['parman'].par)
        conf = {}
        conf['nll'] = self.nll
        conf['par lims'] = self.get_par_lims()
        conf['num points'] = self.npar * conf['num points factor']
        conf['snapshot'] = conf['args'].snapshot
        nest = NEST(conf)
        par = nest.samples_p[-1]
        self.get_residuals(par)
        report = self.conf['resman'].gen_report(verb=1, level=1)
        save(report, 'report')
