from flask import Flask, redirect, render_template, request

app = Flask(__name__)
data = {
    'ml': 1609,
    'yard': 0.9144,
    'ft': 30.48,
    'inch': 0.0254,
    'km': 1000,
    'meter': 1,
    'cm': 0.01,
    'mm': 0.001,
}


@app.route('/')
def index():
    return redirect('/length')


@app.route('/length')
def length():
    if request.values.get('value') is not None:
        value = request.values.get('value')
        convert_from = request.values.get('unit_from')
        convert_to = request.values.get('unit_to')
        meter_value = float(int(value) * data[convert_from])
        answer = float(meter_value / data[convert_to])
        message = '{} {} = {} {}'.format(value, convert_from, answer, convert_to)
        return render_template('length.html', message=message)
    else:
        return render_template('length.html', message=None)


if __name__ == '__main__':
    app.run('127.0.0.1', port=8080, debug=True)
