|CI| |Docs| |Anaconda| |Install with conda| |Codecov| |Last updated| |Downloads| |License|

**SIMBA**: **SI**\ ngle-cell e\ **MB**\ edding **A**\ long with features
========================================================================

SIMBA is a method to embed cells along with their defining features such as gene expression, transcription factor binding sequences and chromatin accessibility peaks into the same latent space. The joint embedding of cells and features allows SIMBA to perform various types of single cell tasks, including but not limited to single-modal analysis (e.g. scRNA-seq and scATAC-seq analysis), multimodal analysis, batch correction, and multi-omic integration.


.. image:: _static/img/Figure1.png
   :align: center
   :width: 600
   :alt: SIMBA overview


.. toctree::
   :maxdepth: 2
   :caption: Overview
   :hidden:

   About SIMBA
   Installation
   API
   Release notes
   Citation


.. toctree::
   :maxdepth: 1
   :caption: SIMBA primer

   Basic concepts
   Output


.. toctree::
   :maxdepth: 1
   :caption: Tutorials

   rna_10xpmbc_all_genes_v1.2
   atac_buenrostro2018_peaks_and_sequences
   multiome_shareseq
   multiome_shareseq_GRN
   rna_mouse_atlas
   rna_human_pancreas
   multiome_10xpmbc10k_integration
   new_graph_generation
   rna_10xpmbc_edgeweigts
   rna_10x_mouse_brain_1p3M


.. |Docs| image:: https://readthedocs.org/projects/simba-bio/badge/?version=latest
   :target: https://simba-bio.readthedocs.io

.. |CI| image:: https://github.com/pinellolab/simba/actions/workflows/CI.yml/badge.svg
   :target: https://github.com/pinellolab/simba/actions/workflows/CI.yml

.. |Anaconda| image:: https://anaconda.org/bioconda/simba/badges/version.svg
   :target: https://anaconda.org/bioconda/simba

.. |Install with conda| image:: https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat
   :target: http://bioconda.github.io/recipes/simba/README.html

.. |Last updated| image:: https://anaconda.org/bioconda/simba/badges/latest_release_date.svg
   :target: https://anaconda.org/bioconda/simba

.. |License| image:: https://anaconda.org/bioconda/simba/badges/license.svg
   :target: https://github.com/pinellolab/simba/blob/master/LICENSE

.. |Downloads| image:: https://anaconda.org/bioconda/simba/badges/downloads.svg
   :target: https://anaconda.org/bioconda/simba

.. |Codecov| image:: https://codecov.io/gh/huidongchen/simba/branch/master/graph/badge.svg?token=ZUA70S1LUU
   :target: https://codecov.io/gh/huidongchen/simba
