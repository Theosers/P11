def test_index_route(client):
    response = client.get('/')
    response_data = response.data.decode()
    assert response.status_code == 200
    assert '<h1>Welcome to the GUDLFT Registration Portal!</h1>' in response_data


def test_index_connexion_failed(client):
    email = 'wrong@wrong.co'
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200
    assert 'Sorry, that email was not found' in response.data.decode()


def test_logout(client):
    response = client.get('/logout')
    assert response.status_code == 302


def test_purchase_places(client):
    response = client.post('/purchasePlaces',
                           data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'places': '1'})
    assert response.status_code == 200
    assert 'complete' in response.data.decode()


def test_rankings_route(client):
    response = client.get('/rankings')
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Club\'s name ' in response_data
    assert 'Simply Lift' in response_data


def test_purchase_too_much_places(client):
    response = client.post('/purchasePlaces', data={'email': 'john@simplylift.co', 'club': 'She Lifts',
                                                    'competition': 'Spring Festival', 'places': 13
                                                    }
                           )
    assert response.status_code == 200


def test_show_summary(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert 'Welcome' in response.data.decode()
    assert 'Points available' in response.data.decode()


def test_can_not_purchase_places_because_of_old_date(client):
    response = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Fall Classic', 'places': 1})
    assert response.status_code == 200
    assert 'Sorry, this competition has already taken place' in response.data.decode()


def test_purchase_places(client):
    response = client.post('/purchasePlaces', data={'club': 'Simply Lift',
                                                    'competition': 'Spring Festival', 'places': '1'
                                                    }
                           )
    assert response.status_code == 200
    assert 'complete' in response.data.decode()


def test_purchase_not_enought_points(client):
    response = client.post('/purchasePlaces', data={'club': 'Simply Lift',
                                                    'competition': 'Spring Festival',
                                                    'places': 6
                                                    }
                           )
    assert response.status_code == 200
