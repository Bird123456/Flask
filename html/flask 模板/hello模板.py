#这样就可以使用已经写好的html模板了

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/hello/<name>')
def index(name):
    #寻找templates文件夹下的指定html文件
   return render_template('hello.html',name1=name)


if __name__ == '__main__':
   app.run(debug = True)