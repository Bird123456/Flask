#url的重定向

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

'''
如果输入参数 等于 admin 就跳转到http://localhost:5000/admin
否则就跳转到：http://localhost:5000/guest/
'''
@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))


if __name__ == '__main__':
   app.run(debug = True)