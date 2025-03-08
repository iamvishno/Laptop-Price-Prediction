from flask import Flask,render_template,request
import numpy as np

from src.pipeline.predict_pipeline import  CustomData,PredictPipeline
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
        Company=request.form.get("Company"),
        TypeName=request.form.get('TypeName'),
        Inches=np.float64(request.form.get('Inches' )),
        Ram=np.int64(request.form.get('Ram')) ,
        Cpu=request.form.get('Cpu') ,
        Gpu=request.form.get('Gpu') ,
        SSD=request.form.get('SSD') ,
        HDD=request.form.get('HDD') ,
        TouchScreen=np.int64(request.form.get('TouchScreen')),
        Ips_display=np.int64(request.form.get('Ips_display')),
        Os=request.form.get("Os"),
        Resolution=request.form.get('Resolution')
        )

    pred_df = data.get_data_as_df()


    predict_pipeline = PredictPipeline()
    results =  predict_pipeline.predict(pred_df)


    return render_template('home.html',results=results)

if __name__=="__main__":
    app.run(debug=True)

