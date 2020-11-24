from flask import Flask, request, jsonify, json
from scripts.handlers.my_app_handler import create, my_search, update, delete

app = Flask(__name__)


@app.route("/find_user")
def find_user():
    name = request.args.get("name")
    query = {
        "name": name
    }
    response = my_search(query=query)

    return jsonify(response)


@app.route("/create_user", methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    address = data['address']
    d = {'name': name, 'address': address}
    response = create(d)
    return json.dumps(response)


@app.route('/update_users', methods=['PUT'])
def update_one():
    data = request.get_json()
    f_query = data['fname']
    f_update = {"name": f_query}
    t_query = data['uname']
    t_update = {"$set": {"name": t_query}}
    response = update(query=f_update, new_value=t_update)
    return json.dumps(response)


@app.route('/delete_users', methods=['DELETE'])
def delete_one():
    data = request.get_json()
    name = data['name']
    d = {'name': name}
    response = delete(d)
    return json.dumps(response)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
