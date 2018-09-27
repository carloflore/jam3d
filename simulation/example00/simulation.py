#!/usr/bin/env python
import pandas as pd
from fitlab.parman import PARMAN
from fitlab.mcsamp import MCSAMP
from fitlab.maxlike import ML
from tools.config import load_config, conf
from tools.tools import checkdir
from fitlab.resman import RESMAN


############################################################################
# prepare parameters

conf['params']={}
conf['params']['pdf']={}
conf['params']['pdf']['uv widths1']  ={'value':    5.72847e-01,'min': 0,'max':1,'fixed':False}
conf['params']['pdf']['uv widths2']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['pdf']['dv widths1']  ={'value':    5.72847e-01,'min': 0,'max':1,'fixed':'uv widths1'}
conf['params']['pdf']['dv widths2']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'uv widths2'}
conf['params']['pdf']['sea widths1'] ={'value':    6.03974e-01,'min': 0,'max':1,'fixed':False}
conf['params']['pdf']['sea widths2'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}

conf['params']['ff']={}
conf['params']['ff']['pi+fav widths1']   ={'value':    1.16791e-01,'min': 0,'max':1,'fixed':False}
conf['params']['ff']['pi+fav widths2']   ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ff']['pi+unfav widths1'] ={'value':    1.37348e-01,'min': 0,'max':1,'fixed':False}
conf['params']['ff']['pi+unfav widths2'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ff']['k+fav widths1']    ={'value':    1.32925e-01,'min': 0,'max':1,'fixed':False}
conf['params']['ff']['k+fav widths2']    ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ff']['k+unfav widths1']  ={'value':    1.86076e-01,'min': 0,'max':1,'fixed':False}
conf['params']['ff']['k+unfav widths2']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}

############################################################################
# define datasets (kinematics) to perform the simulation

conf['datasets']={}
conf['datasets']['sidis']={}
conf['datasets']['sidis']['xlsx']={}
conf['datasets']['sidis']['xlsx'][1000]='./template.xlsx'  # |  proton   | pi+   
conf['datasets']['sidis']['norm']={}
for idx in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][idx]={'value':1,'fixed':True,'min':0,'max':1} 
conf['datasets']['sidis']['filters']={}


############################################################################
# run simulation
resman = RESMAN()
parman = conf['parman']
resman.get_residuals(parman.par)
print 


############################################################################
# prepare the new pseudo data set and save it as xlsx file
simdata=pd.DataFrame(conf['sidis tabs'][1000])
simdata['value']=simdata['thy']
simdata['stat_u']=pd.Series(simdata['thy']*simdata['%stat']/100,index=simdata.index)
simdata['syst_u']=pd.Series(simdata['thy']*simdata['%syst']/100,index=simdata.index)
simdata=simdata.drop(['r-residuals','shift','alpha','residuals','yp','yh','W2','Shift','N','thy','%stat','%syst'],axis=1)
print simdata[:10]

writer = pd.ExcelWriter('simulation.xlsx')
simdata.to_excel(writer,'Sheet1',index=False)
writer.save()



