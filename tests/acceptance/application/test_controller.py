import unittest.mock

import fastapi.testclient

import application.model
import application.fastapi.wsgi


def test() -> None:
    # act
    app = application.fastapi.wsgi.create_application()

    with (
        unittest.mock.patch('application.model.Storage') as storage,
        fastapi.testclient.TestClient(app) as client
    ):
        # assert isinstance(storage, application.model.Storage)  # todo
        storage.tree = {}
        response = client.post(
            '/items.json',
            json=[
                {'verb': "GET", 'path': "/api/v1/cluster/metrics"},
                {'verb': "POST", 'path': "/api/v1/cluster/{cluster}/plugins"},
                # {'verb': "POST", 'path': "/api/v1/cluster/{cluster}/plugins/{plugin}"},  # todo
            ],
        )

    # assert
    assert response.status_code == 200
    assert response.json() == {
        'cluster': {
            'metrics': 'GET',
            'plugins': 'POST',
        },
    }
