import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

def gender_transformer(df):
    if df['gender'][0]=='Male':
        df['gender_Male']=1
        df['gender_Other']=0
    elif df['gender'][0]=='Other':
        df['gender_Other']=1
        df['gender_Male']=0
    else:
        df['gender_Other']=0
        df['gender_Male']=0

def worktype_transformer(df):
    cols=['work_type_Never_worked','work_type_Private','work_type_children',
          'work_type_Self-employed']
    if df['work_type'][0]=='Never_worked':
        df[cols]=[1,0,0,0]
    elif df['work_type'][0]=='Private':
        df[cols]=[0,1,0,0]
    elif df['work_type'][0]=='Self-employed':
        df[cols]=[0,0,0,1]
    elif df['work_type'][0]=='children':
        df[cols]=[0,0,1,0]
    else:
        df[cols]=[0,0,0,0]

def smoking_transformer(df):
    cols=['smoking_status_formerly smoked', 'smoking_status_never smoked',
       'smoking_status_smokes']
    if df['smoking_status'][0]=='formerly smoked':
        df[cols]=[1,0,0]
    elif df['smoking_status'][0]=='never smoked':
        df[cols]=[0,1,0]
    elif df['smoking_status'][0]=='smokes':
        df[cols]=[0,0,1]
    else:
        df[cols]=[0,0,0]
        
def output(res):
    	if res==0:
    		return 'Congratulations!! You are not likely to have a stroke in future.'
    	else:
    		return 'Hey! Don\'t panic! You are likely to get a stroke in future. You need to take care of your health.'

def preprocessor(df):
    gender_transformer(df)
    worktype_transformer(df)
    smoking_transformer(df)
    df.drop(["gender","work_type","smoking_status"],axis=1,inplace=True)
    columns = ['avg_glucose_level','bmi','age']
    df[columns]=df[columns].astype(int)
    df[columns] = scaler.transform(df[columns])
    desired_col=['age', 'hypertension', 'heart_disease', 'ever_married',
       'Residence_type', 'avg_glucose_level', 'bmi', 'gender_Male',
       'gender_Other', 'work_type_Never_worked', 'work_type_Private',
       'work_type_Self-employed', 'work_type_children',
       'smoking_status_formerly smoked', 'smoking_status_never smoked',
       'smoking_status_smokes']
    return df[desired_col]

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	cols=['gender', 'age', 'hypertension', 'heart_disease', 'ever_married','work_type', 'Residence_type', 'avg_glucose_level', 'bmi','smoking_status']
	data=pd.DataFrame(columns=cols)
	data.loc[0] = [x for x in request.form.values()]
	input_features = preprocessor(data)
	prediction = model.predict(input_features.astype(float))
	return render_template('index.html', result=output(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)