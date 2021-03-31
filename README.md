# ML-deployment-stroke-prediction
Using [Strokes Prediction dataset](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset) dataset from kaggle, I made a binary classification model.
I performed exploratory data analysis to get some insights from the data. After imputing missing values with mean, I over-sampled the data as it was highly imbalanced. Then I label encoded the categorical features having 2 classes. For categorical features with multiple categories, I used one-hot encoding. Then after scaling the numerical features I used XGBoost Classifier to build a model.
AUC-ROC score is 0.82.

I deployed it using Flask and Heroku.

App link: https://strokes-prediction-api.herokuapp.com/

[Click here to see EDA](https://github.com/ayushikaushik/ML-deployment-stroke-prediction/blob/main/EDA.ipynb)\n\n
[Click here to see model building](https://github.com/ayushikaushik/ML-deployment-stroke-prediction/blob/main/model.ipynb)
