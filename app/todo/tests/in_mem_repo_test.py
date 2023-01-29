from app.todo.repositories.in_memmory import TodoRepositoryInMemory
from faker import Faker
from app.todo.domain import Todo
from datetime import datetime
import uuid


def test_todo_repository():
    repo = TodoRepositoryInMemory()
    saved_id = ''
    for i in range(0, 10):
        fake = Faker()

        todo = Todo(
            Id=uuid.uuid4(),
            title=fake.sentences()[0],
            description=fake.sentences()[0],
            created_at=datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            updated_at=None,
            finished_at=None,
            deleted_at=None,
        )
        saved_id = todo.Id
        if not repo.save(todo):
            raise Exception("Error save todo")

    # get todos must be more than 0
    assert len(repo.get_all()) > 0
    # test get by id
    todo = repo.get_by_id(saved_id)

    assert todo.Id == saved_id
