from flask import Flask,render_template,request,redirect,flash,url_for
app=Flask(__name__)
app.secret_key = 'any random string'

'''
flash()方法。它将消息传递给下一个请求，该请求通常是一个模板。
'''
#首页
@app.route('/')
def index():
    return render_template('index.html')

#获取login的post，传过来的参数
@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    '''
    如果账号密码不为admin，就返回error，error可以传递给login.html
    都是admin则返回调用flash（），然后可以将这些数据，传递到index函数中，在index.html中，哪些方法就是获取flash的数据
    '''
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error = error)

if __name__ == '__main__':
    app.run(debug=True)