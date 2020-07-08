from flask import Flask,render_template,request
from werkzeug.utils import secure_filename      #secure_filename()函数获取filename属性的安全版本。
import os

app=Flask(__name__)

#选择首页
@app.route('/index')
def upload():
   return render_template('upload.html')

@app.route('/uploader',methods = ['POST', 'GET'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']

      basepath = os.path.dirname(__file__)  # __file__当前py文件所在路径, 然后os.path.dirname是返回当前文件的文件夹
      dir_name = 'img'
      # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
      if not os.path.isdir(dir_name):
         os.makedirs(dir_name)
      upload_path = os.path.join(basepath,dir_name,secure_filename(f.filename))#路径拼接

      upload_path = os.path.abspath(upload_path) # 将路径转换为绝对路径

      f.save(upload_path)
      return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(debug='True')