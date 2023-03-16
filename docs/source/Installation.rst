Installation
============

Anaconda
~~~~~~~~


For first-time *conda* users, perform a one-time set up of Bioconda with the following commands:

    conda config --add channels defaults
    conda config --add channels bioconda
    conda config --add channels conda-forge
    conda config --set channel_priority strict


To install `simba <https://anaconda.org/bioconda/simba>`_ with conda, run::

    conda install -c bioconda simba

**Recommended**: install *simba* in a new virtual enviroment::

    conda create -n env_simba python simba
    conda activate env_simba


Dev version
~~~~~~~~~~~

To install the latest version on `GitHub <https://github.com/pinellolab/simba>`_, 

first install `simba_pbg <https://anaconda.org/bioconda/simba_pbg>`_ ::

    conda install -c bioconda simba_pbg


then run::

    git clone https://github.com/pinellolab/simba.git
    pip install simba --user

or::

    pip install git+https://github.com/pinellolab/simba
