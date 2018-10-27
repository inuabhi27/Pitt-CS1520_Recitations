#!/usr/bin/python
#Source: https://overiq.com/flask/0.12/cookies-in-flask/
from flask import Flask, render_template, request, redirect, url_for, flash, make_response

app = Flask(__name__)
@app.route('/cookie/')
def cookie():
    res = make_response("Setting a cookie")
    res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    return res

@app.route('/delete-cookie/')
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie('foo', 'bar', max_age=0)
    return res
if __name__ == "__main__":
    app.run()


	