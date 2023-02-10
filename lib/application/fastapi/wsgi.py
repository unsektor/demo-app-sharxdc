import fastapi

import application.api
import application.controller
import application.fastapi.controller
import application.model

__all__ = (
    'create_application',
)


def create_application() -> fastapi.FastAPI:
    fastapi_application = fastapi.FastAPI(
        routes=[
            fastapi.routing.APIRoute(
                '/items.json',
                application.fastapi.controller.post_item_list,
                methods={'POST'}
            )

        ]
    )
    fastapi_application.api = application.api.API(
        storage=application.model.Storage(tree={})
    )
    return fastapi_application
