from flask import Blueprint, request, jsonify

from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

from src.errors.error_handler import handle_errors


tag_routes_bp = Blueprint("tags_routes", __name__)

@tag_routes_bp.route("/create-tag", methods=["POST"])
def create_tag():
    tag_creator_view = TagCreatorView()
    try:
        http_request = HttpRequest(body=request.json)
        response = tag_creator_view.valiedate_and_create(http_request)
        return jsonify(response.body), response.status_code

    except Exception as e:
        response = handle_errors(e)
        return jsonify(response.body), response.status_code
