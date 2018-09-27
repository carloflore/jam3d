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
# TMD PDF:
conf['params']['pdf']={}
conf['params']['pdf']['widths1_uv']  ={'value':    5.73014e-01,'min': 0,'max':1,'fixed':True}
conf['params']['pdf']['widths2_uv']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['pdf']['widths1_dv']  ={'value':    5.73014e-01,'min': 0,'max':1,'fixed':'widths1_uv'}
conf['params']['pdf']['widths2_dv']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_uv'}
conf['params']['pdf']['widths1_sea'] ={'value':    6.26747e-01,'min': 0,'max':1,'fixed':True}
conf['params']['pdf']['widths2_sea'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}

# TMD FF:
conf['params']['ffpi']={}
conf['params']['ffpi']['widths1_fav']   ={'value':    1.16604e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffpi']['widths2_fav']   ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffpi']['widths1_ufav'] ={'value':    1.37065e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffpi']['widths2_ufav'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffk']={}
conf['params']['ffk']['widths1_fav']    ={'value':    1.32333e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffk']['widths2_fav']    ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffk']['widths1_ufav']  ={'value':    1.85630e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffk']['widths2_ufav']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffh']={}
conf['params']['ffh']['widths1_fav']    ={'value':    1.32925e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffh']['widths2_fav']    ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffh']['widths1_ufav']  ={'value':    1.86073e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffh']['widths2_ufav']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}


# transversty 
conf['params']['transversity']={}
conf['params']['transversity']['widths1_uv']  = {'value': 5.24140000000000050306e-01, 'min':0, 'max':1, 'fixed': False}
conf['params']['transversity']['widths1_dv']  = {'value': 5.24140000000000050306e-01, 'min':0, 'max':1, 'fixed': 'widths1_uv'}
conf['params']['transversity']['widths1_sea'] = {'value': 5.84650000000000003020e-01, 'min':0, 'max':1, 'fixed': False}
conf['params']['transversity']['widths2_uv']  = {'value': 0.0, 'min':0, 'max':1, 'fixed': True}
conf['params']['transversity']['widths2_dv']  = {'value': 0.0, 'min':0, 'max':1, 'fixed': True}
conf['params']['transversity']['widths2_sea'] = {'value': 0.0, 'min':0, 'max':1, 'fixed': True}

conf['params']['transversity']['u N0 1'] = {'value':6.93615720926875667374e+00, 'min': -10.0, 'max': 10.0, 'fixed': False}
conf['params']['transversity']['u N1 1'] = {'value': 0.0, 'min': -10.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u a0 1'] = {'value':7.50418051324418744485e-01, 'min':-2.0, 'max':10.0, 'fixed': False}
conf['params']['transversity']['u a1 1'] = {'value': 0.0, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u b0 1'] = {'value':2.35588099798776795524e+00, 'min': 0.0, 'max':10.0, 'fixed': False}
conf['params']['transversity']['u b1 1'] = {'value': 0.0, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u c0 1'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u c1 1'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u d0 1'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u d1 1'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u N0 2'] = {'value': 0.0, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u N1 2'] = {'value': 0.0, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u a0 2'] = {'value': 0.0, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u a1 2'] = {'value': 0.0, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u b0 2'] = {'value': 0.0, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u b1 2'] = {'value': 0.0, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u c0 2'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u c1 2'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u d0 2'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u d1 2'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}


conf['params']['transversity']['d N0 1'] = {'value': -5.76636326391826070648e+00, 'min': -10.0, 'max': 10.0, 'fixed': False}
conf['params']['transversity']['d N1 1'] = {'value': 0.0, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d a0 1'] = {'value':2.50990802211820351886e-01, 'min':-2.0, 'max':10.0, 'fixed': False}
conf['params']['transversity']['d a1 1'] = {'value': 0.0, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['d b0 1'] = {'value':7.32587435823372068455e+00, 'min': 0.0, 'max':10.0, 'fixed': False}
conf['params']['transversity']['d b1 1'] = {'value': 0.0, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['d c0 1'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d c1 1'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d d0 1'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d d1 1'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d N0 2'] = {'value': 0.0, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d N1 2'] = {'value': 0.0, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d a0 2'] = {'value': 0.0, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['d a1 2'] = {'value': 0.0, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['d b0 2'] = {'value': 0.0, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['d b1 2'] = {'value': 0.0, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['d c0 2'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d c1 2'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d d0 2'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d d1 2'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}


conf['params']['transversity']['s N0 1'] = {'value':-1.09888581504296936608e-01, 'min': -10.0, 'max': 10.0, 'fixed': False}
conf['params']['transversity']['s N1 1'] = {'value': 0.0, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s a0 1'] = {'value':-2.15235869713699123906e-01, 'min':-2.0, 'max':10.0, 'fixed': False}
conf['params']['transversity']['s a1 1'] = {'value': 0.0, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s b0 1'] = {'value': 0.0, 'min': 0.0, 'max':10.0, 'fixed': False}
conf['params']['transversity']['s b1 1'] = {'value': 0.0, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s c0 1'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s c1 1'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s d0 1'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s d1 1'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s N0 2'] = {'value': 0.0, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s N1 2'] = {'value': 0.0, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s a0 2'] = {'value': 0.0, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s a1 2'] = {'value': 0.0, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s b0 2'] = {'value': 0.0, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s b1 2'] = {'value': 0.0, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s c0 2'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s c1 2'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s d0 2'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s d1 2'] = {'value': 0.0, 'min':-1.0, 'max': 1.0, 'fixed': True}



# COLLINS TMD FF:
conf['params']['collinspi']={}

conf['params']['collinspi']['widths1_fav']   = {'value': 7.69e-02,'min':0, 'max':1, 'fixed':False}
conf['params']['collinspi']['widths1_ufav'] = {'value':  7.82e-02,'min':0, 'max':1, 'fixed':False}
conf['params']['collinspi']['widths2_fav']   = {'value':  0.0,'min':0, 'max':1, 'fixed':True}
conf['params']['collinspi']['widths2_ufav'] = {'value':  0.0,'min':0, 'max':1, 'fixed':True}

conf['params']['collinspi']['u N0 1'] = {'value': 7.27e-01,'min': -15, 'max': 2, 'fixed':False}
conf['params']['collinspi']['u N1 1'] = {'value':  0.0,'min': -10, 'max': 10, 'fixed':True}
conf['params']['collinspi']['u a0 1'] = {'value':  -1.8529e+00,'min':-2.5, 'max': 5, 'fixed':False}
conf['params']['collinspi']['u a1 1'] = {'value':  0.0,'min':-2, 'max': 5, 'fixed':True}
conf['params']['collinspi']['u b0 1'] = {'value':  5.3918e+00,'min': 0, 'max':10, 'fixed':False}
conf['params']['collinspi']['u b1 1'] = {'value':  0.0,'min': 0, 'max':10, 'fixed':True}
conf['params']['collinspi']['u c0 1'] = {'value':  0.0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u c1 1'] = {'value':  0.0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u d0 1'] = {'value':  0.0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u d1 1'] = {'value':  0.0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u N0 2'] = {'value': 1.05827284963755605673e+01,'min': -10, 'max': 10, 'fixed':False}
conf['params']['collinspi']['u N1 2'] = {'value': 0,'min': 0, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u a0 2'] = {'value': 7.94843162206008546633e+00,'min':-2, 'max': 20, 'fixed':False}
conf['params']['collinspi']['u a1 2'] = {'value': 0,'min':-2, 'max': 2, 'fixed':True}
conf['params']['collinspi']['u b0 2'] = {'value': 3.00185190517106192942e+00,'min': 0, 'max':10, 'fixed':False}
conf['params']['collinspi']['u b1 2'] = {'value': 0,'min': 0, 'max':10, 'fixed':True}
conf['params']['collinspi']['u c0 2'] = {'value': 0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u c1 2'] = {'value': 0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u d0 2'] = {'value': 0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u d1 2'] = {'value': 0,'min':-1, 'max': 1, 'fixed':True}

conf['params']['collinspi']['d N0 1'] = {'value':  -3.43290097947612160567e+00,'min': -10, 'max': 10, 'fixed':False}
conf['params']['collinspi']['d N1 1'] = {'value':  0.0,'min': 0, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d a0 1'] = {'value':  1.07876853314680998253e+00,'min':-2, 'max': 2, 'fixed':False}
conf['params']['collinspi']['d a1 1'] = {'value':  0.0,'min':-2, 'max': 2, 'fixed':True}
conf['params']['collinspi']['d b0 1'] = {'value':  3.00e+00,'min': 0, 'max':10, 'fixed':False}
conf['params']['collinspi']['d b1 1'] = {'value':  0.0,'min': 0, 'max':10, 'fixed':True}
conf['params']['collinspi']['d c0 1'] = {'value':  0.0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d c1 1'] = {'value':  0.0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d d0 1'] = {'value':  0.0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d d1 1'] = {'value':  0.0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d N0 2'] = {'value': 0,'min': 0, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d N1 2'] = {'value': 0,'min': 0, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d a0 2'] = {'value': 0,'min':-2, 'max': 2, 'fixed':True}
conf['params']['collinspi']['d a1 2'] = {'value': 0,'min':-2, 'max': 2, 'fixed':True}
conf['params']['collinspi']['d b0 2'] = {'value': 0,'min': 0, 'max':10, 'fixed':True}
conf['params']['collinspi']['d b1 2'] = {'value': 0,'min': 0, 'max':10, 'fixed':True}
conf['params']['collinspi']['d c0 2'] = {'value': 0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d c1 2'] = {'value': 0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d d0 2'] = {'value': 0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d d1 2'] = {'value': 0,'min':-1, 'max': 1, 'fixed':True}

conf['params']['collinspi']['s N0 1'] = {'value':  0.0,'min': 0, 'max': 1, 'fixed':False}
conf['params']['collinspi']['s N1 1'] = {'value':  0.0,'min': 0, 'max': 1, 'fixed':True}
conf['params']['collinspi']['s a0 1'] = {'value': -0.5,'min':-2, 'max': 2, 'fixed':False}
conf['params']['collinspi']['s a1 1'] = {'value':  0.0,'min':-2, 'max': 2, 'fixed':True}
conf['params']['collinspi']['s b0 1'] = {'value':  3.0,'min': 0, 'max':10, 'fixed':False}
conf['params']['collinspi']['s b1 1'] = {'value':  0.0,'min': 0, 'max':10, 'fixed':True}
conf['params']['collinspi']['s c0 1'] = {'value':  0.0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['s c1 1'] = {'value':  0.0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['s d0 1'] = {'value':  0.0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['s d1 1'] = {'value':  0.0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['s N0 2'] = {'value': 0,'min': 0, 'max': 1, 'fixed':True}
conf['params']['collinspi']['s N1 2'] = {'value': 0,'min': 0, 'max': 1, 'fixed':True}
conf['params']['collinspi']['s a0 2'] = {'value': 0,'min':-2, 'max': 2, 'fixed':True}
conf['params']['collinspi']['s a1 2'] = {'value': 0,'min':-2, 'max': 2, 'fixed':True}
conf['params']['collinspi']['s b0 2'] = {'value': 0,'min': 0, 'max':10, 'fixed':True}
conf['params']['collinspi']['s b1 2'] = {'value': 0,'min': 0, 'max':10, 'fixed':True}
conf['params']['collinspi']['s c0 2'] = {'value': 0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['s c1 2'] = {'value': 0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['s d0 2'] = {'value': 0,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['s d1 2'] = {'value': 0,'min':-1, 'max': 1, 'fixed':True}





############################################################################
# set data sets

conf['datasets']={}

# SIDIS
conf['datasets']['sidis']={}
conf['datasets']['sidis']['norm']={}
conf['datasets']['sidis']['xlsx']={}
conf['datasets']['sidis']['filters']={}


# Collins Asy
#conf["datasets"]["sidis"]["xlsx"][4007]="sidis/expdata/4007.xlsx"  #  compass  deuteron   k+   pT
#conf["datasets"]["sidis"]["xlsx"][4006]="sidis/expdata/4006.xlsx"  #  compass  deuteron   k+    x
#conf["datasets"]["sidis"]["xlsx"][4008]="sidis/expdata/4008.xlsx"  #  compass  deuteron   k+    z
#conf["datasets"]["sidis"]["xlsx"][4010]="sidis/expdata/4010.xlsx"  #  compass  deuteron   k-   pT
#conf["datasets"]["sidis"]["xlsx"][4009]="sidis/expdata/4009.xlsx"  #  compass  deuteron   k-    x
#conf["datasets"]["sidis"]["xlsx"][4011]="sidis/expdata/4011.xlsx"  #  compass  deuteron   k-    z
conf["datasets"]["sidis"]["xlsx"][4001]="sidis/expdata/4001.xlsx"  #  compass  deuteron  pi+  pT
conf["datasets"]["sidis"]["xlsx"][4000]="sidis/expdata/4000.xlsx"  #  compass  deuteron  pi+   x
conf["datasets"]["sidis"]["xlsx"][4002]="sidis/expdata/4002.xlsx"  #  compass  deuteron  pi+   z
conf["datasets"]["sidis"]["xlsx"][4004]="sidis/expdata/4004.xlsx"  #  compass  deuteron  pi-   pT
conf["datasets"]["sidis"]["xlsx"][4003]="sidis/expdata/4003.xlsx"  #  compass  deuteron  pi-    x
conf["datasets"]["sidis"]["xlsx"][4005]="sidis/expdata/4005.xlsx"  #  compass  deuteron  pi-    z
#conf["datasets"]["sidis"]["xlsx"][6003]="sidis/expdata/6003.xlsx"  #  compass    proton   k+   pt
#conf["datasets"]["sidis"]["xlsx"][6004]="sidis/expdata/6004.xlsx"  #  compass    proton   k+    x
#conf["datasets"]["sidis"]["xlsx"][6005]="sidis/expdata/6005.xlsx"  #  compass    proton   k+    z
#conf["datasets"]["sidis"]["xlsx"][6000]="sidis/expdata/6000.xlsx"  #  compass    proton   k-   pt
#conf["datasets"]["sidis"]["xlsx"][6001]="sidis/expdata/6001.xlsx"  #  compass    proton   k-    x
#conf["datasets"]["sidis"]["xlsx"][6002]="sidis/expdata/6002.xlsx"  #  compass    proton   k-    z
conf["datasets"]["sidis"]["xlsx"][3027]="sidis/expdata/3027.xlsx"  #  compass    proton    pt
conf["datasets"]["sidis"]["xlsx"][3025]="sidis/expdata/3025.xlsx"  #  compass    proton     x
conf["datasets"]["sidis"]["xlsx"][3010]="sidis/expdata/3010.xlsx"  #  compass    proton     z
conf["datasets"]["sidis"]["xlsx"][3012]="sidis/expdata/3012.xlsx"  #  compass    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3005]="sidis/expdata/3005.xlsx"  #  compass    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3013]="sidis/expdata/3013.xlsx"  #  compass    proton  pi-    z
#conf["datasets"]["sidis"]["xlsx"][3024]="sidis/expdata/3024.xlsx"  #   HERMES    proton   k+   pt
#conf["datasets"]["sidis"]["xlsx"][3007]="sidis/expdata/3007.xlsx"  #   HERMES    proton   k+    x
#conf["datasets"]["sidis"]["xlsx"][3008]="sidis/expdata/3008.xlsx"  #   HERMES    proton   k+    z
#conf["datasets"]["sidis"]["xlsx"][3021]="sidis/expdata/3021.xlsx"  #   HERMES    proton   k-   pt
#conf["datasets"]["sidis"]["xlsx"][3017]="sidis/expdata/3017.xlsx"  #   HERMES    proton   k-    x
#conf["datasets"]["sidis"]["xlsx"][3023]="sidis/expdata/3023.xlsx"  #   HERMES    proton   k-    z
conf["datasets"]["sidis"]["xlsx"][3026]="sidis/expdata/3026.xlsx"  #   HERMES    proton pi+   pt
conf["datasets"]["sidis"]["xlsx"][3000]="sidis/expdata/3000.xlsx"  #   HERMES    proton pi+    x
conf["datasets"]["sidis"]["xlsx"][3003]="sidis/expdata/3003.xlsx"  #   HERMES    proton pi+    z
conf["datasets"]["sidis"]["xlsx"][3016]="sidis/expdata/3016.xlsx"  #   HERMES    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3004]="sidis/expdata/3004.xlsx"  #   HERMES    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3018]="sidis/expdata/3018.xlsx"  #   HERMES    proton  pi-    z
for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1}
conf['datasets']['sidis']['filters'][0]={}
conf['datasets']['sidis']['filters'][0]['idx']=[4001,4000,4002,4004,4003,4005,3027,3025,3010,3012,3005,3013,3026,3000,3003,3016,3004,3018]
conf['datasets']['sidis']['filters'][0]['filter']="z>0.2 and z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"


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
