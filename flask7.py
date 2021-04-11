import webview
import pywebio
from pywebio.platform.flask import webio_view
from flask import Flask, escape, request, send_from_directory, render_template
from pywebio import STATIC_PATH
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import logging
from datetime import date, timedelta
from functools import partial

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")
    # name = request.args.get("name", "World")
    # msg = f'Hello, {escape(name)}!'
    # msg = msg + f'<br/><a href="/tool">View Tool</a>'
    # return msg


if __name__ == '__main__':
    # bmi()
    # webview.create_window('Hello world', pywebio.start_server(show_table, port=8888))
    # webview.start()
    # app = Flask(__name__)
    # log = logging.getLogger('werkzeug')
    # log.setLevel(logging.ERROR)
    # log.disabled = True

    # app.add_url_rule('/tool', 'webio_view', webio_view(layout_keys),
    #                  methods=['GET', 'POST', 'OPTIONS'])
    app.static_folder = 'static'
    app.debug = True
    app.run(host='localhost', port=8089)
    # webview.create_window('Flask example', app)
    # webview.start()
