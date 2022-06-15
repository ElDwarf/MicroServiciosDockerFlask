from flask import Flask, request
from flask import jsonify


app = Flask(__name__)


USER_LIST = [
    {'id': 1, 'name': 'ADMIN', 'username': 'admin'},
    {'id': 2, 'name': 'Pablo Dalmasso', 'username': 'pdalmasso'},
    {'id': 3, 'name': 'Santiago Perez', 'username': 'sperez'},
    {'id': 4, 'name': 'Vanesa Olmo', 'username': 'volmo'}
]


def get_user_by_id(user_id):
    user_response = None
    for user in USER_LIST:
        if user['id'] == user_id:
            user_response = user
    return user_response


def get_user_by_username(username):
    user_response = None
    for user in USER_LIST:
        if user['username'] == username:
            user_response = user
    return user_response


@app.route('/api/user/<user_id>', methods=['GET'])
def user_data(user_id):
    user = get_user_by_id(int(user_id))
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user)


@app.route('/api/user/login', methods=['POST'])
def login():
    json = request.get_json(force=True)
    username = json.get('username')
    if username is None:
        return jsonify({'message': 'Bad request'}), 400
    user = get_user_by_username(username)
    if user is None:
        return jsonify({'message': 'User not found'}), 401
    return jsonify(get_user_by_username(username)), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


































