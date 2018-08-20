conf={}

############################################################################
#mcsamp
conf['ncpu']=10
conf['nruns']=1
conf['factor']=4.0
conf['kappa']=1.5
conf['tol']=1e-10
conf['itmax']=int(1e7)
conf['block size']=10

############################################################################
# params

conf['params']={}

conf['params']['pdf']={}
conf['params']['pdf']['widths1 uv']  ={'value':    3.87639e-01,'min':0,'max':1,'fixed':False}
conf['params']['pdf']['widths1 dv']  ={'value':    3.87639e-01,'min':0,'max':1,'fixed':'widths1 uv'}
conf['params']['pdf']['widths1 sea'] ={'value':    7.54262e-01,'min':0,'max':1,'fixed':False}
conf['params']['pdf']['widths2 uv']  ={'value':    1.80589e-01,'min':-1,'max':1,'fixed':False}
conf['params']['pdf']['widths2 dv']  ={'value':    3.87639e-01,'min':-1,'max':1,'fixed':'widths1 uv'}
conf['params']['pdf']['widths2 sea'] ={'value':   -2.62630e-01,'min':-1,'max':1,'fixed':False}


conf['params']['ff']={}
conf['params']['ff']['widths1 pi+fav']   ={'value':    1.51632e-01,'min':0,'max':1,'fixed':False}
conf['params']['ff']['widths1 pi+unfav'] ={'value':    1.23832e-01,'min':0,'max':1,'fixed':False}
conf['params']['ff']['widths2 pi+fav']   ={'value':   -4.10924e-02,'min':0,'max':1,'fixed':False}
conf['params']['ff']['widths2 pi+unfav'] ={'value':    1.29717e-02,'min':0,'max':1,'fixed':False}
conf['params']['ff']['widths1 k+fav']    ={'value':    1.58596e-01,'min':0,'max':1,'fixed':False}
conf['params']['ff']['widths1 k+unfav']  ={'value':    1.68915e-01,'min':-1,'max':1,'fixed':False}
conf['params']['ff']['widths2 k+fav']    ={'value':   -3.27346e-02,'min':-1,'max':1,'fixed':False}
conf['params']['ff']['widths2 k+unfav']  ={'value':    2.06972e-02,'min':-1,'max':1,'fixed':False}

############################################################################
# set data sets

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
for idx in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][idx]={'value':1,'fixed':True,'min':0,'max':1} 

conf['datasets']['sidis']['filters']={}
for idx in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['filters'][idx]="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"







