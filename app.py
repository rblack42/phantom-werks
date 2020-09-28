import os
from flask import Flask
from whitenoise import WhiteNoise


app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app,
        root=os.path.join(os.path.dirname(__file__), 'docs'),
        prefix='')

@app.route("/hello")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()


