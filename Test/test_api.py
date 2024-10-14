import requests
from data import *


def test_api_search_by_name():
    query_params = {
        'page': '1',
        'limit': '1',
        'query': 'House of the dragon'
    }
    my_headers = {"X-API-KEY": token}

    resp = requests.get(URL + '/v1.4/movie/search', json=query_params, headers=my_headers)
    assert resp.status_code == 200

def test_api_search_by_id():
    query_params = {
        'id': '1316601'
    }
    my_headers = {"X-API-KEY": token}

    resp = requests.get(URL + '/v1.4/movie', json=query_params, headers=my_headers)
    assert resp.status_code == 200

def test_api_search_by_actors_name():
    query_params = {
        'page': '1',
        'limit': '1',
        'query': "emma d'arcy"
    }
    my_headers = {"X-API-KEY": token}

    resp = requests.get(URL + '/v1.4/person/search', json=query_params, headers=my_headers)
    assert resp.status_code == 200

def test_api_search_by_wrong_query():
    query_params = {
        'page': '1',
        'limit': '',
        'query': 'House of the dragon'
    }
    my_headers = {"X-API-KEY": token}

    resp = requests.get(URL + '/v1.4/movie/search', json=query_params, headers=my_headers)
    assert resp.status_code == 400

def test_api_search_by_id_doesnt_exist():
    query_params = {
        'id': '1000100 1010110 1010010'
    }
    my_headers = {"X-API-KEY": token}

    resp = requests.get(URL + '/v1.4/movie', json=query_params, headers=my_headers)
    assert resp.status_code == 400
