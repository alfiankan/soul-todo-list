from app.todo.repositories.in_memmory import TodoRepositoryInMemory
from app.todo.usecases.todo import TodoUseCase
from app.todo.ports import ITodoUseCases
from faker import Faker


def seed_usecase(usecase: ITodoUseCases):
    for i in range(0, 10):
        fake = Faker()
        ok = usecase.create_todo(fake.sentences()[0], fake.sentences()[0])
        assert ok


def test_usecase_create_todo():
    repo = TodoRepositoryInMemory()
    usecase = TodoUseCase(repo)
    seed_usecase(usecase)


def test_usecase_get_todo():
    repo = TodoRepositoryInMemory()
    usecase = TodoUseCase(repo)
    seed_usecase(usecase)

    # check todos must be more than 0
    todos = usecase.get_all_todo()
    assert len(todos) > 0

    # check by id valid
    saved_id = todos[0].Id
    print(todos[0])
    single_todo = usecase.get_by_id(saved_id)
    assert single_todo.Id == saved_id


def test_usecase_update_todo():
    repo = TodoRepositoryInMemory()
    usecase = TodoUseCase(repo)
    seed_usecase(usecase)
    saved_id = usecase.get_all_todo()[0].Id

    # update
    assert usecase.update_by_id('edited', 'edited', saved_id)
