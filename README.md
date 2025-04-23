# Financial distress precition
Based on Give Me Some Credit Kaggle competition. Goal is to predict whether a person will experience financial distress in the next two years.

Imbalanced dataset, linear inseparability, low correlation of input and target features, and large outliers make this classification task quite a challange. Exploratory data analysis along with PCA analysis were performed to gain some top down insights into the data along with statistical tests (nonparametric t-test alternative, Mann Whitney U-test).

To prepare data for the modelling phase, some feature engineering was done: new feature was introduced (based on number of times customer was late with downpayments in the past), data was scaled, missling values were imputed and outliers (top quantiles) of extremely skewed features were removed. 

In the modelling phase, baseline logistic regression model was developed which immediately showed problems related to an imbalanced dataset (low precision or accuracy). SMOTE method was not used, but insted class imbalance was handled with increased weights of minority class.

Cross validation grid search was performed to find the best model between logistic regression, random forest and a decision tree classifier.

## Available notebooks
* Notebook 1: Exploratory data analysis
    *  Data and outlier visualisation, feature correlation heatmap, PCA analysis and statistical tests
* Notebook 2: Data preparation and feature engineering
    * Feature engineering, data scaling and outlier removal
* Notebook 3: Baseline model
    * Creation of a baseline logistic regression model
* Notebook 4: Model selection
    * Model selection based on cross validation

## Models used
* Logistic regression
* Random forest classifier
* Decision tree classifier
