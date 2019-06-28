from flask import Flask, jsonify, Response, request

apm = 0

def add_keys(keys):
        global apm
        apm += keys
        return apm

def zero_apm():
        global apm
        apm = 0
        return "Great success"


app = Flask(__name__)
class Server():
        @app.route('/')
        def count():
                return jsonify(apm)

        @app.route('/reset')
        def reset():
                reply = zero_apm()
                return reply
                
        @app.route('/apm/<int:keys>')
        def update(keys):
                result = add_keys(keys)
                return jsonify(result)
        app.run(port=3048)

Server()