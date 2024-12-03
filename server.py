from flask import request, jsonify, Flask
import init


sd = lambda: init.get_stardict()

app = Flask(__name__)


@app.route('/get')
def index():
    word = request.args.get("word")
    result = sd().query(word)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
