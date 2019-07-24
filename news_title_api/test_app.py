from app import app
import pytest


@pytest.fixture
def client():
    return app.test_client()


def do_get(client, path):
    response = client.get(path)
    return response.status_code, str(response.data), response.get_json()


def test_home(client):
    status_code, body, data = do_get(client, '/')
    assert status_code == 200


def test_daum_rt(client):
    status_code, body, data = do_get(client, '/daum-rt')
    assert status_code == 200
    assert 'daum_realtime' in data


def test_naver_rt(client):
    status_code, body, data = do_get(client, '/naver-rt')
    assert status_code == 200
    assert 'naver_realtime' in data