from flask import Flask
from flask import jsonify
import core

app = Flask(__name__)
APP_VERSION = 0.1


@app.route('/', methods=['GET'])
def root():
    return f'World Weather {APP_VERSION}'


@app.route('/api/bycityname/<string:cityname>', methods=['GET'])
def api(cityname):
    sanitized_query = core.sanitize_query(cityname)
    try:
        response = core.treat_response(core.request_weather_api(sanitized_query))
        return jsonify(response)
    except RuntimeError:
        error_response = {'response_code': '!200'}
        return jsonify(error_response)


if __name__ == '__main__':
    app.run(debug=True)
