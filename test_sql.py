from flask import Flask
from flask import request
from flask_restful import Resource, Api, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tmp_hello:ceshiren.com@182.92.129.158/tmp123?charset=utf8mb4'
db = SQLAlchemy(app)


class TestCaseTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=True)
    description = db.Column(db.String(80), unique=False, nullable=True)
    steps = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.description


class HelloWorld(Resource):
    def get(self, tmp):
        print(tmp)
        # db.create_all()

        if "name" in request.args:
            # 通过 name ，指定要运行的用例
            name = request.args['name']
            testcase = TestCaseTable.query.filter_by(name=name).first()
            return testcase.content
        abort(404)

    def post(self, tmp):
        if "file" in request.files and "name" in request.form:
            f = request.files["file"]
            name = request.form['name']
            file_name = f.filename
            content = f.read()
            testcase = TestCaseTable(name=name, file_name=file_name, content=content)
            db.session.add(testcase)
            db.session.commit()
            return "OK"
        # 返回不同的状态码，和默认的错误页
        abort(404)

    def get_tables(self):
        pass


api.add_resource(HelloWorld, '/testcase')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
