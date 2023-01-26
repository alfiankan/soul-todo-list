from app.todo.repositories.in_memmory import TodoRepositoryInMemory
from faker import Faker
from app.todo.domain import Todo
from datetime import datetime


def test_add_data_with_lock():
    repo = TodoRepositoryInMemory()

    for i in range(0, 10):
        fake = Faker()

        todo = Todo(
            Id=i,
            title=fake.sentences()[0],
            description=fake.sentences()[0],
            created_at=datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            updated_at=None,
            finished_at=None,
            deleted_at=None,
        )
        if not repo.save(todo):
            raise Exception("Error save todo")

    assert len(repo.get_all()) > 0

