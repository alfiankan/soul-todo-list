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
            Id=uuid.uuid4(),
            title=title,
            description=description,
            created_at=datetime.strftime(datetime.now(), '%d-%m-%Y %H:%M:%S')
        )

        return self.todo_repository.save(new_todo)

    def get_all_todo(self) -> list[Todo]:
        return self.todo_repository.get_all().values()
