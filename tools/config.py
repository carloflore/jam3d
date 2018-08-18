
conf = {}


def load_config(fname):
    with open(fname) as f:
        L = f.readlines()
    D = {}
    for l in L:
        exec l.replace('<<', '').replace('>>', '') in D
    conf.update(D['conf'])
