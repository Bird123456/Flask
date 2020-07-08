from flask import Flask, render_template
app = Flask(__name__)


'''
跳转到index.html中，
然后html调用static/hello.js文件
'''
@app.route("/index")
def index():
   return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)