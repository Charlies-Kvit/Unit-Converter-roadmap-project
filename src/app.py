from flask import Flask, redirect, render_template, request

app = Flask(__name__)
data = {"ml": 1, "cm": 10, "meter": 100, "km": 1000, "inch":}


@app.route('/')
def index():
    return redirect('/length')


@app.route('/length')
def length():
    if request.values.get('value') is not None:
        value = request.values.get('value')
        convert_from = request.values.get('unit_form')
        convert_to = request.values.get('unit_to')
        return
    else:
        return render_template('length.html', message=None)


if __name__ == '__main__':
    app.run('127.0.0.1', port=8080, debug=True)
