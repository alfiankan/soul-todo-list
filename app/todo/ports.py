from abc import ABC
from typing import Union
from app.todo.domain import Todo


class ITodoRepository(ABC):
    """
    ports handle data layer
    """
    def save(self, todo: Todo) -> bool:
        pass

    def get_all(self) -> dict[str, Todo]:
        pass

    def get_by_id(self, todo_id: int) -> Todo:
        pass

    def update_by_id(self, todo: Todo) -> bool:
        pass

    def update_finish_by_id(self, todo: Todo) -> bool:
        pass

    def soft_delete_by_id(self, todo: Todo) -> bool:
        pass


class ITodoUseCases(ABC):
    """
    ports handle businees logic
    """
    def create_todo(self, title: str, description: str) -> bool:
        pass

    def get_all_todo(self) -> list[Todo]:
        pass

    def get_by_id(self, todo_id: str) -> Union[Todo, None]:
        pass

    def update_by_id(self, title: str, description: str, todo_id: str) -> bool:
        pass

    def set_finish_by_id(self, todo_id: str) -> bool:
        pass

    def delete_by_id(self, todo_id: str) -> bool:
        pass
