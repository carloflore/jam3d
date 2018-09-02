conf={}

############################################################################
#mcsamp
conf['ncpu']=10
conf['nruns']=1
conf['factor']=3.0
conf['kappa']=1.5
conf['tol']=1e-10
conf['itmax']=int(1e7)
conf['block size']=10


conf['evo'] = 'no' #if 'no', set evo parameters to 'fixed':True
conf['Q02evo'] = 4.0
conf['lam2evo'] = 0.04
############################################################################
# params

conf['params']={}
# Parameters in gaussian approximation, parton model:
# TMD PDF fixed:
conf['params']['pdf']={}
conf['params']['pdf']['uv widths1']  ={'value':    5.72856e-01,'min': 0,'max':1,'fixed':True}
conf['params']['pdf']['uv widths2']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['pdf']['dv widths1']  ={'value':    5.72856e-01,'min': 0,'max':1,'fixed':'uv widths1'}
conf['params']['pdf']['dv widths2']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'uv widths2'}
conf['params']['pdf']['sea widths1'] ={'value':    6.03981e-01,'min': 0,'max':1,'fixed':True}
conf['params']['pdf']['sea widths2'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}

# TMD FF fixed:
conf['params']['ff']={}
conf['params']['ff']['pi+fav widths1']   ={'value':    1.16790e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ff']['pi+fav widths2']   ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ff']['pi+unfav widths1'] ={'value':    1.37349e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ff']['pi+unfav widths2'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ff']['k+fav widths1']    ={'value':    1.32925e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ff']['k+fav widths2']    ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ff']['k+unfav widths1']  ={'value':    1.86073e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ff']['k+unfav widths2']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}

# COLLINS TMD FF:
conf['params']['collins']={}
conf['params']['collins']['widths0 pi+ fav']     = {'value':    7.69177847427865157837e-02,'fixed':False,'min':0.05,'max':1.24049999999999993605e-01}
conf['params']['collins']['widths0 pi+ unfav']   = {'value':    7.82974753203348333708e-02,'fixed':False,'min':1e-5,'max':1.43729999999999996652e-01}
conf['params']['collins']['pi+ u N0 1']  = {'value':    7.27976317212180701333e-01,'fixed':False,'min':0,'max':4}
conf['params']['collins']['pi+ u a0 1']  = {'value':   -1.85298624430834779631e+00,'fixed':False,'min':-2.5,'max':0}
conf['params']['collins']['pi+ u b0 1']  = {'value':    5.39183069660368463616e+00,'fixed':False,'min':3.,'max':7.}
#evo part
conf['params']['collins']['pi+ u N1 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u a1 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u b1 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u c1 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d1 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['pi+ d N0 1']  = {'value':   -3.43290097947612160567e+00,'fixed':False,'min':-15,'max':2}
conf['params']['collins']['pi+ d a0 1']  = {'value':    1.07876853314680998253e+00,'fixed':False,'min': 0.,'max':4.5}
conf['params']['collins']['pi+ d b0 1']  = {'value':    3.18601609944188135515e+00,'fixed':False,'min':2.5,'max':3.8}
#evo part
conf['params']['collins']['pi+ d N1 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d a1 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d b1 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d c1 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d d1 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['pi+ u c0 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d c0 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d0 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d d0 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}


conf['params']['collins']['pi+ u c0 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d c0 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d0 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d d0 1']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['pi+ u N0 2']  = {'value':    1.05827284963755605673e+01,'fixed':False,'min':1,'max':52}
conf['params']['collins']['pi+ u a0 2']  = {'value':    7.94843162206008546633e+00,'fixed':False,'min':1,'max':20}
conf['params']['collins']['pi+ u b0 2']  = {'value':    3.00185190517106192942e+00,'fixed':False,'min':3,'max':25}
#evo part
conf['params']['collins']['pi+ u N1 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u a1 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u b1 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u c1 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d1 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['pi+ d N0 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-20,'max':0}
conf['params']['collins']['pi+ d a0 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-1,'max':5}
conf['params']['collins']['pi+ d b0 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':1e-5,'max':10}
conf['params']['collins']['pi+ u c0 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d c0 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d0 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d d0 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
#evo part
conf['params']['collins']['pi+ d N1 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d a1 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d b1 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d c1 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d d1 2']  = {'value':    0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}

# TRANSVERSITY TMD PDF:
conf['params']['transversity']={}
conf['params']['transversity']['u widths1']  ={'value':    5.24140000000000050306e-01,'min': 0,'max':1,'fixed':True}
conf['params']['transversity']['u widths2']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['transversity']['d widths1']  ={'value':    5.24140000000000050306e-01,'min': 0,'max':1,'fixed':'u widths1'}
conf['params']['transversity']['d widths2']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'uv widths2'}
conf['params']['transversity']['sea widths1'] ={'value':    5.84650000000000003020e-01,'min': 0,'max':1,'fixed':True}
conf['params']['transversity']['sea widths2'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}


conf['params']['transversity']['u N0']             = {'value':    6.93615720926875667374e+00 ,'fixed':False,'min':-10,'max':10}
conf['params']['transversity']['u a0']             = {'value':    7.50418051324418744485e-01 ,'fixed':False,'min':-1,'max':10}
conf['params']['transversity']['u b0']             = {'value':    2.35588099798776795524e+00 ,'fixed':False,'min':1e-5,'max':10}
conf['params']['transversity']['d N0']             = {'value':   -5.76636326391826070648e+00 ,'fixed':False,'min':-20,'max':20}
conf['params']['transversity']['d a0']             = {'value':    2.50990802211820351886e-01 ,'fixed':False,'min':-1,'max':5}
conf['params']['transversity']['d b0']             = {'value':    7.32587435823372068455e+00 ,'fixed':False,'min':1e-5,'max':20}
conf['params']['transversity']['s N0']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s a0']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-1,'max':5}
conf['params']['transversity']['s b0']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':0.,'max':10}

conf['params']['transversity']['u c0']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['d c0']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s c0']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-10,'max':10}

conf['params']['transversity']['u d0']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['d d0']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s d0']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-10,'max':10}

#evolution
conf['params']['transversity']['u N1']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['u a1']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-1,'max':5}
conf['params']['transversity']['u b1']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':0.,'max':10}
conf['params']['transversity']['u c1']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-1,'max':5}
conf['params']['transversity']['u d1']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':0.,'max':10}

conf['params']['transversity']['d N1']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['d a1']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-1,'max':5}
conf['params']['transversity']['d b1']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':0.,'max':10}
conf['params']['transversity']['d c1']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-1,'max':5}
conf['params']['transversity']['d d1']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':0.,'max':10}


conf['params']['transversity']['s N1']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s a1']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-1,'max':5}
conf['params']['transversity']['s b1']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':0.,'max':10}
conf['params']['transversity']['s c1']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':-1,'max':5}
conf['params']['transversity']['s d1']             = {'value':    0.00000000000000000000e+00 ,'fixed':True,'min':0.,'max':10}

############################################################################
# set data sets

conf['datasets']={}

# SIA

conf['datasets']['sia']={}


conf['datasets']['sia']['norm']={}

conf['datasets']['sia']['filters']=[] # npts    = 122 chi2    = 69.799935
#conf['datasets']['sia']['filters'].append("z<0.6")
#conf['datasets']['sia']['filters'].append("Q2>1.69")
#conf['datasets']['sia']['filters'].append("pT>0.2 and pT<0.9")


conf['datasets']['sia']['xlsx']={}

conf['datasets']['sia']['xlsx'][1000]='sia/expdata/1000.xlsx' # babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1001]='sia/expdata/1001.xlsx' # babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1002]='sia/expdata/1002.xlsx' # babar | pi,pi | AUC-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1003]='sia/expdata/1003.xlsx' # babar | pi,pi | AUL-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1004]='sia/expdata/1004.xlsx' # belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
conf['datasets']['sia']['xlsx'][1005]='sia/expdata/1005.xlsx' # belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |
conf['datasets']['sia']['xlsx'][2008]='sia/expdata/2008.xlsx' # | babar      | pi,pi | AUL-0            | 16     | z1,z2      |
conf['datasets']['sia']['xlsx'][2009]='sia/expdata/2009.xlsx' # | babar      | pi,pi | AUC-0            | 16     | z1,z2      |


# Collins Asy
conf['datasets']['sidis']={}
conf['datasets']['sidis']['norm']={}
conf['datasets']['sidis']['xlsx']={}
conf['datasets']['sidis']['filters']={}

conf['datasets']['sidis']['filters'][0]={}
conf['datasets']['sidis']['filters'][0]['idx']=[4001,4000,4002,4004,4003,4005,3027,3025,3010,3012,3005,3013,3026,3000,3003,3016,3004,3018]
conf['datasets']['sidis']['filters'][0]['filter']="z>0.2 and z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"

#multiplicity?

#conf["datasets"]["sidis"]["xlsx"][4007]="sidis/expdata/4007.xlsx"  #  compass  deuteron   k+   pT
#conf["datasets"]["sidis"]["xlsx"][4006]="sidis/expdata/4006.xlsx"  #  compass  deuteron   k+    x
#conf["datasets"]["sidis"]["xlsx"][4008]="sidis/expdata/4008.xlsx"  #  compass  deuteron   k+    z
#conf["datasets"]["sidis"]["xlsx"][4010]="sidis/expdata/4010.xlsx"  #  compass  deuteron   k-   pT
#conf["datasets"]["sidis"]["xlsx"][4009]="sidis/expdata/4009.xlsx"  #  compass  deuteron   k-    x
#conf["datasets"]["sidis"]["xlsx"][4011]="sidis/expdata/4011.xlsx"  #  compass  deuteron   k-    z
conf["datasets"]["sidis"]["xlsx"][4001]="sidis/expdata/4001.xlsx"  #  compass  deuteron  pi+   pT
conf["datasets"]["sidis"]["xlsx"][4000]="sidis/expdata/4000.xlsx"  #  compass  deuteron  pi+    x
conf["datasets"]["sidis"]["xlsx"][4002]="sidis/expdata/4002.xlsx"  #  compass  deuteron  pi+    z
conf["datasets"]["sidis"]["xlsx"][4004]="sidis/expdata/4004.xlsx"  #  compass  deuteron  pi-   pT
conf["datasets"]["sidis"]["xlsx"][4003]="sidis/expdata/4003.xlsx"  #  compass  deuteron  pi-    x
conf["datasets"]["sidis"]["xlsx"][4005]="sidis/expdata/4005.xlsx"  #  compass  deuteron  pi-    z
#conf["datasets"]["sidis"]["xlsx"][6003]="sidis/expdata/6003.xlsx"  #  compass    proton   k+   pt
#conf["datasets"]["sidis"]["xlsx"][6004]="sidis/expdata/6004.xlsx"  #  compass    proton   k+    x
#conf["datasets"]["sidis"]["xlsx"][6005]="sidis/expdata/6005.xlsx"  #  compass    proton   k+    z
#conf["datasets"]["sidis"]["xlsx"][6000]="sidis/expdata/6000.xlsx"  #  compass    proton   k-   pt
#conf["datasets"]["sidis"]["xlsx"][6001]="sidis/expdata/6001.xlsx"  #  compass    proton   k-    x
#conf["datasets"]["sidis"]["xlsx"][6002]="sidis/expdata/6002.xlsx"  #  compass    proton   k-    z
conf["datasets"]["sidis"]["xlsx"][3027]="sidis/expdata/3027.xlsx"  #  compass    proton  pi+   pt
conf["datasets"]["sidis"]["xlsx"][3025]="sidis/expdata/3025.xlsx"  #  compass    proton  pi+    x
conf["datasets"]["sidis"]["xlsx"][3010]="sidis/expdata/3010.xlsx"  #  compass    proton  pi+    z
conf["datasets"]["sidis"]["xlsx"][3012]="sidis/expdata/3012.xlsx"  #  compass    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3005]="sidis/expdata/3005.xlsx"  #  compass    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3013]="sidis/expdata/3013.xlsx"  #  compass    proton  pi-    z
#conf["datasets"]["sidis"]["xlsx"][3024]="sidis/expdata/3024.xlsx"  #   HERMES    proton   k+   pt
#conf["datasets"]["sidis"]["xlsx"][3007]="sidis/expdata/3007.xlsx"  #   HERMES    proton   k+    x
#conf["datasets"]["sidis"]["xlsx"][3008]="sidis/expdata/3008.xlsx"  #   HERMES    proton   k+    z
#conf["datasets"]["sidis"]["xlsx"][3021]="sidis/expdata/3021.xlsx"  #   HERMES    proton   k-   pt
#conf["datasets"]["sidis"]["xlsx"][3017]="sidis/expdata/3017.xlsx"  #   HERMES    proton   k-    x
#conf["datasets"]["sidis"]["xlsx"][3023]="sidis/expdata/3023.xlsx"  #   HERMES    proton   k-    z
conf["datasets"]["sidis"]["xlsx"][3026]="sidis/expdata/3026.xlsx"  #   HERMES    proton  pi+   pt
conf["datasets"]["sidis"]["xlsx"][3000]="sidis/expdata/3000.xlsx"  #   HERMES    proton  pi+    x
conf["datasets"]["sidis"]["xlsx"][3003]="sidis/expdata/3003.xlsx"  #   HERMES    proton  pi+    z
conf["datasets"]["sidis"]["xlsx"][3016]="sidis/expdata/3016.xlsx"  #   HERMES    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3004]="sidis/expdata/3004.xlsx"  #   HERMES    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3018]="sidis/expdata/3018.xlsx"  #   HERMES    proton  pi-    z

for k in conf['datasets']['sia']['xlsx']: conf['datasets']['sia']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1}
for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1}


# Lattice

conf['datasets']['moments']={}
conf['datasets']['moments']['filters']=[]
#conf['datasets']['moments']['filters'][0]['idx']=[1000,1001,1002,1002,1003,1004,1005,1006]

conf['datasets']['moments']['xlsx']={}
conf['datasets']['moments']['xlsx'][1000]='lattice/1000.xlsx'
conf['datasets']['moments']['xlsx'][1001]='lattice/1001.xlsx'
conf['datasets']['moments']['xlsx'][1002]='lattice/1002.xlsx'
#conf['datasets']['moments']['xlsx'][1002]='lattice/1002.xlsx'
#conf['datasets']['moments']['xlsx'][1003]='lattice/1003.xlsx'
#conf['datasets']['moments']['xlsx'][1004]='lattice/1004.xlsx'
conf['datasets']['moments']['xlsx'][1005]='lattice/1005.xlsx'
conf['datasets']['moments']['xlsx'][1006]='lattice/1006.xlsx'

conf['datasets']['moments']['norm']={}
for k in conf['datasets']['moments']['xlsx']: conf['datasets']['moments']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1}
