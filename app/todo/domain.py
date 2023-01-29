from dataclasses import dataclass
from typing import Union
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Todo:
    """
    Todo object data structure
    """
    Id: str
    title: str
    description: str
    created_at: str
    finished_at: Union[str, None] = None
    updated_at: Union[str, None] = None
    deleted_at: Union[str, None] = None
