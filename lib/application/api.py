import re
import typing

import application.model

__all__ = (
    'VerbExists',
    'API',
)


_NORMALIZE_PATH_REGEXP = re.compile(r'(?:/\{[^/]*|/api/v\d)')  # fixme too weak


class VerbExists(RuntimeError):
    pass


class API:
    def __init__(self, storage: application.model.Storage) -> None:
        self.storage = storage

    def add_item(self, item: application.model.Item) -> None:
        # todo consider to verify path not contains few slashes per time
        _, *key_list, key = _NORMALIZE_PATH_REGEXP.sub('', item.path).split('/')
        tree = self.storage.tree

        for i in key_list:
            tree = tree.setdefault(i, {})

        if key in tree:  # and tree[key] == item.path:
            raise VerbExists(item.path)

        tree[key] = item.verb

    def get_tree(self) -> typing.Dict[str, typing.Union[dict, str]]:
        return self.storage.tree
