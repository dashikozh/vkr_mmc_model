from flask import Flask, request, render_template, redirect, url_for, session 
import math

app = Flask(__name__)
app.secret_key = '12345678'

@app.route('/', methods=['GET', 'POST'])

def index():

    result = session.pop('result', None) # достаем результат из сессии

    if request.method == 'POST':

        lam    = int(request.form.get('lam')) # λ
        mu     = int(request.form.get('mu'))  # mu
        c      = int(request.form.get('c') )  # c

        if mu > lam:
            # конструкция для обработки ошибок, если указать слишком большое значение кол-во серверов, 
            # то питон не справляется при вычислении фаториала и падает с ошибкой
            try:
                # Коэффициент использования серверов: U = λ / (c × µ)
                U  = lam / (c * mu)
                # Вероятность того, что система не занята
                U_pow_c = U ** c # возводим в степень
                fact_c  = math.factorial(c) # факториал
                P0 = U_pow_c / (fact_c * (1 - U)) # итоговое выражение
                # Среднее количество запросов в системе: L = (λ / (c ×(µ — λ)))
                L  = (lam / (c * (mu - lam)))
                # Среднее время, которое запрос проводит в системе: W = 1 / (c × (µ — λ))
                W  = 1 / (c * (mu - lam))
         
                result = {
                    'U':  U,
                    'P0': P0,
                    'L':  L,
                    'W':  W,
                    'state': 'true',
                    'log': '<span class="green">Данные успешно рассчитаны</span>'
                }
            except OverflowError:
                result = {
                    'log': '<span class="red">Ошибка: слишком большое значение "c (количество серверов)"</span>'
                }
        else:
            result = {
                'log': '<span class="red">Значение <b>µ</b> должно быть больше <b>λ</b></span>' 
            }
        
        session['result'] = result 
        return redirect(url_for('index')) 
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
