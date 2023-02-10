import typing
import pydantic


class Item(pydantic.BaseModel):  # fixme remove adhoc using 3rd party dependencies in domain ! used for fast-api atm
    verb: str
    path: str


class Storage:
    def __init__(self, tree: typing.Dict[str, typing.Union[dict, str]] = None) -> None:
        self.tree = tree or {}
