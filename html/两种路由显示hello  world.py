# 导入Flask类
from flask import Flask
# 实例化，可视为固定格式
app = Flask(__name__)


#application对象的add_url_rule()函数
def hello_world():
    return 'Hello, World!'
app.add_url_rule('/hello/','hello', hello_world)

# route()方法用于设定路由；类似spring路由配置
'''
app.route(rule, options)
rule 参数表示与该函数的URL绑定。
options 是要转发给基础Rule对象的参数列表。
'''
@app.route('/hello')
def xm():
    return 'xm'

if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host="127.0.0.1", port=5000, debug=False
    app.run(host="0.0.0.0", port=5000)

'''
app.run(host, port, debug, options)
所有参数都是可选的

host:要监听的主机名。 默认为127.0.0.1（localhost）。设置为“0.0.0.0”以使服务器在外部可用

port:默认值为5000

debug:默认为false。 如果设置为true，则提供调试信息

options:要转发到底层的Werkzeug服务器。
'''