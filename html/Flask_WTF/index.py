from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField
from wtforms import validators, ValidationError

'''
除了'name'字段，还会自动创建CSRF令牌的隐藏字段。这是为了防止Cross Site Request Forgery（跨站请求伪造）攻击。
'''
'''
DataRequired
检查输入字段是否为空
'''
class ContactForm(Form):
   name = TextField("Name Of Student",[validators.Required("Please enter your name.")])#判断字符段是否为空
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")

   email = TextField("Email",[validators.Required("Please enter your email address."),#判断字符段是否为空
                              validators.Email("Please enter your email address.")])#检查字段中的文本是否遵循电子邮件ID约定

   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C++'),('py', 'Python')])
   submit = SubmitField("Send")

from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         return render_template('contact.html', form = form)
      else:
         return render_template('success.html')
   elif request.method == 'GET':
      return render_template('contact.html', form = form)

if __name__ == '__main__':
   app.run(debug = True)