import os

from flask import Flask, request
from flask_restful import Resource, Api, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["testcase"] = []
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tmp_hello:ceshiren.com@182.92.129.158/tmp123?charset=utf8mb4'
db = SQLAlchemy(app)


class TestCaseTable(db.Model):
    name = db.Column(db.String(80), primary_key=True)
    description = db.Column(db.String(80), unique=False, nullable=True)
    filename = db.Column(db.String(80), unique=False, nullable=True)
    content = db.Column(db.String(300), unique=False, nullable=False)

    def __repr__(self):
        return '<TestCaseTable %r>' % self.name


class TestCaseStore(Resource):
    def get(self):
        """
        读取测试用例
        :return:
        """

    def post(self):
        """
        存储测试用例
        :return:
        """
        if "file" in request.files and "name" in request.form:
            f = request.files['file']
            name = request.form['name']
            file_name = f.filename
            content = f.read()
            testcase = TestCaseTable(name=name, filename=file_name, content=content)
            # f.save(os.path.join("./", file_name))
            db.session.add(testcase)
            db.session.commit()
            return "OK"
        # 返回不同的状态码和默认错误页面
        abort(404)


api.add_resource(TestCaseStore, '/testcase_store')

if __name__ == '__main__':
    app.run(debug=True)
    # db.create_all()
