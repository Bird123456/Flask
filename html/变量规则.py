from flask import Flask
app = Flask(__name__)

#将单个值传进去
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run(debug = True)