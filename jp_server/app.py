#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

import json

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	r = requests.get("http://data.cityofnewyork.us/resource/v7f4-gjgr.json")
	pothole_object = json.loads(str(r.text))
	print pothole_object[0]
	return pothole_object[0]

if __name__ == '__main__':
	app.run()

