from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/output', methods=['POST'])  
def output():

    type_val = request.form['type'] # categorical variable and add a dropdown
    amount_val = request.form['amount'] # numerical
    old_val = request.form['old'] # numerical
    new_val = request.form['new'] # numerical

    with open('model.pkl', 'rb') as model_file:
        loaded_model = pickle.load(model_file)
        
    if type_val=='PAYMENT':
        type_val=1
    elif type_val=='TRANSFER':
        type_val=4
    elif type_val=='CASH_OUT':
        type_val=2
    elif type_val=='DEBIT':
        type_val=5
    elif type_val=='CASH_IN':
        type_val=3
        
        
    temp=[[type_val,amount_val,old_val,new_val]]
    
    result = loaded_model.predict(temp)
    if result==0:
        result='No Fraud'
    else:
        result="Fraud"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
