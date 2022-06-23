# Reproduction repository for "Diagnosing the interstellar medium of galaxies with far-infrared emission lines III. Physical parameters of observed galaxies"

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/aframosp/Analysis_DiagISM/HEAD)
<!-- [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5227294.svg)](https://doi.org/10.5281/zenodo.5227294) -->

[![DOI](https://zenodo.org/badge/506689031.svg)](https://zenodo.org/badge/latestdoi/506689031)


This repository contains data and code to reproduce the results of the research "[Diagnosing the interstellar medium of galaxies with far-infrared emission lines III. Physical parameters of observed galaxies]()". Each step of the work is described in a [step-by-step](StepByStep.md) file with their respective [Jupyter notebooks](/notebooks).

## Software requirements

The most important software packages to work with the files in this repository are in [environment.yml](environment.yml). This file is also used to launch a [Binder](https://mybinder.org/) to open the Jupyter notebooks interactively. We print all the packages in a given notebook using the IPython magic extension [watermark](https://github.com/rasbt/watermark). We also use [autotpep8](https://pypi.org/project/autopep8/) to format the code to the PEP 8 style guide. 


## Repository Organization
The following is the organization of the repository with a simple description of the files or folder contents 

    .
    ├── CITATION.cff       <- Metadata for citation
    ├── LICENSE            <- License file
    ├── environment.yml    <- File containing the required software
    ├── README.md          <- This file
    ├── StepByStep.md      <- File describing the steps taken in this work
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed
    │   ├── processed      <- Results from DiagISM and final data
    │   └── raw            <- Original data from Paper II
    ├── notebooks          <- Jupyter notebooks
    └── figures            <- Figures created from the Jupyter notebooks

## Estimated physical parameters
The file containing the estimated physical parameters from the observational sample can be found in the [predictions_DiagISM_obsSample.csv](/data/processed) file.

## Missing data
Unfortunately not all the raw data is available in the repository. Data from the SIDES lightcone catalog is ~2Gb, then we decided not to included in this repository, but if you want to use it you can check the [webpage](https://cesamsi.lam.fr/instance/sides/home) to obtain the catalogue.

Beside this, the mock_sample.csv file is not stored in Github (~100Mb) and need to be stored locally by running the notebook [AppA_Predictions_newlinreg](/notebooks/AppA_Predictions_newlinreg.ipynb).