#!/usr/bin/python
from flask import Flask, session, request
import os
#Source: https://www.youtube.com/watch?v=T1ZVyY1LWOg&list=PLXmMXHVSvS-CMpHUeyIeqzs3kl-tIG-8R&index=2
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
	session['user'] = 'Mark'
	return 'Index'

@app.route('/getsession')
def getsession():
	if 'user' in session:
		return session['user']
	return 'Not logged in!'

@app.route('/dropsession')
def dropsession():
	session.pop('user', None)
	return 'Session dropped'
if __name__ == "__main__":
    app.run()

