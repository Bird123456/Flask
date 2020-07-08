from flask import Flask,render_template

#生成Flask实例
app = Flask(__name__)
@app.route('/')
def my_echart():
#在浏览器上渲染my_templaces.html模板
    return render_template('bar.html')

if __name__ == "__main__":
    #运行项目
    app.run(debug = True)
