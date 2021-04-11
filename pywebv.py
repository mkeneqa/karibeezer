import webview
import pywebio
from pywebio.platform.flask import webio_view
from flask import Flask, escape, request, send_from_directory
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
    name = request.args.get("name", "World")
    msg = f'Hello, {escape(name)}!'
    msg = msg + f'<br/><a href="/tool">View Tool</a>'
    return msg


def edit_row(choice, row):
    put_markdown("> You click`%s` button ar row `%s`" % (choice, row))


def show_table():
    put_buttons([
        dict(label=i, value=i, color=i)
        for i in ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark']
    ], onclick=put_text)
    hold()


def show_msg():
    put_text("You clicked the notification.")


def btn_click():
    # toast('New messages', position='right', color='#2188ff', duration=0)
    # put_markdown("> You click `%s` button" % btn_val)
    # with popup('Choose Your Best'):
    #     input('Input your Name', type=TEXT)
    #     input('Input your age', type=NUMBER)
    input('Input your age', type=NUMBER)
    print("input  Clicked")
    # popup('popup title', 'popup text content', size=PopupSize.SMALL)


def layout_keys():
    # put_buttons(['A', 'B', 'C'], onclick=btn_click)
    # put_buttons(["Edit"], onclick=btn_click)
    put_link("Go Home", "/")
    # put_table([
    #     ['A', 'B'],
    #     ['C', style(put_text('Red'), 'color: red; background-color:blue; border-radius:6px;padding:6px;')],
    # ])
    _my_style = 'color: #000; background-color:#f4f2f7; border-radius:6px;padding:6px;vertical-align: text-middle;font-weight:800;text-align:center;'
    # put_row([
    #     put_column([
    #         put_code('A'),
    #         put_row([
    #             put_buttons(['ABB']), None,
    #             put_code('B1'), None,  # None represents the space between the output
    #             put_code('B2'), None,
    #             style(put_link('B3 Link',"/"), _my_style), None,
    #         ]),
    #     ]), None,
    #     put_code('D'), None,
    #     put_code('E')
    # ])

    # put_row([
    #     put_column([
    #         put_code('A'),
    #         put_row([
    #             put_code('B1'), None,  # None represents the space between the output
    #             put_code('B2'), None,
    #             style(put_link('B3 Link', "/"), _my_style), None,
    #         ]),
    #         put_buttons(['C PopUp'], onclick=[btn_click]),
    #     ]), None,
    #     put_code('D'), None,
    #     put_code('E')
    # ])
    # hold()

    select('Which gift you want?', ['keyboard', 'ipad'])
    put_buttons(['edit', 'delete'], onclick=[show_msg, btn_click])
    hold()


def bmi():
    height = input("Input your height(cm)：", type=FLOAT)
    weight = input("Input your weight(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    print(f"YOUR BMI = {BMI}")

    top_status = [(16, 'Severely underweight'),
                  (18.5, 'Underweight'),
                  (25, 'Normal'),
                  (30, 'Overweight'),
                  (35, 'Moderately obese'),
                  (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
            break


if __name__ == '__main__':
    # bmi()
    # webview.create_window('Hello world', pywebio.start_server(show_table, port=8888))
    # webview.start()
    # app = Flask(__name__)
    # log = logging.getLogger('werkzeug')
    # log.setLevel(logging.ERROR)
    # log.disabled = True

    app.add_url_rule('/tool', 'webio_view', webio_view(layout_keys),
                     methods=['GET', 'POST', 'OPTIONS'])
    # app.run(host='localhost', port=8089)
    webview.create_window('Flask example', app)
    webview.start()
