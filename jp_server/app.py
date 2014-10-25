#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

import json

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	r = requests.get("http://data.cityofnewyork.us/resource/v7f4-gjgr.json")
	pothole_object = json.loads(r.text)

	potholes = []
	
	for i in range(len(pothole_object)):

		longitude = ""
		latitude = ""
		zip_code = ""

		try:
			longitude = pothole_object[i]["longitude"]
			latitude = pothole_object[i]["latitude"]
			zip_code = pothole_object[i]["incident_zip"]
		except KeyError:
			print "this does not have lat or long"

		
		potholes.append("longitude " + longitude + " and latitude " + latitude + " and zip code is " + zip_code)

	return str(potholes)

if __name__ == '__main__':
	app.run(debug=True)

