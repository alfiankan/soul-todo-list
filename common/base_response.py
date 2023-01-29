from dataclasses import dataclass
from typing import Any
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class BaseJsonResponse:
    message: str
    data: Any
