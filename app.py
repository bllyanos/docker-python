from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def list_users():
    return jsonify(users)


@app.route('/add')
def add_user():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    users.append({
        "name": name,
        "age": age
    })
    return jsonify(users)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
