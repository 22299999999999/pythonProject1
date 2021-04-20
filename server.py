from flask import Flask, request
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)
app.config["testcase"] = []


class TestCase(Resource):
    def get(self):
        # return ("tmp123", 404)
        # return "OK"
        return [1, 2, 3]

    # 把测试用例存储到本地/数据库
    def post(self):
        if "file" in request.files:
            f = request.files["file"]
            file_name = f.filename
            # # 存储到本地
            # f.save(os.path.join("./", file_name))

            return "OK"
        # 返回不同的状态码，和默认的错误码
        abort(404)


api.add_resource(TestCase, '/testcase')

if __name__ == '__main__':
    app.run(debug=True)
