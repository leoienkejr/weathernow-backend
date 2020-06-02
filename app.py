from flask import Flask

app = Flask(__name__)
APP_VERSION = 0.1


@app.route('/')
def root():
    return f'<h3>World Weather {APP_VERSION}</h3>'


@app.route('/api/bycityname/<string:cityname>', methods=['GET'])
def api(cityname):
    return cityname


if __name__ == '__main__':
    app.run(debug=True)
