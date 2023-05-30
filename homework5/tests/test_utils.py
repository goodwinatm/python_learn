from homework5.utils import get_project_dir


def test_get_project_dir():
    print(get_project_dir('data\cookies.json'))
    assert 'cookies.json' in get_project_dir('data\cookies.json')