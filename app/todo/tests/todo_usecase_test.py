from app.todo.repositories.in_memmory import TodoRepositoryInMemory
from app.todo.usecases.todo import TodoUseCase
from faker import Faker


def test_usecase_todo():
    repo = TodoRepositoryInMemory()
    usecase = TodoUseCase(repo)

    for i in range(0, 10):
        fake = Faker()
        ok = usecase.create_todo(fake.sentences()[0], fake.sentences()[0])
        assert ok

    # check todos must be more than 0
    todos = usecase.get_all_todo()
    assert len(todos) > 0

    # check by id valid
    saved_id = todos[0].Id
    print(todos[0])
    single_todo = usecase.get_by_id(saved_id)
    assert single_todo.Id == saved_id
