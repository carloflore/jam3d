examples
========

example00
---------

Lets examine the input.py provided at ::

  examples/examples00/input.py


At the top we have 

.. code-block:: python

  conf={}

This dictionary serves as a common block in the sense of fortran programming with 
the difference that we will be able to add not just numbers but also class objects

We next specify the number of CPU (logical-cores) to be used

.. code-block:: python
  
  conf['ncpu']=2

The next part is only relevant for MC runs  

.. code-block:: python
  
  conf['nruns']=1
  conf['factor']=4.0
  conf['kappa']=1.5
  conf['tol']=1e-10
  conf['itmax']=int(1e7)
  conf['block size']=10
  conf['nll shift']=0


Proceed to specify the parameters to be fitted

.. code-block:: python
  
  
  conf['params']={}
  
  conf['params']['pdf']={}
  conf['params']['pdf']['widths1 uv']  ={'value':    3.90812e-01,'min':0,'max':1,'fixed':False}
  conf['params']['pdf']['widths1 dv']  ={'value':    3.90812e-01,'min':0,'max':1,'fixed':'widths1 uv'}
  conf['params']['pdf']['widths1 sea'] ={'value':    8.14534e-01,'min':0,'max':1,'fixed':False}
  conf['params']['pdf']['widths2 uv']  ={'value':    1.72798e-01,'min':0,'max':1,'fixed':False}
  conf['params']['pdf']['widths2 dv']  ={'value':    3.90812e-01,'min':0,'max':1,'fixed':'widths1 uv'}
  conf['params']['pdf']['widths2 sea'] ={'value':   -3.44763e-01,'min':0,'max':1,'fixed':False}
  
  
  conf['params']['ff']={}
  conf['params']['ff']['widths1 pi+ fav']   ={'value':    1.50893e-01,'min':0,'max':1,'fixed':False}
  conf['params']['ff']['widths1 pi+ unfav'] ={'value':    1.22787e-01,'min':0,'max':1,'fixed':False}
  conf['params']['ff']['widths2 pi+ fav']   ={'value':   -3.99747e-02,'min':0,'max':1,'fixed':False}
  conf['params']['ff']['widths2 pi+ unfav'] ={'value':    1.42020e-02,'min':0,'max':1,'fixed':False}
  conf['params']['ff']['widths1 k+ fav']    ={'value':    1.34063e-01,'min':0,'max':1,'fixed':True}
  conf['params']['ff']['widths1 k+ unfav']  ={'value':    1.87915e-01,'min':0,'max':1,'fixed':True}
  conf['params']['ff']['widths2 k+ fav']    ={'value':    0.00000e+00,'min':0,'max':1,'fixed':True}
  conf['params']['ff']['widths2 k+ unfav']  ={'value':    0.00000e+00,'min':0,'max':1,'fixed':True}
  

Finally we setup the data sets to be include in the chi2 minimazation

.. code-block:: python
  
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




















