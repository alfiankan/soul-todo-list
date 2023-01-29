from abc import ABC
from app.todo.domain import Todo


class ITodoRepository(ABC):
    def save(self, todo: Todo) -> bool:
        pass

    def get_all(self) -> dict[int, Todo]:
        pass

    def get_by_id(self, todo_id: int) -> Todo:
        pass


class ITodoUseCases(ABC):
    def create_todo(self, title: str, description: str) -> bool:
        pass

    def get_all_todo(self) -> dict[int, Todo]:
        pass

