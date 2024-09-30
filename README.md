# Business Validation Machine Learning Models
![image](https://github.com/user-attachments/assets/710e27a2-2864-4962-9467-2546462cac56)


This repository contains a machine learning application developed as part of a college assignment to determine whether a business is validated or not, utilizing the Yelp dataset. The project implements various algorithms, including Decision Trees, Random Forests, AdaBoost, and XGBoost, and compares their feature importances using LIME and SHAP.

## Project Overview

In this project, we aim to achieve the following objectives:

- **Data Exploration and Preprocessing**: Analyze the Yelp dataset to understand the features and their distributions, ensuring appropriate preprocessing and feature engineering are applied before model training.
- **Model Implementation**: Build and evaluate multiple machine learning models:
  - Decision Tree
  - Random Forest
  - AdaBoost
  - XGBoost
- **Feature Importance Analysis**: Examine feature importance generated from Decision Trees, Random Forests, and Boosting techniques. Additionally, use LIME and SHAP for comparison.
- **Empirical Tuning**: Conduct three rounds of empirical tuning on all models to optimize performance.

## Dataset

The data used for this project is sourced from the [Yelp Dataset](https://www.yelp.com/dataset/download). Please follow the link to download the dataset for local use.

## Requirements

To run the notebooks, ensure you have the following Python packages installed:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- lime
- shap

You can install the required packages using pip:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost lime shap
