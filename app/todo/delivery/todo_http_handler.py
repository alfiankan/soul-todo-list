from app.todo.ports import ITodoUseCases
from flask import Flask, request, Response
from common.base_response import BaseJsonResponse


class TodoHttpHandler:
    def __init__(self, todo_usecase: ITodoUseCases, http_server: Flask):
        self.todo_usecase = todo_usecase
        self.http_server = http_server

    def handle_create_todo(self) -> Response:
        return Response(
            BaseJsonResponse(message='Success Created', data={}).to_json(),
            status=201,
            content_type='application/json',
        )

    def handle(self):
        @self.http_server.route('/todo', methods=['POST'])
        def create_todo():
            return self.handle_create_todo()
