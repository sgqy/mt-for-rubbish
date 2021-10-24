#!/usr/bin/env python3
import json
from flask import Flask, request, Response
import HS

app = Flask(__name__)
hs = HS.HS('table.tsv')

def conv(q):
	try:
		return hs.conv(q)
	except Exception as e:
		return "Error: " + str(e)

@app.route('/t', methods=['GET', 'POST'])
def t():
	s = request.form.get('s') or request.args.get('s')
	t = request.form.get('t') or request.args.get('t')
	q = request.form.get('q') or request.args.get('q')
	return json.dumps({"t": conv(q)})

@app.route('/load', methods=['GET', 'POST'])
def load():
	hs.load('table.tsv')
	return Response(str(hs) + '\n', content_type='text/plain; charset=utf-8')

app.run(host='0.0.0.0', port=9999)
