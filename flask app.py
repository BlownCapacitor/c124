from flask import Flask, jsonify, Request
from werkzeug.wrappers import request

contact_app = Flask(__name__)

#Phone numbers changed for privacy
contacts = [{
    'id': 1,

    'Number': u'0000000001',
    'Name': u'Akshay'
 },
 {
    'id': 2,
    'Number': u'0000000002',
    'Name': u'Shreyank',
    
 }]
@contact_app.route("/get-data")

def getContact():
    return jsonify({
       'data': contacts
    })

@contact_app.route("/add-data", methods = ['POST'])

def add_task():
    if not request.json:
        return jsonify({
            'status' : 'ERROR',
            'message': 'Unable to find data'
        },
        400)
    names = {
        'id': [-1]['id'] +1,
        'Number': request.json.get(['Number']),
        'Name': request.json.get('Name'),
        
    }
    contacts.append(contacts)
    return jsonify({
        'status': 'success',
        'message':'task added successfully'
    })

if __name__ == '__main__':
    contact_app.run(debug = True)
