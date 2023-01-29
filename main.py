from flask import Flask
from app.todo.repositories.in_memmory import TodoRepositoryInMemory
from app.todo.usecases.todo import TodoUseCase
from app.todo.delivery.todo_http_handler import TodoHttpHandler

app = Flask(__name__)
# set slash not strict
app.url_map.strict_slashes = False

repo = TodoRepositoryInMemory()
usecase = TodoUseCase(repo)
TodoHttpHandler(usecase, app).handle()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
