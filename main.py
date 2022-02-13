import json

from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/base')

def odd_even():
    return render_template('base.html', title='Заготовка')

@app.route('/training/<prof>')
def professional(prof):
    return render_template('example.html', prof=prof, title='Cпециальность')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
