import typing
import unittest.mock

import pytest

import application.api
import application.model


class TestAPI:
    @pytest.mark.parametrize('item_raw, result_tree', [
        pytest.param(('GET', '/'), {'': 'GET'}, id='/'),
        pytest.param(('GET', '/foo/bar'), {'foo': {'bar': 'GET'}}, id='/foo/bar'),
        pytest.param(('GET', '/api/v1/foo/bar'), {'foo': {'bar': 'GET'}}, id='/api/v1/foo/bar'),
        pytest.param(('GET', '/foo/bar/{baz}'), {'foo': {'bar': 'GET'}}, id='/foo/bar/{baz}'),
        pytest.param(('GET', '/foo/{bar}/baz'), {'foo': {'baz': 'GET'}}, id='/foo/{bar}/baz'),
        pytest.param(('GET', '/foo/{bar}/baz/{42}'), {'foo': {'baz': 'GET'}}, id='/foo/{bar}/baz/{42}'),
    ])
    def test_add_item(self, item_raw: typing.Tuple[str, str], result_tree: dict) -> None:
        # arrange
        item = unittest.mock.Mock(spec=application.model.Item)
        item.verb, item.path = item_raw
        tree = {}
        storage = unittest.mock.Mock(spec=application.model.Storage)
        storage.tree = tree

        # act
        api = application.api.API(storage=storage)
        api.add_item(item)
        tree_ = api.get_tree()

        # assert
        assert tree_ is tree
        assert tree_ == result_tree

    def test_add_item_exception(self) -> None:
        # arrange
        item = unittest.mock.Mock(spec=application.model.Item)
        item.verb, item.path = ('GET', '/foo/bar')

        tree = {}
        storage = unittest.mock.Mock(spec=application.model.Storage)
        storage.tree = tree

        # act
        api = application.api.API(storage=storage)
        api.add_item(item)

        # assert
        with pytest.raises(application.api.VerbExists):
            api.add_item(item)
