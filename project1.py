from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
       principle = float(request.form['principle'])
       Rate = float(request.form['Rate'])
       time = float(request.form['time'])
       Rate=Rate/1200
       time= time*12
       EMI = round((principle * Rate * (1 + Rate) ** time )/ ((1 + Rate) ** time - 1), 5)

       return render_template('calculator.html',principle=principle, Rate=Rate, time=time, EMI=EMI)

    return render_template('index.html')

if __name__ == "__main__":
      app.run(debug=True)