from flask import Flask, redirect, url_for, request, render_template
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home1_2.html')

@app.route('/enternew')
def new_student():
    return render_template('Student1_2.html')

if __name__ == '__main__':
    app.run()