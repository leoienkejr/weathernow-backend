from flask import Flask
import core

app = Flask(__name__)
APP_VERSION = 0.1


@app.route('/', methods=['GET'])
def root():
    return f'World Weather {APP_VERSION}'


@app.route('/api/bycityname/<string:cityname>', methods=['GET'])
def api(cityname):
    return core.sanitize_query(cityname)


if __name__ == '__main__':
    app.run(debug=True)
