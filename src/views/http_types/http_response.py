from typing import Dict, Any, Never


class HttpResponse:
    def __init__(self, status_code: int, body: Dict[str, Any]) -> Never:
        self.status_code = status_code
        self.body = body
