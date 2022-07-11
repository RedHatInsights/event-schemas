# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = empty_from_dict(json.loads(json_string))

from typing import Any


def from_none(x: Any) -> Any:
    assert x is None
    return x


def empty_from_dict(s: Any) -> None:
    return from_none(s)


def empty_to_dict(x: None) -> Any:
    return from_none(x)
