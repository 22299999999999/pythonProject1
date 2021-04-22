from jenkinsapi.jenkins import Jenkins


def test_jenkins():
    J = Jenkins('http://localhost:8083', username='admin', password='11f04b57967d785e4232d9a5a7b37c8da8')
    print(J.keys())
    J['test_platform'].invoke(build_params={"name": "tmp1234", "file_name": "hello420.py"})
