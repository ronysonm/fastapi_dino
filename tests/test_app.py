def test_root_deve_retornar_200_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message' : 'Olá mundo!'}

def test_hello_route_deve_retornar_200_e_HTML(client):
    response = client.get('/hello')

    assert response.status_code == 200
    assert response.text == '<h1>Olá mundo</h1>'

def test_create_user(client):
    response = client.post(
        '/users',
        json = {
            'username' : 'john',
            'email' : 'example@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        'username' : 'john',
        'email' : 'example@example.com',
        'id' : 1,
    }

def test_list_users(client):
    response = client.get('/users/')

    assert response.status_code == 200
    assert response.json() == {
        'users' : [
            {
                'username' : 'john',
                'email' : 'example@example.com',
                'id' : 1,
            }
        ]
    }

def test_update_user(client):
    response = client.put('/users/1',
    json = {
        'username' : 'Bob',
        'email' : 'bob@example.com',
        'password' : 'SecretKey'
    })

    assert response.status_code == 200
    assert response.json() == {
        'username' : 'Bob',
        'email' : 'bob@example.com',
        'id' : 1
    }

def test_update_user_not_fount(client):
    response = client.put('/users/2',
        json = {
            'username' : 'John',
            'email' : 'jhon@example.com',
            'password' : 'secret'
        })

    assert response.status_code == 404
    assert response.json() == {'detail' : 'User not found'}

def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'message' : 'User deleted'}
