def test_authentication(client):
    response = client.post('/auth', json={'email': 'test@example.com', 'mot_de_passe': '12345'})
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_authentication_invalid(client):
    response = client.post('/auth', json={'email': 'wrong@example.com', 'mot_de_passe': 'wrong'})
    assert response.status_code == 401
