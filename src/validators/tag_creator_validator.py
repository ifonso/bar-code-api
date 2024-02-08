from typing import Any
from cerberus import Validator

from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError


def tag_creator_validator(request: Any) -> None:
    schema = {
        "product_code": {
            "type": "string",
            "required": True,
            "empty": False,
            "minlength": 1,
            "maxlength": 48
        }
    }

    body_validator = Validator(schema)
    response = body_validator.validate(request)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
