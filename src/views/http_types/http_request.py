from typing import Dict, Union


class HttpRequest:
    def __init__(
        self,
        header: Union[Dict, None] = None,
        body: Union[Dict, None] = None,
        query_params: Union[Dict, None] = None
    ) -> None:
        self.header = header
        self.body = body
        self.query_params = query_params
