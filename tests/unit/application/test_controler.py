import typing
import unittest.mock

import application.controller
import application.model


def test_post_item_list() -> None:
    # arrange
    storage = unittest.mock.Mock(spec=application.model.Storage)
    storage.tree = {'test': 42}

    api: typing.Union[application.api.API, unittest.mock.Mock] = unittest.mock.Mock(spec=application.api.API)
    api.storage = storage
    api.get_tree.return_value = storage.tree

    item_1 = unittest.mock.Mock(spec=application.model.Item)
    item_2 = unittest.mock.Mock(spec=application.model.Item)
    item_3 = unittest.mock.Mock(spec=application.model.Item)
    item_list = [item_1, item_2, item_3, ]

    # act
    tree_ = application.controller.post_item_list(api=api, item_list=item_list)

    # assert
    api.add_item.assert_any_call(item_1)
    api.add_item.assert_any_call(item_2)
    api.add_item.assert_any_call(item_3)

    assert tree_ is storage.tree
