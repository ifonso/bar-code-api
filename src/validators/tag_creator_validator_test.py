from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .tag_creator_validator import tag_creator_validator


class MockRequest:
    def __init__(self, json):
        self.json = json


def test_tag_creator_validator_with_valid_request():
    # Given a valid request
    req = MockRequest(json={ "product_code": "123456" })
    # When the request is validated
    tag_creator_validator(req.json)
    # Then no exception is raised


def test_tag_creator_validator_with_invalid_request():
    # Given a request with no product code
    req = MockRequest(json={})
    # When the request is validated
    try:
        tag_creator_validator(req.json)
        assert False, "An exception should have been raised given a request with no product code"
    # Then an exception is raised
    except Exception as e:
        assert isinstance(e, HttpUnprocessableEntityError)
