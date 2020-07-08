'''
Flask HTTP方法
Http协议是万维网中数据通信的基础。在该协议中定义了从指定URL检索数据的不同方法。

GET:以未加密的形式将数据发送到服务器。最常见的方法。

HEAD:和GET方法相同，但没有响应体。

POST:用于将HTML表单数据发送到服务器。POST方法接收的数据不由服务器缓存。

PUT:用上传的内容替换目标资源的所有当前表示。

DELETE:删除由URL给出的目标资源的所有当前表示。
'''


from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('success',name = user))
   else:
       #args是包含表单参数对及其对应值对的列表的字典对象
      user = request.args.get('name')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)