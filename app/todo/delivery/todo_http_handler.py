from app.todo.ports import ITodoUseCases
from flask import Flask, request, Response
from common.base_response import BaseJsonResponse
from common.validator import validateIsTypeValid, validateIsNotEmpty, isValidationError, validationErrMessage


class TodoHttpHandler:
    """
    handler and router for Todo
    Attributes
    """
    def __init__(self, todo_usecase: ITodoUseCases, http_server: Flask):
        self.todo_usecase = todo_usecase
        self.http_server = http_server

    def handle_create_todo(self) -> Response:
        title = request.json['title']
        desc = request.json['description']
        valErr = [
            validateIsNotEmpty(title, 'title'),
            validateIsTypeValid(title, str, 'title'),
            validateIsNotEmpty(desc, 'description'),
            validateIsTypeValid(desc, str, 'description'),
        ]

        if isValidationError(valErr):
            return BaseJsonResponse.validation_error(valErr)

        try:
            assert self.todo_usecase.create_todo(title, desc)
            return Response(
                BaseJsonResponse(message='Success Created', data={}).to_json(),
                status=201,
                content_type='application/json',
            )
        except Exception as e:
            # log here
            print(e)
            return BaseJsonResponse.internal_server_error()

    def handle_get_all_todos(self) -> Response:

        try:
            todos = self.todo_usecase.get_all_todo()
            return Response(
                BaseJsonResponse(message='Success Retreiving Todos', data=todos).to_json(),
                status=200,
                content_type='application/json',
            )
        except Exception as e:
            # log here
            print(e)
            return BaseJsonResponse.internal_server_error()

    def handle_get_todo_by_id(self, todo_id: str) -> Response:

        valErr = [
            validateIsTypeValid(todo_id, str, 'todo id'),
        ]

        if isValidationError(valErr):
            return BaseJsonResponse.validation_error(valErr)

        try:
            todo = self.todo_usecase.get_by_id(todo_id)
            return Response(
                BaseJsonResponse(message='Success Retreiving Todos', data=todo).to_json(),
                status=200,
                content_type='application/json',
            )
        except Exception as e:
            # log here
            print(e)
            return BaseJsonResponse.internal_server_error()

    def handle_update_todo(self, todo_id: str) -> Response:
        title = request.json['title']
        desc = request.json['description']
        valErr = [
            validateIsNotEmpty(title, 'title'),
            validateIsTypeValid(title, str, 'title'),
            validateIsNotEmpty(desc, 'description'),
            validateIsTypeValid(desc, str, 'description'),
        ]

        if isValidationError(valErr):
            return BaseJsonResponse.validation_error(valErr)

        try:
            assert self.todo_usecase.update_by_id(title, desc, todo_id)
            return Response(
                BaseJsonResponse(message='Success Updated', data={}).to_json(),
                status=200,
                content_type='application/json',
            )
        except Exception as e:
            # log here
            print(e)
            return BaseJsonResponse.internal_server_error()

    def handle_finish_todo(self, todo_id: str) -> Response:

        try:
            assert self.todo_usecase.set_finish_by_id(todo_id)
            return Response(
                BaseJsonResponse(message='Success Todo Finished', data={}).to_json(),
                status=200,
                content_type='application/json',
            )
        except Exception as e:
            # log here
            print(e)
            return BaseJsonResponse.internal_server_error()

    def handle_delete_todo(self, todo_id: str) -> Response:

        try:
            assert self.todo_usecase.delete_by_id(todo_id)
            return Response(
                BaseJsonResponse(message='Success Todo Deleted', data={}).to_json(),
                status=200,
                content_type='application/json',
            )
        except Exception as e:
            # log here
            print(e)
            return BaseJsonResponse.internal_server_error()

    def handle(self):
        """
        todo api routers
        """
        @self.http_server.route('/todo', methods=['POST'])
        def create_todo():
            return self.handle_create_todo()

        @self.http_server.route('/todo', methods=['GET'])
        def get_todos():
            return self.handle_get_all_todos()

        @self.http_server.route('/todo/<todo_id>', methods=['GET'])
        def get_todo_by_id(todo_id: str):
            return self.handle_get_todo_by_id(todo_id)

        @self.http_server.route('/todo/<todo_id>', methods=['PUT'])
        def update_todo_by_id(todo_id: str):
            return self.handle_update_todo(todo_id)

        @self.http_server.route('/todo/<todo_id>/finish', methods=['PATCH'])
        def finish_todo_by_id(todo_id: str):
            return self.handle_finish_todo(todo_id)

        @self.http_server.route('/todo/<todo_id>', methods=['DELETE'])
        def delete_todo_by_id(todo_id: str):
            return self.handle_delete_todo(todo_id)
