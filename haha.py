import pytest

from hello import get_yaml


def test_get_yaml():
    data = get_yaml()
    print(data)
    print(type(data))
