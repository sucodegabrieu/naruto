from os import environ
from flask import Flask

app = Flask(__name__)
app.run(host= '170.0.59.189', port=environ.get('PORT'))
