Tutorial
========

Dependencies
------------

- Only Linux and OSX is supported

- We recommend to install anacoda (python2) which 
  comes will all the necessary libraries

- A fortran compiler (gfortran) 

Installation
------------

Clone the codes from https://github.com/JeffersonLab/jam3d


From the command line ::

  cd external  ./install

Enviroment variables needs to be set in your terminal session. 
For bash they are ::

  export FITPACK=path2fitpack
  PYTHONPATH=$FITPACK:$PYTHONPATH
  export PATH=$FITPACK/bin:$PATH

Alternatively you can source the setup files ::

  source  setup.bash 

Once the enviroment variables are set the scripts can be called from 
anywhere in your system. In other words, there is no need to work within 
the same code folder. As a good practice, create dedicated folders for a
given analysis. 

Basic workflow
--------------

1) Prepare an input file (e.g.  input.py)   

2) Run the executable jam3d (python script) to make a fit or to run an MC analysis. See jam3d -h
   for more info

3) Use a jupyer notebook to study the results






