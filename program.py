from flask import Flask, render_template

app = Flask(__name__)

@app.route('/distribution')
def distribute():
    command = [str(i) for i in range(10)]
    return render_template('По каютам!.html', com=command)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
