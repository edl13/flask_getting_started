from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/name', methods=['GET'])
def get_name():
    '''Returns my name (Edward Liang) as JSON'''

    name_dict = {'name': 'Edward Liang'}
    return jsonify(name_dict)


@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    '''Returns "Hello there, <:name."'''

    hello_dict = {'message': 'Hello there, {}'.format(name)}
    return jsonify(hello_dict)


@app.route('/distance', methods=['POST'])
def distance():
    '''Returns the distance of two points from input JSON'''

    r = request.get_json()
    point_a = r['a']
    point_b = r['b']

    dis = getDis(point_a, point_b)

    dis_dict = {
        'Distance': dis,
        'a': point_a,
        'b': point_b
    }

    return jsonify(dis_dict)


def getDis(a, b):
    '''Return distance between a and b
    :param a: len 2 list (x, y)
    :param b: len 2 list (x, y)
    :return: Distance between a and b
    '''

    dis = ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5
    return dis
