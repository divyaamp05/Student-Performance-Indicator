from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predictdata():
    try:
        if request.method == 'POST':  

            data = CustomData(

                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                math_score=float(request.form.get('math_score')),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )

            pred_df = data.get_data_as_data_frame()

            predict_pipeline = PredictPipeline()

            results = predict_pipeline.predict(pred_df)

            return render_template('home.html', results=results[0])  
        
        # Handle GET requests (initial page load)
        return render_template('home.html')  

    except Exception as e:
        return render_template('home.html', error=str(e)) 



if __name__ == '__main__':
    app.run(port=5003, debug=True)