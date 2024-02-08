from src.views.http_types.http_response import HttpResponse


def log_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'Error: {e}')
            return None
    return wrapper


def handle_errors(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Internal Server Error",
                "detail": str(error)
            }]
        }
    )
