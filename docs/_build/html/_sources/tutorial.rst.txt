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

From the commandline ::

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

Workflow
--------

1) Prepare an input file (e.g.  input.py)   

2) Run the executable jam3d (python script) to make a fit or to run an MC analysis. See jam3d -h
   for more info

3) Use a jupyer notebook to study the results

.. %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
.. \begin{frame}
.. \frametitle{\textbf{Workflow}}
.. %------------------------------------------------------------
.. \begin{textblock}{110}(5,12) 
.. 
.. \begin{itemize}
.. \item \textbf{Using Jupyer notebooks}
..       \begin{itemize}
..       \item[+] The core libraries can also be loaded from jupyer notebooks
..       \item[+] The notebooks are more useful for visualization task
..                such as plotting data or TMDs. 
..       \item[+] This is ideal to share the software via \texttt{jupter-hub}
..                servers. 
..       \end{itemize}
.. 
.. \item \textbf{Terminal or jupyter }
..       \begin{itemize}
..       \item[+] In principle all the workflow can be set inside a
..                jupyter notebook without ever need to run programs 
..                from the commandline. 
..       \item[+] However at the beginning of any analysis where one
..                needs to know if a particular implementation of the
..                theory works by fitting the data, it is simpler to check  
..                from commandline if the setup works
..       \item[+] Moreover, for more complex problem where many parameters 
..                are involved in the analysis or a MC sampling is
..                desired, is best to proceed via terminal (specially for
..                very long runs)and use  jupyter-notebooks to post-process the results
..       \end{itemize}
.. \end{itemize}
.. 
.. \end{textblock}
.. %------------------------------------------------------------
.. \end{frame}
.. 
.. 
.. %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
.. \begin{frame}
.. \frametitle{\textbf{Tutorial 1: fits of unpolarized TMDs}}
.. %------------------------------------------------------------
.. \begin{textblock}{110}(5,12) 
.. 
.. \begin{itemize}
.. \item 
.. \end{itemize}
.. 
.. \end{textblock}
.. %------------------------------------------------------------
.. \end{frame}






























