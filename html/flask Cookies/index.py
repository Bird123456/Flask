#Cookie以文本文件的形式存储在客户端的计算机上。其目的是记住和跟踪与客户使用相关的数据，以获得更好的访问者体验和网站统计信息。
from flask import Flask, redirect, url_for, request,render_template,make_response
app = Flask(__name__)

#首页
@app.route('/')
def index():
   return render_template('index.html')

#首页的POST方法，会返回name参数
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        #指定这个html
        resp = make_response(render_template('readcookie.html'))
        #设置cookies
        resp.set_cookie('userID', user)

        return resp

#readcookie里有个超链接返回getcookie
@app.route('/getcookie')
def getcookie():
    #获取cookie
    name = request.cookies.get('userID')

    return '<h1>welcome '+name+'</h1>'

if __name__ == '__main__':
   app.run(debug = True)