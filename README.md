
# Soul Todo API

## Architectural Design

  - this application adopts a clean architecture and hexagonal design with some modification. the main layer is repository, usecase, and delivery
  - folders & files:
      - <b>delivery</b>: route and request response handler
      - <b>repositories</b>: implementation from port(interface) data store layer
      - <b>usecases</b>: implementation from port(interface) businees logic layer
      - <b>tests</b>: all tests for current domain
      - <b>domain.py</b>: domain/data structure for app
      - <b>ports.py</b>: all interfaces agnostic infras driven and driver

## Requirements
  - python 3.9^
  - Make
  - install python required package using :
    ```
    pip install -r requirements.txt
    ```

<a name="3"></a>
## How to run &nbsp;&nbsp;🔨
  1. Make sure all requirements already installed
  2. To install predefined python package use `pip install -r requirements.txt`
  3. Copy `env.example` to `.env` and set configuration or leave it be default
  4. Run app `make run` or `python3 main.py` 

## How to run on docker &nbsp;&nbsp;🔨
  1. Copy `env.example` to `.env` and set configuration or leave it be default
  2. Build docker image `docker build -t soul-todo .`
  3. Run docker container `docker run -d -p <port>:<port> soul-todo` 

<a name="4"></a>
## How to test &nbsp;&nbsp; 🧪
  - Verbose testing run `make test`
      > output :

        app/todo/tests/http_test.py::test_create_todo_api PASSED                                                                                                             [  5%]
        app/todo/tests/http_test.py::test_get_todos_api PASSED                                                                                                               [ 11%]
        app/todo/tests/http_test.py::test_get_todo_by_id_api PASSED                                                                                                          [ 17%]
        app/todo/tests/http_test.py::test_update_todo_by_id_api PASSED                                                                                                       [ 23%]
        app/todo/tests/http_test.py::test_finish_todo_by_id_api PASSED                                                                                                       [ 29%]
        app/todo/tests/http_test.py::test_delete_todo_by_id_api PASSED                                                                                                       [ 35%]
        app/todo/tests/in_mem_repo_test.py::test_create_todo_repository PASSED                                                                                               [ 41%]
        app/todo/tests/in_mem_repo_test.py::test_getall_todo_repository PASSED                                                                                               [ 47%]
        app/todo/tests/in_mem_repo_test.py::test_getbyid_todo_repository PASSED                                                                                              [ 52%]
        app/todo/tests/in_mem_repo_test.py::test_updatebyid_todo_repository PASSED                                                                                           [ 58%]
        app/todo/tests/in_mem_repo_test.py::test_finish_todo_repository PASSED                                                                                               [ 64%]
        app/todo/tests/in_mem_repo_test.py::test_delete_todo_repository PASSED                                                                                               [ 70%]
        app/todo/tests/todo_usecase_test.py::test_usecase_create_todo PASSED                                                                                                 [ 76%]
        app/todo/tests/todo_usecase_test.py::test_usecase_get_todo PASSED                                                                                                    [ 82%]
        app/todo/tests/todo_usecase_test.py::test_usecase_update_todo PASSED                                                                                                 [ 88%]
        app/todo/tests/todo_usecase_test.py::test_usecase_finish_todo PASSED                                                                                                 [ 94%]
        app/todo/tests/todo_usecase_test.py::test_delete_finish_todo PASSED                                                                                                  [100%]
        
        ============================================================================ 17 passed in 1.24s ============================================================================                                    [100%]


## Api Docs

- this app include open api swagger docs server, you can access from `http://localhost:<env_port>/docs`
- postman documenter version from swagger open api specs:
    <br><br>
    [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/24530299-5b8bb710-839c-40af-9dd3-8eb6521ac677?action=collection%2Ffork&collection-url=entityId%3D24530299-5b8bb710-839c-40af-9dd3-8eb6521ac677%26entityType%3Dcollection%26workspaceId%3D554dcc4f-cf17-4e8a-bdb2-bcda713286cf)
        






