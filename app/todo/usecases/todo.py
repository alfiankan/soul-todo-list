import uuid

from app.todo.ports import ITodoUseCases, ITodoRepository
from app.todo.domain import Todo
from datetime import datetime


class TodoUseCase(ITodoUseCases):
    """
    Todo use case business logic
    """

    def __init__(self, todo_repository: ITodoRepository) -> ITodoUseCases:
        self.todo_repository = todo_repository

    def create_todo(self, title: str, description: str) -> bool:
        new_todo = Todo(
            Id=uuid.uuid4().__str__(),
            title=title,
            description=description,
            created_at=datetime.strftime(datetime.now(), '%d-%m-%Y %H:%M:%S')
        )

        return self.todo_repository.save(new_todo)

    def get_all_todo(self) -> list[Todo]:
        return list(filter(lambda todo: todo.deleted_at is None , list(self.todo_repository.get_all().values())))

    def get_by_id(self, todo_id: int) -> Todo:
        return self.todo_repository.get_by_id(todo_id)

    def update_by_id(self, title: str, description: str, todo_id: str) -> bool:
        todo = Todo(
            Id=todo_id,
            title=title,
            description=description,
            updated_at=datetime.strftime(datetime.now(), '%d-%m-%Y %H:%M:%S'),
        )
        return self.todo_repository.update_by_id(todo)

    def set_finish_by_id(self, todo_id: str) -> bool:
        todo = Todo(
            Id=todo_id,
            finished_at=datetime.strftime(datetime.now(), '%d-%m-%Y %H:%M:%S'),
        )
        return self.todo_repository.update_finish_by_id(todo)

    def delete_by_id(self, todo_id: str) -> bool:
        return self.todo_repository.soft_delete_by_id(todo_id)
