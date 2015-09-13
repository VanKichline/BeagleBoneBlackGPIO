#!/usr/bin/python
import Adafruit_BBIO.GPIO as GPIO
from flask import Flask, render_template

app = Flask(__name__)
pinIn = "P9_27"

GPIO.setup(pinIn, GPIO.IN)

@app.route("/")
def hello():
	if GPIO.input(pinIn):
		buttonStatus = "on"
	else:
		buttonStatus = "off"
	templateData = {
		'buttonStatus': buttonStatus,
	}
	return render_template('main.html', **templateData)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=81, debug=True)

