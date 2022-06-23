# Step-By-Step

This file works as a Table of contents (TOC) to follow the procedures done to reproduce the information presented in the paper. The numbers on this TOC are the same as in the [Jupyter notebooks](/notebooks). Each subseccion related to a [data](/data) or [figure](/figures) file is indicated with a '=>'. Keep in mind that after step 4, it is necessary to have run the Appendix A notebook.

Paper II refers to the [data](https://zenodo.org/record/6576202) and description presented in the previous [research article](https://arxiv.org/abs/2205.11955) of the series on "Diagnosing the interstellar medium of galaxies with far-infrared emission lines".

## TOC
1) [Estimate Hyperparameters](/notebooks/1_Hyperparameters_MLP.ipynb)
* 1.1 Read the observational dataset from [Paper II](https://zenodo.org/record/6576202#.YqyFgezP1TY) 
* 1.2 Obtain the hyperparameters with [ATOM](https://tvdboom.github.io/ATOM) => [Hyperparameters_table.csv](/data/interim)
2) [Create pickle file for the pre-trained model](/notebooks/2_Pickle_file.ipynb)
* 2.1 Read data
* 2.2 Train models
* 2.3 Save file => [AllLines_trained](/data/interim)
3) [Results from the web app in simulated data](/notebooks/3_Results_webapp_simulations.ipynb)
* 3.1 Read simulation file dataset from [Paper II](https://zenodo.org/record/6576202#.YqyFgezP1TY) and create the input files for the DiagISM web app => [Simdata_set_*.txt](/data/interim/inputs_DiagISM)
* 3.2 Results from assumed error [FIGURE 2](/figures/Sigma.pdf)
* 3.3 Results from the metrics
* 3.4 Difference between the estimates [FIGURE 3](/figures/Difference_parameters_M8all.pdf) and [FIGURE 4](figures/Difference_parameters_M2plus.pdf)
4) [Results from the web app in observational data](/notebooks/4_Results_webapp.ipynb)
* 4.1 Read observational dataset from [Paper II](https://zenodo.org/record/6576202#.YqyFgezP1TY) and create the input files for the DiagISM web app => [Obsdata_set_*.txt](/data/interim/inputs_DiagISM)
* 4.2 Results from the metrics TABLE 2
* 4.3 Verify the error estimations
* 4.4 Verify the error in other physical parameters
* 4.5 Correlation between observed and predicted values [FIGURE 6](/figures/True_predictions.pdf)
* 4.6 Predictions for observational sample (set B) => [predictions_DiagISM_obsSample.csv](/data/processed), [predictions.tex TABLE 3](/data/processed) and [FIGURE B1](/figures/Observations_predictions.pdf)
* 4.7 Reference selected images DiagISM, information for comparing FIGURE 5
5) [Estimates of the sensitivity](/notebooks/5_Estimate_sensitivity_data.ipynb)
* 5.1 Reading and pre-processing data
* 5.2 Using the estimator to calculate the bands sensitivies => [NcountsMay_SIDES_LETO_percentiles_poisson*.npy](../data/processed)
6) [Sentivitities analysis](/notebooks/6_Sensitivities_analysis.ipynb)
* 6.1 PRIMA configuration
* 6.2 Counts tables => [Example_counts.tex TABLE 5](/data/processed)
* 6.3 Counts plots => [FIGURE 8](/figures/Counts.pdf)
7) [Comparison between different LCII estimates](/notebooks/7_Comparison_SIDES_LCII.ipynb)
* 7.1 Read SIDES data
* 7.2 Check information of the catalogue
* 7.3 Estimate luminosities with MLP
* 7.4 Comparison plots => [FIGURE 7](/figures/Comparison_LCII.pdf)

AppA) [Create mock for DiagISM](/notebooks/AppA_Predictions_newlinreg.ipynb)
* AppA.1 Read simulation file dataset from [Paper II](https://zenodo.org/record/6576202#.YqyFgezP1TY)
* AppA.2 Create the mock catalog => [mock_sample.csv](/data/interim)
* AppA.3 Obtaining the polynomial regression => [coeff_MLPreg.csv](/data/interim) and [coeff_MLPreg_latex.tex TABLE A1](/data/interim)