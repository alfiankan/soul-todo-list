from dataclasses import dataclass
from typing import Union
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Todo:
    """
    Todo object data structure
    """
    Id: Union[str, None] = None
    title: Union[str, None] = None
    description: Union[str, None] = None
    created_at: Union[str, None] = None
    finished_at: Union[str, None] = None
    updated_at: Union[str, None] = None
    deleted_at: Union[str, None] = None
