from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')

def result():
   dict = {'phy':50,'chi':60,'maths':70}
   #将这个字典的值传过去
   return render_template('result.html', result = dict)

if __name__ == '__main__':

   app.run(debug = True)