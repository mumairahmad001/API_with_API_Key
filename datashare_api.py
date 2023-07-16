from flask import Flask, request, jsonify
# from flask_restful import Resource, Api, reqparse
# import pandas as pd
import ast, requests, json

app = Flask(__name__)
api_keys = {'1db4f85ce1701159b1a770771c831db975d4fd279af31b29': '/getname' }

@app.route('/getname', methods=['GET'])
def getname():
    api_key = request.headers.get ('X-API-Key')
    if api_key and api_key in api_keys:
        uname = request.args.get('user')
        # data = {'message': 'Access Granted'}
        return jsonify({'message':f'Access Granted to the getname Method for {uname} - This endpoint is secured'}), 200
    else:
        return {'Error':f'Unauthorized Request'}, 401


@app.route('/apistatus', methods=['GET'])
def startapi():
    api_key = request.headers.get ('X-API-Key')
    if api_key and api_key in api_keys:
        return jsonify({'message':f'API Started - This endppoint is secured'}), 200
    else:
        return {'Error': f'Couldn''t connect to the API'}, 401

def main(request):
    return app(request)

if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=8080, ssl_context='adhoc')
    # app.run(host='127.0.0.1', port=8080, debug=True, ssl_context=('cert.pem', 'key.pem'))
    app.run()
