#API - trip_planning, trip_completed, trip_performance, safe_unsafe, device_performance, car_distance, trip_track,violations

import requests
import json
import flask
import datetime
from time import sleep
from datetime import time,timedelta
from flask import Flask, jsonify, request,json,make_response
from flask_cors import CORS
import pandas as pd
import numpy as np
import psycopg2
from itertools import chain, groupby
import math
import gzip
from requests.structures import CaseInsensitiveDict


app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


#RC-VERIFICATION PICHAIN
# @app.route('/vehicleNumberValidation', methods = ['GET'])

# def vehicleNumberValidation():
# 	conn = psycopg2.connect(host="127.0.0.1", port = 5432, database="ezyloads", user="ezyloads", password="ezy@1234")
# 	cur = conn.cursor()

# 	json_output = json.loads('{"success":"true", "message":"success" }')
	
# 	#try:
# 	vehicleNumber = request.args.get('vehicleNumber')

# 	if vehicleNumber:
# 		url = "https://api.pichainlabs.com/v1/rc/advance"

# 		headers = CaseInsensitiveDict()
# 		headers["Accept"] = "application/json"
# 		headers["org-id"] = "60b08e7c11c83687fb96aaf1"
# 		headers["apikey"] = "iZVSC7qfu0qXnLgwtKzEI7qGeuo4UvEc"
# 		headers["Content-Type"] = "application/json"

# 		data = {
# 			"rc_number": str(vehicleNumber),
# 			"chassis_number": "MA3FHEB1S00452500"
# 		}

# 		resp = requests.post(url, headers=headers, data=json.dumps(data))

# 		resp_json = json.loads(str(resp.text))

# 		json_output['vehicleDetails'] = resp_json
# 	else:
# 		json_output = json.loads('{"success":"false", "message":"vehicleNumber not found" }')

# 	# except Exception as e:
# 	# 	print(e)
# 	# finally:
# 	cur.close()
# 	conn.close()

# 	content = gzip.compress(json.dumps(json_output).encode('utf8'), 5)
# 	response = make_response(content)

# 	response.headers['Content-Encoding'] = 'gzip'
# 	response.headers['Content-length'] = len(content)

# 	return response

	#return jsonify(json_output) 

#RC-VERIFICATION ZOOP
@app.route('/vehicleNumberValidation', methods = ['GET'])

def vehicleNumberValidation():
	conn = psycopg2.connect(host="127.0.0.1", port = 5432, database="ezyloads", user="ezyloads", password="ezy@1234")
	cur = conn.cursor()

	json_output = json.loads('{"success":"true", "message":"success" }')
	
	try:
		vehicleNumber = request.args.get('vehicleNumber')

		if vehicleNumber:
			url = "https://live.zoop.one/api/v1/in/vehicle/rc/advance"

			headers = CaseInsensitiveDict()
			headers["Accept"] = "application/json"
			headers["app-id"] = "6192210302f92d001d6992aa"
			headers["api-key"] = "45M15KB-GMJMF6E-PTCVHXQ-Z1W2PRE"
			headers["Content-Type"] = "application/json"

			data = {
					"data": {
						"vehicle_registration_number": str(vehicleNumber),
						"consent": "Y",
						"consent_text": "I hear by declare my consent agreement for fetching my information via ZOOP API."
					}
				}

			resp = requests.post(url, headers=headers, data=json.dumps(data))

			resp_json = json.loads(str(resp.text))

			json_output['vehicleDetails'] = resp_json
		else:
			json_output = json.loads('{"success":"false", "message":"vehicleNumber not found" }')

	except Exception as e:
		print(e)
	finally:
		cur.close()
		conn.close()

	content = gzip.compress(json.dumps(json_output).encode('utf8'), 5)
	response = make_response(content)

	response.headers['Content-Encoding'] = 'gzip'
	response.headers['Content-length'] = len(content)

	return response

#GSTIN VERIFICATION
@app.route('/gstNumberValidation', methods = ['GET'])

def gstinNumberValidation():
	conn = psycopg2.connect(host="127.0.0.1", port = 5432, database="ezyloads", user="ezyloads", password="ezy@1234")
	cur = conn.cursor()

	json_output = json.loads('{"message":"success" }')
	
	try:
		gstNumber = request.args.get('gstNumber')

		if gstNumber:
			url = "https://live.zoop.one/api/v1/in/merchant/gstin/advance"

			headers = CaseInsensitiveDict()
			headers["Accept"] = "application/json"
			headers["app-id"] = "6192210302f92d001d6992aa"
			headers["api-key"] = "45M15KB-GMJMF6E-PTCVHXQ-Z1W2PRE"
			headers["Content-Type"] = "application/json"


			data = {
					"data": {
						"business_gstin_number": str(gstNumber),
						"consent": "Y",
						"consent_text": "I hear by declare my consent agreement for fetching my information via ZOOP API"
					}
				}

			resp = requests.post(url, headers=headers, data=json.dumps(data))

			resp_json = json.loads(str(resp.text))

			json_output['gstDetails'] = resp_json
		else:
			json_output = json.loads('{"success":"false", "message":"panNumber not found" }')

	except Exception as e:
		print(e)
	finally:
		cur.close()
		conn.close()

	content = gzip.compress(json.dumps(json_output).encode('utf8'), 5)
	response = make_response(content)

	response.headers['Content-Encoding'] = 'gzip'
	response.headers['Content-length'] = len(content)

	return response

#PAN VERIFICATION
@app.route('/panNumberValidation', methods = ['GET'])

def panNumberValidation():
	conn = psycopg2.connect(host="127.0.0.1", port = 5432, database="ezyloads", user="ezyloads", password="ezy@1234")
	cur = conn.cursor()

	json_output = json.loads('{"message":"success" }')
	
	try:
		panNumber = request.args.get('panNumber')

		if panNumber:
			url = "https://live.zoop.one/api/v1/in/identity/pan/lite"

			headers = CaseInsensitiveDict()
			headers["Accept"] = "application/json"
			headers["app-id"] = "6192210302f92d001d6992aa"
			headers["api-key"] = "45M15KB-GMJMF6E-PTCVHXQ-Z1W2PRE"
			headers["Content-Type"] = "application/json"


			data = {
					"data": {
						"customer_pan_number": str(panNumber),
						"consent": "Y",
						"consent_text": "I hear by declare my consent agreement for fetching my information via ZOOP API"
					}
				}

			resp = requests.post(url, headers=headers, data=json.dumps(data))

			resp_json = json.loads(str(resp.text))

			json_output['panDetails'] = resp_json
		else:
			json_output = json.loads('{"success":"false", "message":"panNumber not found" }')

	except Exception as e:
		print(e)
	finally:
		cur.close()
		conn.close()

	content = gzip.compress(json.dumps(json_output).encode('utf8'), 5)
	response = make_response(content)

	response.headers['Content-Encoding'] = 'gzip'
	response.headers['Content-length'] = len(content)

	return response

#DRIVER LICENSE VERIFICATION
@app.route('/dlNumberValidation', methods = ['GET'])

def dlNumberValidation():
	conn = psycopg2.connect(host="127.0.0.1", port = 5432, database="ezyloads", user="ezyloads", password="ezy@1234")
	cur = conn.cursor()

	json_output = json.loads('{"message":"success" }')
	
	try:
		dlNumber = request.args.get('dlNumber')
		dob = request.args.get('dob')

		if dlNumber and dob:
			url = "https://live.zoop.one/api/v1/in/identity/dl/advance"

			headers = CaseInsensitiveDict()
			headers["Accept"] = "application/json"
			headers["app-id"] = "6192210302f92d001d6992aa"
			headers["api-key"] = "45M15KB-GMJMF6E-PTCVHXQ-Z1W2PRE"
			headers["Content-Type"] = "application/json"


			data = {
					"data": {
						"customer_dl_number": str(dlNumber),
						"customer_dob": str(dob),
						"consent": "Y",
						"consent_text": "I hear by declare my consent agreement for fetching my information via ZOOP API"
					}
			}

			resp = requests.post(url, headers=headers, data=json.dumps(data))

			resp_json = json.loads(str(resp.text))

			json_output['driverLicenseDetails'] = resp_json
		else:
			json_output = json.loads('{"success":"false", "message":"panNumber not found" }')

	except Exception as e:
		print(e)
	finally:
		cur.close()
		conn.close()

	content = gzip.compress(json.dumps(json_output).encode('utf8'), 5)
	response = make_response(content)

	response.headers['Content-Encoding'] = 'gzip'
	response.headers['Content-length'] = len(content)

	return response

if __name__ == "__main__":
	app.run(host='demo2.transo.in',threaded = True,port=5004,ssl_context=('/etc/letsencrypt/live/demo2.transo.in/fullchain.pem', '/etc/letsencrypt/live/demo2.transo.in/privkey.pem'))
