from app.todo.repositories.in_memmory import TodoRepositoryInMemory
from app.todo.usecases.todo import TodoUseCase
from faker import Faker
from app.todo.domain import Todo
from datetime import datetime


def test_create_todo():
    repo = TodoRepositoryInMemory()
    usecase = TodoUseCase(repo)

    for i in range(0, 10):
        fake = Faker()

        ok = usecase.create_todo(fake.sentences()[0], fake.sentences()[0])
        assert ok

