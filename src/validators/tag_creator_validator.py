from typing import Any
from cerberus import Validator

from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError


def tag_creator_validator(request: Any) -> None:
    """
    Validates the incoming request for the tag creator.

    This function checks if the request contains all the necessary fields 
    and if their values are of the expected types. If the request is valid, 
    it returns None. If the request is invalid, it raises an appropriate 
    error.

    Parameters:
    request (dict): The incoming request to validate (JSON).

    Raises:
    `HttpUnprocessableEntityError`: If the request is missing necessary fields or the fields 
    have invalid values.
    """

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
