from dataclasses import dataclass
from typing import Any
from dataclasses_json import dataclass_json
from common.validator import validationErrMessage
from flask import Response


@dataclass_json
@dataclass
class BaseJsonResponse:
    message: str
    data: Any

    def validation_error(errors: list[str]) -> Response:
        return Response(
            BaseJsonResponse(
                message='Success Created',
                data='Validation error, {}'.format(validationErrMessage(errors)),
            ).to_json(),
            status=422,
            content_type='application/json'
        )

    def internal_server_error() -> Response:
        return Response(
            BaseJsonResponse(
                message='Internal Server Error',
                data={},
            ).to_json(),
            status=500,
            content_type='application/json'
        )
