
'''
Jinja2模板引擎使用以下分隔符从HTML转义。
{% ... %}用于语句 程序判断语句
{{ ... }}用于表达式可以打印到模板输出  可以传值
{# ... #}用于未包含在模板输出中的注释
# ... ##用于行语句
'''
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('hello2.html', marks = score)


if __name__ == '__main__':

   app.run(debug = True)