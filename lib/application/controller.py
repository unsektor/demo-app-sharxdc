import typing

import application.model


def post_item_list(  # fixme CQRS violation
    api: application.api.API,
    item_list: typing.List[application.model.Item]
) -> typing.Dict[str, typing.Union[dict, str]]:
    for item in item_list:
        api.add_item(item)

    return api.get_tree()
