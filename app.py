from flask import Flask
from flask import jsonify
import core
import os

app = Flask(__name__)
APP_VERSION = 0.1


@app.route('/', methods=['GET'])
def root():
    return f'World Weather {APP_VERSION}'


@app.route('/api/bycityname/<string:cityname>', methods=['GET'])
def api(cityname):
    sanitized_query = core.sanitize_query(cityname)
    try:
        response = core.request_weather_api(sanitized_query)
        response = core.treat_response(response)
        return jsonify(response)
    except RuntimeError:
        error_response = {'response_code': '!200'}
        return jsonify(error_response)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
