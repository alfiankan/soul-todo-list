import os

from flask import Flask, send_from_directory
from app.todo.repositories.in_memmory import TodoRepositoryInMemory
from app.todo.usecases.todo import TodoUseCase
from app.todo.delivery.todo_http_handler import TodoHttpHandler
from flask_swagger_ui import get_swaggerui_blueprint
from common.config import load_config

config = load_config('.env')

app = Flask(__name__)
app.register_blueprint(
    get_swaggerui_blueprint(
        '/docs',
        'http://localhost:{0}/specs/todo.yml'.format(config['port'])
    )
)


@app.route('/specs/<path:path>')
def send_report(path):
    return send_from_directory('docs', path)


# set slash not strict
app.url_map.strict_slashes = False

repo = TodoRepositoryInMemory()
usecase = TodoUseCase(repo)
TodoHttpHandler(usecase, app).handle()

if __name__ == '__main__':
    app.run(host=config['host'], port=config['port'], threaded=True, debug=config['debug'])
