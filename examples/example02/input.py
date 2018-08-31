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

############################################################################
# params

conf['params']={}
# Parameters in gaussian approximation, parton model:
conf['params']['pdf']={}
conf['params']['pdf']['uv widths1']  ={'value':    3.99391e-01,'min': 0,'max':1,'fixed':False}
conf['params']['pdf']['uv widths2']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['pdf']['dv widths1']  ={'value':    3.99391e-01,'min': 0,'max':1,'fixed':'uv widths1'}
conf['params']['pdf']['dv widths2']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'uv widths2'}
conf['params']['pdf']['sea widths1'] ={'value':    5.44764e-01,'min': 0,'max':1,'fixed':False}
conf['params']['pdf']['sea widths2'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}

conf['params']['ff']={}
conf['params']['ff']['pi+fav widths1']   ={'value':    1.26522e-01,'min': 0,'max':1,'fixed':False}
conf['params']['ff']['pi+fav widths2']   ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ff']['pi+unfav widths1'] ={'value':    1.62336e-01,'min': 0,'max':1,'fixed':False}
conf['params']['ff']['pi+unfav widths2'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ff']['k+fav widths1']    ={'value':    1.39083e-01,'min': 0,'max':1,'fixed':False}
conf['params']['ff']['k+fav widths2']    ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ff']['k+unfav widths1']  ={'value':    2.24566e-01,'min': 0,'max':1,'fixed':False}
conf['params']['ff']['k+unfav widths2']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}

############################################################################
# set data sets

conf['datasets']={}
conf['datasets']['sidis']={}

# The data sets to use are here:
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
# The cuts you want to impose on the data are here:
for idx in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['filters'][idx]="z>0.2 and z<0.6 and Q2>1.69 and (pT/z)**2>0.25*Q2 and dy>2.5"






