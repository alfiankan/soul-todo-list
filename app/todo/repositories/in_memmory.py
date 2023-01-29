from threading import Lock
from app.todo.domain import Todo
from app.todo.ports import ITodoRepository


class TodoRepositoryInMemory(ITodoRepository):
    """
    data layer for todo using memory and mutex to avoid
    race condition
    """

    def __init__(self) -> ITodoRepository:
        self.mutex: Lock = Lock()
        self.todos: dict[str, Todo] = dict()

    def save(self, todo: Todo) -> bool:
        try:
            with self.mutex:
                self.todos[todo.Id] = todo
            return True
        except Exception as err:
            print("log :", err)
            return False

    def get_all(self) -> dict[str, Todo]:
        return self.todos

    def get_by_id(self, todo_id: str) -> Todo:
        return self.todos[todo_id]

    def update_by_id(self, todo: Todo) -> bool:
        try:
            self.todos[todo.Id].title = todo.title
            self.todos[todo.Id].description = todo.description
            self.todos[todo.Id].updated_at = todo.updated_at
            return True
        except Exception as e:
            print(e)
            return False

    def update_finish_by_id(self, todo: Todo) -> bool:
        try:
            self.todos[todo.Id].finished_at = todo.finished_at
            return True
        except Exception as e:
            print(e)
            return False
