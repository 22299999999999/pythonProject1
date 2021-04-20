from flask import Flask, escape, request, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tmp_hello:ceshiren.com@182.92.129.158/tmp123?charset=utf8mb4'
db = SQLAlchemy(app)


@app.route('/users')
def hello():
    """
    返回类型处理:
    Response 对象：直接返回。
    string ：自动创建 Response 对象， 返回该对象，其状态码是 200 OK，类型是text/html。
    dict：使用 jsonify 改造并返回。
    tuple：(response, status), (response, headers) 或 (response, status, headers)。status 覆盖状态码，headers 是列表或字典，用于填充 headers 内容。
    符合 WSGI 接口的函数，自动转换成 response 对象
    :return:
    """
    name = request.args.get("name", "World3344")
    return f'Hello, {escape(name)}!'
    # return ("tmp123", 404)
    # return "OK"
    # return jsonify([1, 2, 3])
    # return [1, 2, 3]


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The projects page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/abc/123/<int:tmp>', methods=['get', 'post'])
def way(tmp):
    print(tmp)
    return 'The about page33'


if __name__ == "__main__":
    app.run(debug=True)
