from app.todo.ports import ITodoUseCases
from flask import Flask, request, Response
from common.base_response import BaseJsonResponse
from common.validator import validateIsTypeValid, validateIsNotEmpty, isValidationError, validationErrMessage


class TodoHttpHandler:
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
            self.todo_usecase.create_todo(title, desc)
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

    def handle(self):
        @self.http_server.route('/todo', methods=['POST'])
        def create_todo():
            return self.handle_create_todo()

        @self.http_server.route('/todo', methods=['GET'])
        def get_todos():
            return self.handle_get_all_todos()
