from main import app
import json
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# POST /todo
def test_create_todo_api(client):
    for _ in range(0, 10):
        response = client.post(
            '/todo',
            data=json.dumps(dict(title='cc', description='xx')),
            content_type='application/json'
        )
        assert response.status_code == 201


# GET /todo
def test_get_todos_api(client):
    response = client.get('/todo')
    assert len(json.loads(response.data)['data']) > 1
    assert response.status_code == 200


# GET /todo/<id>
def test_get_todo_by_id_api(client):
    response = client.get('/todo')
    todo_id = json.loads(response.data)['data'][0]['Id']
    print(todo_id)
    assert response.status_code == 200

    response = client.get('/todo/' + todo_id)
    todo_id_last = json.loads(response.data)['data']['Id']
    print("last", todo_id_last)
    assert todo_id_last == todo_id


# PUT /todo/<id>
def test_update_todo_by_id_api(client):
    response = client.get('/todo')
    todo_id = json.loads(response.data)['data'][0]['Id']
    print(todo_id)
    assert response.status_code == 200

    response = client.put(
        '/todo/' + todo_id,
        data=json.dumps(dict(title='edited', description='edited')),
        content_type='application/json'
    )
    assert response.status_code == 200


# PATCH /todo/<id>/finish
def test_finish_todo_by_id_api(client):
    response = client.get('/todo')
    todo_id = json.loads(response.data)['data'][0]['Id']
    print(todo_id)
    assert response.status_code == 200

    response = client.patch('/todo/' + todo_id + '/finish')
    assert response.status_code == 200


# DELETE /todo/<td>
def test_delete_todo_by_id_api(client):
    response = client.get('/todo')
    todo_id = json.loads(response.data)['data'][0]['Id']
    print(todo_id)
    assert response.status_code == 200

    response = client.delete('/todo/' + todo_id)
    assert response.status_code == 200
