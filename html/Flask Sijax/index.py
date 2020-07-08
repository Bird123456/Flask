import os
from flask import Flask, g,render_template
import flask_sijax

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')#保存静态文件
app = Flask(__name__)

'''
配置文件
 '''
app.config['SIJAX_STATIC_PATH'] = path  #保存静态文件
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'#从中加载json2.js静态文件的URI
flask_sijax.Sijax(app)

@app.route('/')
def index():
   return 'Index'

@flask_sijax.route(app, '/hello')
def hello():
    def say_hi(obj_response):
        obj_response.alert('Hi there!')
     #在服务器上检测到此请求，在这种情况下，让Sijax处理该请求。
    if g.sijax.is_sijax_request:
        # Sijax request detected - let Sijax handle it
        g.sijax.register_callback('say_hi', say_hi)#注册的所有函数（请参见flask_sijax.Sijax.register_callback（））都可以从浏览器调用
        return g.sijax.process_request()#告诉Sijax执行适当的（先前注册的）函数，并将响应返回给浏览器。
    return render_template('sijaxexample.html')

if __name__ == '__main__':
   app.run(debug = True)