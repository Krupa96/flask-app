from flask import Flask, jsonify, request
app = Flask(__name__)
customers = [{'name': 'John'}, {'name': 'Amy'}, {'name': 'Kate'}]

# @app.route('/users',methods=['GET'])
# def test():
#     return jsonify({'message': 'It Works!'})
@app.route('/users',methods=['GET'])
def returnall():
    return jsonify({'customers': customers})

@app.route('/users/<string:name>', methods=['GET'])
def returnone(name):
    names = [cname for cname in customers if cname['name'] == name]
    return jsonify({'cname': names[0]})

@app.route('/users', methods=['POST'])
def add_one():
    data = request.get_json()

    cname = {'name': data['name']}
    customers.append(cname)
    # return {'id': len(customers)}, 200
    return jsonify({'customers': customers})

@app.route('/users/<string:name>', methods=['PUT'])
def updateone(name):
    data = request.get_json()
    names = [cname for cname in customers if cname['name'] == name]
    names[0]['name'] = data['name']
    return jsonify({'cname': names[0]})

@app.route('/users/<string:name>', methods=['DELETE'])
def removeone(name):
    # data = request.get_json()
    name = [cname for cname in customers if cname['name'] == name]
    customers.remove(name[0])
    return jsonify({'customers': customers})

if __name__ == '__main__':
    app.run(debug=True)

