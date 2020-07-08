from flask import Flask,session,request,redirect,url_for,render_template
app = Flask(__name__)
'''
Session（会话）数据存储在服务器上
为每个客户端的会话分配会话ID。会话数据存储在cookie的顶部，服务器以加密方式对其进行签名。
对于此加密，Flask应用程序需要一个定义的SECRET_KEY。
'''
app.secret_key = 'any random string'

#主页
@app.route('/')
def index():
    #如果设置了session，就返回logout函数
    #没有设置就返回login函数
    if 'username' in session:
        username = session['username']
        return 'Logged in as '+username+'<br> <b><a href ="/logout"> click here to log out</a></b> '
    return "You are not logged in <br><a href = '/login'></b>click here to log in</b></a>"

#没有设置session，login
@app.route('/login', methods = ['GET', 'POST'])
def login():
    #如果返回了post方法，就设置session，在返回index函数
   if request.method == 'POST':
      session['username'] = request.form['username']#获取表格的username将其存储在uesername  Session中
      return redirect(url_for('index'))#返回index函数
    #没有返回post方法，就返回index.html界面
   return render_template('index.html')

#session.pop释放session,释放之后就返回index函数
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)