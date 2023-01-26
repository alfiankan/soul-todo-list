from dataclasses import dataclass
from typing import Union
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Todo:
    """
    Todo object data structure
    """
    Id: int
    title: str
    description: str
    finished_at: Union[str, None]
    created_at: str
    updated_at: Union[str, None]
    deleted_at: Union[str, None]
