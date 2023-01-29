from app.todo.repositories.in_memmory import TodoRepositoryInMemory
from app.todo.ports import ITodoRepository
from faker import Faker
from app.todo.domain import Todo
from datetime import datetime
import uuid


def seed_todo(repo: ITodoRepository) -> str:
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
        assert repo.save(todo)
    return saved_id


def test_create_todo_repository():
    repo = TodoRepositoryInMemory()
    seed_todo(repo)


def test_getall_todo_repository():
    repo = TodoRepositoryInMemory()
    seed_todo(repo)

    # get todos must be more than 0
    assert len(repo.get_all()) > 0


def test_getbyid_todo_repository():
    repo = TodoRepositoryInMemory()
    saved_id = seed_todo(repo)
    # test get by id
    todo = repo.get_by_id(saved_id)

    assert todo.Id == saved_id


def test_updatebyid_todo_repository():
    repo = TodoRepositoryInMemory()
    saved_id = seed_todo(repo)
    # test get by id
    ok = repo.update_by_id(Todo(
        Id=saved_id,
        title='edited',
        description='edited',
    ))

    assert ok


def test_finish_todo_repository():
    repo = TodoRepositoryInMemory()
    saved_id = seed_todo(repo)
    # test get by id
    ok = repo.update_finish_by_id(Todo(
        Id=saved_id,
        finished_at=datetime.strftime(datetime.now(), '%d-%m-%Y %H:%M:%S'),
    ))

    assert ok


def test_delete_todo_repository():
    repo = TodoRepositoryInMemory()
    saved_id = seed_todo(repo)
    # test get by id
    ok = repo.soft_delete_by_id(saved_id)

    assert ok
