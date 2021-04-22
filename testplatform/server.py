import os

from flask import Flask, request
from flask_restful import Resource, Api, abort
from flask_sqlalchemy import SQLAlchemy
from jenkinsapi.jenkins import Jenkins

app = Flask(__name__)
api = Api(app)
app.config["testcase"] = []
# mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/mydata?charset=utf8mb4'
db = SQLAlchemy(app)


class TestCaseTable(db.Model):
    name = db.Column(db.String(80), primary_key=True)
    description = db.Column(db.String(80), unique=False, nullable=True)
    filename = db.Column(db.String(80), unique=False, nullable=True)
    content = db.Column(db.String(300), unique=False, nullable=False)
    report = db.relationship('Report', backref='test_case_table', lazy=True)

    def __repr__(self):
        return '<TestCaseTable %r>' % self.name


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), unique=False, nullable=True)
    dir = db.Column(db.String(300), unique=False, nullable=False)
    testcase_id = db.Column(db.String(80), db.ForeignKey('test_case_table.name'),
                            nullable=False)

    def __repr__(self):
        return '<Report %r>' % self.name


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


@app.route("/get_testcase", methods=['get'])
def get():
    """
    通过name，读取测试用例
    :param self:
    :return:
    """
    if "name" in request.args:
        print(request.args)
        name = request.args['name']
        testcase = TestCaseTable.query.filter_by(name=name).first()
        return testcase.content
    abort(404)


@app.route("/run", methods=['get'])
def run():
    """
    通过name，读取测试用例
    :param self:
    :return:
    """
    if "name" in request.args:
        name = request.args['name']
        testcase = TestCaseTable.query.filter_by(name=name).first()
        J = Jenkins('http://localhost:8083', username='admin', password='11f04b57967d785e4232d9a5a7b37c8da8')
        print(J.keys())
        J['test_platform'].invoke(build_params={"name": name, "file_name": testcase.filename})
        return "OK"
    abort(404)


@app.route("/report", methods=['post'])
def report():
    """
    测试报告
    :return:
    """
    if "file" in request.files and "name" in request.form:
        f = request.files['file']
        name = request.form['name']
        file_name = f.filename
        DIR = r"C:\Users\hp\Desktop\tmp"
        dir = os.path.join(DIR, file_name)
        f.save(dir)
        report = Report(dir=dir, testcase_id=name)
        db.session.add(report)
        db.session.commit()
        return "OK"
    # 返回不同的状态码和默认错误页面
    abort(404)


api.add_resource(TestCaseStore, '/store')

if __name__ == '__main__':
    app.run(debug=True)

    # db.drop_all()
    # db.create_all()
