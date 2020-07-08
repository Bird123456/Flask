from flask_wtf import Form
from wtforms import TextField

'''
除了'name'字段，还会自动创建CSRF令牌的隐藏字段。这是为了防止Cross Site Request Forgery（跨站请求伪造）攻击。
'''
class ContactForm(Form):
   name = TextField("Name Of Student")