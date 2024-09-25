from flask import Flask, redirect, render_template, request

app = Flask(__name__)

length_data = {
    'ml': 1609,
    'yard': 0.9144,
    'ft': 30.48,
    'inch': 0.0254,
    'km': 1000,
    'meter': 1,
    'cm': 0.01,
    'mm': 0.001
}
weight_data = {
    'mg': 0.000001,
    'gr': 0.001,
    'kg': 1,
    'ounce': 0.028349523125,
    'pound': 0.45359237
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
        if convert_from == convert_to:
            redirect("/")
        meter_value = float(float(value) * length_data[convert_from])
        answer = float(meter_value / length_data[convert_to])
        message = '{} {} = {} {}'.format(value, convert_from, answer, convert_to)
        return render_template('length.html', message=message)
    else:
        return render_template('length.html', message=None)


@app.route("/weight")
def weight():
    if request.values.get('value') is not None:
        value = request.values.get('value')
        convert_from = request.values.get('unit_from')
        convert_to = request.values.get('unit_to')
        if convert_from == convert_to:
            redirect("/weight")
        kilogram_value = float(float(value) * weight_data[convert_from])
        answer = float(kilogram_value / weight_data[convert_to])
        message = '{} {} = {} {}'.format(value, convert_from, answer, convert_to)
        return render_template('weight.html', message=message)
    else:
        return render_template('weight.html', message=None)


@app.route("/temperature")
def temperature():
    if request.values.get('value') is not None:
        value = request.values.get('value')
        convert_from = request.values.get('unit_from')
        convert_to = request.values.get('unit_to')
        if convert_from == convert_to:
            redirect("/temperature")
        if convert_from == "f":
            answer = (float(value) - 32) * (5 / 9)
            if convert_to == "k":
                answer += 273.15
        elif convert_from == "c":
            if convert_to == "f":
                answer = (float(value) * (9 / 5)) + 32
            elif convert_to == "k":
                answer = float(value) + 273.15
        else:
            answer = float(value) - 273.15
            if convert_to == "f":
                answer = (answer * (9 / 5)) + 32
        message = '{} {} = {} {}'.format(value, convert_from, answer, convert_to)
        return render_template('temperature.html', message=message)
    else:
        return render_template('temperature.html', message=None)


if __name__ == '__main__':
    app.run('127.0.0.1', port=8080, debug=True)
