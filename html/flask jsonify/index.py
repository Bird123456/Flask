from flask import Flask, jsonify

# 实例化app
app = Flask(import_name=__name__)

@app.route('/login', methods=["GET","POST"])
def login():

    data =[
        {'name': 'xm', 'age': 30},
        {'name': 'xx', 'age': 18}
            ]
    json1=jsonify(data)
    return json1

if __name__ == '__main__':
    app.run(debug=True)