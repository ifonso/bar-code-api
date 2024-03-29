from typing import Dict, Any, Union, Never


class HttpRequest:
    def __init__(
        self,
        header: Union[Dict[str, Any], None] = None,
        body: Union[Dict[str, Any], None] = None,
        query_params: Union[Dict[str, Any], None] = None
    ) -> Never:
        self.header = header
        self.body = body
        self.query_params = query_params
