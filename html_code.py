from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/distribution')
def index():
    return render_template('base.html', title='Заготовка')


if __name__ == '__main__':
    app.run(port=8064, host='127.0.0.1')