import typing

import fastapi

import application.api
import application.model

__all__ = (
    'post_item_list',
)


def post_item_list(
    request: fastapi.Request,
    item_list: typing.List[application.model.Item],
) -> fastapi.responses.JSONResponse:
    api: application.api.API = request.app.api
    return application.controller.post_item_list(api=api, item_list=item_list)
