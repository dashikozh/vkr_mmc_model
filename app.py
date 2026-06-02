from flask import Flask, request, render_template, redirect, url_for, session 
import math

from classes.model_mmc import ModelMMC
from classes.model_mm1 import ModelMM1
from classes.model_md1 import ModelMD1

app = Flask(__name__)
app.secret_key = '12345678'

@app.route('/', methods=['GET', 'POST'])

def index():

    result = session.pop('result', None) # достаем результат из сессии

    if request.method == 'POST':

        lam    = int(request.form.get('lam')) # λ
        mu     = int(request.form.get('mu'))  # mu
        c      = int(request.form.get('c') )  # c
        n      = int(request.form.get('n') )  # n
        model  = request.form.get('models')


        if model == 'mmc':
            mmc_obj = ModelMMC(lam, mu, c)
            result  = mmc_obj.mmc() 
        elif model == 'md1':
            mmc_obj = ModelMD1(lam, mu)
            result  = mmc_obj.md1() 
        elif model == 'mm1':
            mmc_obj = ModelMM1(lam, mu, n)
            result  = mmc_obj.mm1()  

        session['result'] = result 
        return redirect(url_for('index')) 
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

