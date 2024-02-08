from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreatorView:
    """
        Responsability for interacting with HTTP
    """

    def valiedate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        if body is None:
            return HttpResponse(status_code=400, body={"error": "no product data found"})

        product_code = body["product_code"]

        print(product_code)

        # business logic

        # HTTP return
        return HttpResponse(status_code=200, body={"Hello": "Wolrd"})
