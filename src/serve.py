from better_wyze import BetterWyze
from flask import Flask, render_template, request

wyze = BetterWyze()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lights', methods=['GET'])
def lights():
    # Get the switch state from the query parameter
    switch_state = request.args.get('on')

    # Perform some Python code execution based on the switch state
    if switch_state == 'true':
        wyze.turn_on_lights()
        result = "Lights turned on"
    else:
        wyze.turn_off_lights()
        result = "Lights turned off"

    return result

if __name__ == '__main__':
    wyze.login()
    wyze.get_devices()
    app.run(host="0.0.0.0", port=9991, debug=True)
