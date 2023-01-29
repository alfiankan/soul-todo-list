from app.todo.ports import ITodoUseCases
from flask import Flask


class TodoHttpHandler:
    def __init__(self, todo_usecase: ITodoUseCases, http_server: Flask):
        self.todo_usecase = todo_usecase
        self.http_server = http_server

    def handle(self):
        @self.http_server.route('/add')
        def create():
            return '200'
