from flask import Flask, request
from flask import jsonify


app = Flask(__name__)


POST_LIST = []


@app.route('/post', methods=['GET'])
def get_posts():
    return jsonify(POST_LIST), 200


@app.route('/post', methods=['POST'])
def create_post():
    json = request.get_json(force=True)
    author = json.get('author', None)
    text_body = json.get('text', None)
    if author is None or text_body is None:
        return jsonify({'message': 'Bad request'}), 400
    d = {'text': text_body, 'author': author}
    POST_LIST.append(d)
    return jsonify({'message': 'Create OK'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

