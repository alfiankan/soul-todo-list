from abc import ABC
from app.todo.domain import Todo


class TodoRepository(ABC):
    def save(self, todo: Todo) -> bool:
        pass

    def get_all(self) -> dict[int, Todo]:
        pass

    def get_by_id(self, todo_id: int) -> Todo:
        pass

