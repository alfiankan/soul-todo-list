from flask import Flask
from app.todo.repositories.in_memmory import TodoRepositoryInMemory
from app.todo.usecases.todo import TodoUseCase
from app.todo.delivery.todo_http_handler import TodoHttpHandler


def init_todo(app: Flask) -> None:
    """init and inject DI todo"""
    repo = TodoRepositoryInMemory()
    usecase = TodoUseCase(repo)
    TodoHttpHandler(usecase, app).handle()


if __name__ == '__main__':
    app = Flask(__name__)

    init_todo(app)

    app.run(host='0.0.0.0', port=5000, threaded=True)
