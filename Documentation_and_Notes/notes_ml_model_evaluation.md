# Overview

A short overview of the trained models and how they perform on the test data.

## Scoring and evaluation

Considering the errors by creating the table ```df_compare``` in [ml_model_evaluation.py](../Workplace/ml_model_evaluation.py),
allows us to make a statistical analysis.
Thus, we consider the following table:

| model                     |   MAE |   R² |    MSE |   RMSE | Median | abs median | abs min |   abs max |  % error < 0.1 | % error < 0.2 | % error < 0.3 | % error > 0.5 |
|---------------------------|------:|-----:|-------:|-------:|-------:|-----------:|--------:|----------:|---------------:|--------------:|--------------:|--------------:|
| Linear Regression         | 0.411 | 0.64 |   0.30 |  0.548 | -0.055 |      0.332 |       0 |     3.691 |          0.167 |         0.316 |         0.453 |         0.309 |
| Neuronal Net              | 0.341 | 0.74 |   0.22 |  0.469 | -0.034 |      0.260 |       0 |     4.234 |          0.214 |         0.394 |         0.567 |         0.220 |
| Decision Tree             | 0.389 | 0.67 |   0.28 |  0.529 | -0.034 |      0.302 |       0 |     3.593 |          0.193 |         0.352 |         0.497 |         0.267 |
| Random Forest             | 0.363 | 0.71 |  0.241 |  0.491 | -0.033 |      0.286 |   0.001 |     3.581 |          0.190 |         0.381 |         0.524 |         0.242 |
| Gradient Boosting         | 0.315 | 0.78 |  0.184 |  0.429 | -0.019 |      0.239 |       0 |     2.807 |          0.224 |         0.428 |         0.588 |         0.193 |
| Elastic Net               | 0.412 | 0.64 |  0.303 |  0.550 | -0.046 |      0.334 |       0 |     3.807 |          0.161 |         0.318 |         0.465 |         0.315 |
| SVR                       | 0.352 | 0.71 |  0.247 |  0.497 | -0.026 |      0.263 |       0 |     4.430 |          0.206 |         0.389 |         0.553 |         0.226 |
| Extreme Gradient Boosting | 0.303 | 0.79 |  0.173 |  0.416 | -0.015 |      0.231 |       0 |     3.139 |          0.248 |         0.453 |         0.610 |         0.193 |
| Combined Mean             | 0.323 | 0.00 |  0.199 |  0.446 | -0.036 |      0.246 |       0 |     3.660 |          0.225 |         0.418 |         0.580 |         0.206 |
| Combined Biased Mean      | 0.316 | 0.00 |  0.191 |  0.437 | -0.032 |      0.241 |       0 |     3.637 |          0.223 |         0.429 |         0.589 |         0.195 |

**Combined Mean**:
Average of all trained models.

**Combined Biased Mean**:
Biased average of all trained models using the R² score given by the cross validation in the gridsearch in [ml_model_parameter_search.py](../Workplace/ml_model_parameter_search.py) and in [notes_ml_gridsearch](notes_ml_gridsearch.md).

### Focusing on **Extreme Gradient Boosting**

Best overall performance among all models across most metrics.

- Lowest **Mean Absolute Error (MAE): `0.303`
- Highest R² score: `0.79`
  - Explains the highest proportion of variance in the target variable, making it the most predictive model in the group.
- Lowest Mean Squared Error (MSE): `0.173`
- Lowest Root Mean Squared Error (RMSE): `0.416`
- Median Error: `-0.015`
  - Slightly underestimates on average, but the bias is minimal.
- Lowest Absolute Median Error: `0.231`
  - Reflecting consistent performance.
- Absolute Min Error: `0`
  - Some predictions are perfectly accurate.
- Absolute Max Error: `3.139`
  - Lower than most models (except Gradient Boosting), indicating fewer extreme mispredictions.
- % of Predictions with Error < 0.1: `24.8%`
  - Highest among all models, showing high accuracy.
- % of Predictions with Error < 0.2: `45.3%`
  - Again, the highest, suggesting more than 45% of predictions are within a `0.2` error range.
- % of Predictions with Error < 0.3: `61.0%`
  - Best model for moderate accuracy tolerance.
- % of Predictions with Error > 0.5: `19.3%`
  - Among the lowest, tied with Gradient Boosting, showing few large deviations.


Extreme Gradient Boosting demonstrates the best trade-off between accuracy, error distribution, and consistency. 
It outperforms all other models in key metrics like MAE, R², MSE, and error thresholds, making it the most reliable and accurate model in your comparison.



















