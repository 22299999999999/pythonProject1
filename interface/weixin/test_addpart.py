import requests


def test_add_part():
    data = {
        "name": "广州研发中心",
        "name_en": "RDGZ",
        "parentid": 1,
        "order": 1,
        "id": 255
    }
    url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=fe90DWf3529Xby7O6cfXEj9T-zJZCwDc8Ttf45rAxxJ02D-uoot5ctlu-nqz3ZYyTErvzVFE-6MDhkbJeJ8WMWl5JZGA0-zN5mN5g5zVkz8LgPmfvRTGvyeYwVvaWeY6gT8Lr3vnPyzboXOh5qRJD0iU7BnLcwO5OxgfCHuo8p5NVAwIFcAUzyQffGJcw2M89nlKTkTGg4Cjf6U3_m3pog'
    r = requests.post(url=url, json=data)
    print(r.status_code)
    print(r.json())
    assert 0 == r.json()['errcode']
