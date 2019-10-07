from os import environ
from flask import Flask

app = Flask(__name__)
app.run(host= 'https://terterert.herokuapp.com', port=environ.get('PORT'))
