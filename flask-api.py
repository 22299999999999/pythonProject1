from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.config["testcase"] = []


class TestCase(Resource):
    def get(self):
        if "id" in request.args:
            # print("入参中id的类型为：")
            # print(type(request.args["id"]))
            for i in app.config["testcase"]:
                # print(type("testcase中的id的类型为："))
                # print(type(i["id"]))
                if i["id"] == request.args["id"]:
                    return i
        else:
            return app.config["testcase"]

    # 模拟post请求的命令：curl -i -H "Content-Type: application/json" -X POST -d "{"""id""":"""200"""}" 127.0.0.1:5000/testcase
    def post(self):
        if "id" not in request.json:
            print(request.json)
            return {"result": "error", "errmessage": "need testcase id"}
        app.config["testcase"].append(request.json)
        return {"result": "ok"}

    # def post(self):
    #     return "hhaha"


api.add_resource(TestCase, '/testcase')

if __name__ == '__main__':
    app.run(debug=True)
